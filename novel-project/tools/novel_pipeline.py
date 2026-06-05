#!/usr/bin/env python3
"""
小说长期生产流水线。

设计目标：
- 自动识别下一章，按章节卡/大纲/资产库/前文上下文生成任务包。
- 可选调用外部 LLM/Codex 命令，默认只生成提示包，避免误耗额度。
- 每生成尾数为 0 或 5 的章节后，先审查该五章段质量，再进入下一轮。
- 用本地状态文件记录预算、上下文估算、阻塞原因和产出路径，便于长期恢复。
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
PROJECT_DIR = ROOT / "novel-project"
TEXT_DIR = PROJECT_DIR / "正文"
STATE_DIR = PROJECT_DIR / ".pipeline"
STATE_FILE = STATE_DIR / "state.json"
PROMPT_DIR = STATE_DIR / "prompts"
OUTPUT_DIR = STATE_DIR / "outputs"
CONTINUITY_DIR = STATE_DIR / "continuity"
LOG_FILE = STATE_DIR / "pipeline.log"

DEFAULT_CONTEXT_TOKENS = 24000
DEFAULT_RESERVE_OUTPUT_TOKENS = 6500
DEFAULT_DAILY_BUDGET_TOKENS = 120000

PLAN_RECONSTRUCTION = PROJECT_DIR / "08-全流程重构计划.md"
PLAN_PROGRESS = PROJECT_DIR / "重构进度表.md"
PLAN_OUTLINE = PROJECT_DIR / "42-新版全书完整大纲.md"
PLAN_FILES = (PLAN_RECONSTRUCTION, PLAN_PROGRESS, PLAN_OUTLINE)


CHAPTER_DRAFT_RE = re.compile(r"第(?P<num>\d{3})章_(?P<title>.+?)_重构稿\.md$")
CHAPTER_EVAL_RE = re.compile(r"第(?P<num>\d{3})章_(?P<title>.+?)_重构评估\.md$")
CHAPTER_CARD_RE = re.compile(r"第(?P<num>\d+)章重构章节卡\.md$")
FILE_BLOCK_RE = re.compile(
    r"^### FILE:\s*(?P<path>[^\n]+)\n(?P<body>.*?)(?=^### FILE:|\Z)",
    re.MULTILINE | re.DOTALL,
)


@dataclass(frozen=True)
class PipelineConfig:
    chapter: int | None
    max_cycles: int
    dry_run: bool
    llm_command: str | None
    context_tokens: int
    reserve_output_tokens: int
    daily_budget_tokens: int
    force_audit: bool
    skip_llm: bool
    respect_progress_gate: bool
    quota_poll_seconds: int
    quota_max_wait_seconds: int
    stop_after_audit_checkpoint: bool
    restart_after_audit: bool


@dataclass(frozen=True)
class ContextFile:
    path: Path
    reason: str
    priority: int


@dataclass(frozen=True)
class PlanStep:
    chapter: int
    stage: str
    source: str
    instruction: str
    required_plan_files: tuple[Path, ...]


def ensure_dirs() -> None:
    for path in (STATE_DIR, PROMPT_DIR, OUTPUT_DIR, CONTINUITY_DIR):
        path.mkdir(parents=True, exist_ok=True)


def now_iso() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def estimate_tokens(text: str) -> int:
    # 中文正文通常接近 1.5-2 字/Token；这里取保守估算，给上下文留余量。
    return max(1, int(len(text) / 1.6))


def read_text(path: Path, limit_tokens: int | None = None) -> str:
    text = path.read_text(encoding="utf-8")
    if limit_tokens is None or estimate_tokens(text) <= limit_tokens:
        return text

    chars = max(800, int(limit_tokens * 1.6))
    head = text[: chars // 2]
    tail = text[-chars // 2 :]
    return f"{head}\n\n……【中段因上下文预算被裁剪】……\n\n{tail}"


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {
            "created_at": now_iso(),
            "runs": [],
            "daily_usage": {},
            "last_success_chapter": None,
            "blocked": False,
            "blocked_reason": None,
        }
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def append_log(message: str) -> None:
    LOG_FILE.write_text(
        (LOG_FILE.read_text(encoding="utf-8") if LOG_FILE.exists() else "")
        + f"[{now_iso()}] {message}\n",
        encoding="utf-8",
    )


def chapter_drafts() -> list[Path]:
    if not TEXT_DIR.exists():
        return []
    return sorted(
        [p for p in TEXT_DIR.iterdir() if p.is_file() and CHAPTER_DRAFT_RE.match(p.name)]
    )


def chapter_evals() -> list[Path]:
    if not TEXT_DIR.exists():
        return []
    return sorted(
        [p for p in TEXT_DIR.iterdir() if p.is_file() and CHAPTER_EVAL_RE.match(p.name)]
    )


def chapter_number(path: Path, pattern: re.Pattern[str]) -> int:
    match = pattern.match(path.name)
    if not match:
        raise ValueError(f"无法解析章节编号：{path}")
    return int(match.group("num"))


def latest_chapter() -> int:
    drafts = chapter_drafts()
    if not drafts:
        return 0
    return max(chapter_number(path, CHAPTER_DRAFT_RE) for path in drafts)


def latest_project_doc_index() -> int:
    max_index = 0
    for path in PROJECT_DIR.glob("*.md"):
        match = re.match(r"(?P<num>\d+)-", path.name)
        if match:
            max_index = max(max_index, int(match.group("num")))
    return max_index


def next_card_path(chapter: int) -> Path:
    existing = find_card(chapter)
    if existing:
        return existing
    chapter_offset = max(1, chapter - latest_chapter())
    return PROJECT_DIR / f"{latest_project_doc_index() + chapter_offset:02d}-第{chapter}章重构章节卡.md"


def extract_next_section(text: str) -> str:
    match = re.search(r"##\s*[四4]、下一步(?P<body>.*?)(?=\n##\s|\Z)", text, re.DOTALL)
    if match:
        return match.group("body").strip()
    match = re.search(r"##\s*下一步(?P<body>.*?)(?=\n##\s|\Z)", text, re.DOTALL)
    if match:
        return match.group("body").strip()
    return ""


def chapter_from_text(text: str) -> int | None:
    patterns = [
        r"生成\s*`?\d+-第(?P<num>\d+)章重构章节卡",
        r"第\s*(?P<num>\d+)\s*章章节卡",
        r"第\s*(?P<num>\d+)\s*章正文",
        r"第\s*(?P<num>\d+)\s*章准备",
        r"第(?P<num>\d{3})章_",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return int(match.group("num"))
    return None


def current_stage_from_plan(chapter: int) -> str:
    if chapter <= 5:
        return "阶段四：黄金五章正文重构"
    if chapter <= 20:
        return "阶段四：第一卷正文重构"
    if chapter <= 31:
        return "阶段四：根据新资产库调整第 21-31 章旧稿"
    if chapter <= 100:
        return "阶段四：规划并生成第 32-100 章"
    return "阶段五：完稿终审与进度闭环"


def build_plan_step(config: PipelineConfig) -> PlanStep:
    progress_text = PLAN_PROGRESS.read_text(encoding="utf-8") if PLAN_PROGRESS.exists() else ""
    next_section = extract_next_section(progress_text)
    planned_chapter = chapter_from_text(next_section) or chapter_from_text(progress_text)
    chapter = config.chapter or planned_chapter or latest_chapter() + 1
    stage = current_stage_from_plan(chapter)
    if config.chapter:
        source = "用户通过 `--chapter` 指定章节，三份路线图用于校验边界"
        instruction = (
            f"用户指定推进第 {chapter:03d} 章。执行前仍需核对 `08-全流程重构计划.md`、"
            "`重构进度表.md`、`42-新版全书完整大纲.md`，若与当前进度冲突必须说明。"
        )
    elif next_section:
        source = "从 `重构进度表.md` 的“下一步”章节提取"
        instruction = next_section
    else:
        source = "未找到明确“下一步”，回退到最新正文后一章"
        instruction = f"根据当前正文最新完成第 {latest_chapter():03d} 章，推进第 {chapter:03d} 章。"
    return PlanStep(
        chapter=chapter,
        stage=stage,
        source=source,
        instruction=instruction,
        required_plan_files=PLAN_FILES,
    )


def find_draft(num: int) -> Path | None:
    prefix = f"第{num:03d}章_"
    for path in chapter_drafts():
        if path.name.startswith(prefix):
            return path
    return None


def find_eval(num: int) -> Path | None:
    prefix = f"第{num:03d}章_"
    for path in chapter_evals():
        if path.name.startswith(prefix):
            return path
    return None


def find_card(num: int) -> Path | None:
    for path in PROJECT_DIR.glob(f"*-第{num}章重构章节卡.md"):
        if CHAPTER_CARD_RE.search(path.name):
            return path
    for path in PROJECT_DIR.glob(f"*第{num}章重构章节卡.md"):
        return path
    return None


def find_continuity(num: int) -> Path | None:
    path = CONTINUITY_DIR / f"第{num:03d}章_连贯性摘要.md"
    return path if path.exists() else None


def first_existing(paths: Iterable[Path]) -> list[Path]:
    return [path for path in paths if path.exists()]


def build_context_files(chapter: int, audit: bool = False) -> list[ContextFile]:
    files: list[ContextFile] = []

    base_paths = first_existing(
        [
            ROOT / "AGENTS.md",
            ROOT / ".codex/rules/project_rules.md",
            ROOT / ".codex/skills/README.md",
            ROOT / ".codex/skills/创作质量优先级.md",
            PLAN_RECONSTRUCTION,
            PLAN_PROGRESS,
            PLAN_OUTLINE,
            PROJECT_DIR / "小说资产库.md",
            PROJECT_DIR / "10-人物压力测试与群像轮转.md",
            PROJECT_DIR / "11-案件引擎与小说资产库.md",
        ]
    )
    for path in base_paths:
        if path in PLAN_FILES:
            files.append(ContextFile(path, "路线图最高依据", 0))
        else:
            files.append(ContextFile(path, "长期规则/大纲/资产", 1))

    card = find_card(chapter)
    if card:
        files.append(ContextFile(card, f"第 {chapter} 章章节卡", 0))

    previous_range = range(max(1, chapter - 3), chapter)
    for num in previous_range:
        draft = find_draft(num)
        evaluation = find_eval(num)
        continuity = find_continuity(num)
        recency_priority = 3 + (chapter - 1 - num) * 2
        if continuity:
            files.append(ContextFile(continuity, f"第 {num} 章连贯性摘要", recency_priority - 1))
        if draft:
            files.append(ContextFile(draft, f"第 {num} 章前文承接", recency_priority))
        if evaluation:
            files.append(ContextFile(evaluation, f"第 {num} 章风险建议", recency_priority + 1))

    if audit:
        start = max(1, chapter - 4)
        for num in range(start, chapter + 1):
            draft = find_draft(num)
            evaluation = find_eval(num)
            if draft:
                files.append(ContextFile(draft, f"五章审计正文：第 {num} 章", 2))
            if evaluation:
                files.append(ContextFile(evaluation, f"五章审计既有评估：第 {num} 章", 3))

    unique: dict[Path, ContextFile] = {}
    for item in files:
        if item.path not in unique or item.priority < unique[item.path].priority:
            unique[item.path] = item
    return sorted(unique.values(), key=lambda item: (item.priority, str(item.path)))


def render_context(files: list[ContextFile], budget_tokens: int) -> tuple[str, int, list[str]]:
    chunks: list[str] = []
    used = 0
    included: list[str] = []

    for item in files:
        remaining = budget_tokens - used
        if remaining <= 600:
            break
        per_file_limit = per_file_budget(item, remaining)
        body = read_text(item.path, per_file_limit)
        token_count = estimate_tokens(body)
        if used + token_count > budget_tokens:
            body = read_text(item.path, max(600, budget_tokens - used))
            token_count = estimate_tokens(body)
        rel = item.path.relative_to(ROOT)
        chunks.append(f"\n\n## {rel}\n\n用途：{item.reason}\n\n{body}")
        included.append(str(rel))
        used += token_count

    return "".join(chunks).strip(), used, included


def per_file_budget(item: ContextFile, remaining: int) -> int:
    rel = item.path.relative_to(ROOT).as_posix()
    if item.priority == 0:
        target = 4200
    elif rel in {"AGENTS.md", ".codex/rules/project_rules.md"}:
        target = 700
    elif rel == ".codex/skills/README.md":
        target = 900
    elif rel == ".codex/skills/创作质量优先级.md":
        target = 1600
    elif rel.endswith("重构进度表.md"):
        target = 1800
    elif rel.endswith("42-新版全书完整大纲.md"):
        target = 2600
    elif rel.endswith("小说资产库.md"):
        target = 2600
    elif "案件引擎" in rel:
        target = 1800
    elif "人物压力测试" in rel:
        target = 1400
    elif item.priority == 2:
        target = 2400
    elif item.priority == 3:
        target = 1200
    elif item.priority == 4:
        target = 1100
    else:
        target = 900
    return min(remaining, target)


def generation_prompt(
    chapter: int,
    context: str,
    included_files: list[str],
    plan_step: PlanStep,
) -> str:
    card = find_card(chapter)
    if card:
        card_instruction = "已有章节卡。必须严格按章节卡执行，不得擅自改主线答案。"
    else:
        card_instruction = (
            "未找到本章章节卡。先基于全书大纲和资产库生成章节卡，再生成正文和评估。"
        )
    card_rel = next_card_path(chapter).relative_to(ROOT)
    plan_files = [str(path.relative_to(ROOT)) for path in plan_step.required_plan_files]

    return f"""你现在是小说生产流水线架构师与执行器。

任务：按路线图执行第 {chapter:03d} 章的下一步产物，不越过 `重构进度表.md` 当前允许推进的范围。

本轮计划来源：{plan_step.source}

当前阶段：{plan_step.stage}

路线图文件最高优先级：
{json.dumps(plan_files, ensure_ascii=False, indent=2)}

本轮计划指令：
{plan_step.instruction}

硬性规则：
1. 全程中文输出。
2. 必须先核对 `08-全流程重构计划.md`、`重构进度表.md`、`42-新版全书完整大纲.md`，三者冲突时以 `重构进度表.md` 的当前状态和下一步为最近事实，以 `42-新版全书完整大纲.md` 的章节安排为剧情边界，以 `08-全流程重构计划.md` 的阶段链路为流程边界。
3. 遵循项目规则：客观中立、最优决策、重要决策记录依据。
4. 执行技能链：plot-architect 章节卡 → character-designer 人物状态 → content-writer 正文 → quality-evaluator 质量闸门 → plagiarism-checker 项目内原创性风险 → progress-tracker 进度记录。
5. {card_instruction}
6. 正文字数目标：汉字约 3000，最多不超过 4000。
7. 章节必须具备目标、阻碍、代价、变化、章末钩子；开头 800 字内必须出现异常/冲突/强信息差之一。
8. 原创性审查只能声明“项目内风险分型”，不得宣称覆盖外部平台查重。
9. 若发现资料不足、上下文冲突、进度表提示暂缓批量推进，或本轮不应进入正文，必须输出阻塞报告，不要硬写。
10. 如果 `重构进度表.md` 明确要求“章节卡/正文准备”而不是完整正文，优先产出章节卡、写作策略和计划核对；正文和评估文件块可以暂不输出，并在进度记录说明暂缓依据。

输出格式必须严格使用以下文件块，脚本会据此写入文件：

### FILE: {card_rel}
这里放章节卡。如果本章已有章节卡，可以不输出这个文件块。

### FILE: novel-project/正文/第{chapter:03d}章_章节标题_重构稿.md
这里放正文终稿。若本轮按路线图只允许做章节卡/正文准备，可以不输出这个文件块。

### FILE: novel-project/正文/第{chapter:03d}章_章节标题_重构评估.md
这里放质量评估、原创性风险结论、问题分诊、下一章接力点。若本轮未生成正文，可以不输出这个文件块。

### FILE: novel-project/.pipeline/progress_updates/第{chapter:03d}章_进度记录.md
这里记录本轮关键决策、依据、产出、风险和下一步。

### FILE: novel-project/.pipeline/plan_steps/第{chapter:03d}章_计划执行核对.md
这里记录本轮如何依据三份路线图推进、是否存在冲突、采用哪个决策依据。

上下文文件清单：
{json.dumps(included_files, ensure_ascii=False, indent=2)}

下面是已压缩上下文：

{context}
"""


def stage_prompt(
    chapter: int,
    kind: str,
    context: str,
    included_files: list[str],
    plan_step: PlanStep,
    config: PipelineConfig,
) -> str:
    card_rel = next_card_path(chapter).relative_to(ROOT)
    draft_hint = f"novel-project/正文/第{chapter:03d}章_章节标题_重构稿.md"
    eval_hint = f"novel-project/正文/第{chapter:03d}章_章节标题_重构评估.md"
    continuity_hint = f"novel-project/.pipeline/continuity/第{chapter:03d}章_连贯性摘要.md"
    progress_hint = f"novel-project/.pipeline/progress_updates/第{chapter:03d}章_进度记录.md"
    plan_hint = f"novel-project/.pipeline/plan_steps/第{chapter:03d}章_计划执行核对.md"
    plan_files = [str(path.relative_to(ROOT)) for path in plan_step.required_plan_files]
    gate_text = (
        "若进度表只允许章节卡/正文准备，可以暂缓正文。"
        if config.respect_progress_gate
        else "本轮按无人值守严格模式执行，不因“正文准备”字样跳过正文和评估。"
    )
    common = f"""你现在是小说生产流水线的无人值守执行器。

任务章节：第 {chapter:03d} 章
执行阶段：{kind}
本轮计划来源：{plan_step.source}
当前阶段：{plan_step.stage}
路线图文件最高优先级：
{json.dumps(plan_files, ensure_ascii=False, indent=2)}

本轮计划指令：
{plan_step.instruction}

硬性规则：
1. 全程中文输出。
2. 必须先核对 `08-全流程重构计划.md`、`重构进度表.md`、`42-新版全书完整大纲.md`。
3. 三份路线图冲突时，以 `重构进度表.md` 的当前事实为最近事实，以 `42-新版全书完整大纲.md` 的章节安排为剧情边界，以 `08-全流程重构计划.md` 的阶段链路为流程边界。
4. {gate_text}
5. 输出必须使用指定 `### FILE:` 文件块；不要输出未指定路径的文件。
6. 如发现无法继续，输出阻塞报告到指定进度/计划文件块，并明确阻塞证据。

上下文文件清单：
{json.dumps(included_files, ensure_ascii=False, indent=2)}

下面是已压缩上下文：

{context}
"""

    if kind == "card":
        return f"""{common}

本阶段目标：生成或修订第 {chapter:03d} 章章节卡，必须服务全书大纲和上一章接力。

章节卡必须包含：
- 章节定位、所属案件、核心功能、字数目标。
- 上章钩子兑现方式。
- 本章目标、阻碍、代价、局面变化、章末钩子。
- 3-4 个主场景设计：空间压力、动作节拍、功能道具、主导感官。
- 人物状态、伏笔与资产、原创性风险边界、下一章接力点。
- 决策依据：说明为什么这是当前路线图下最稳的方案。

输出格式：

### FILE: {card_rel}
这里放第 {chapter:03d} 章章节卡。

### FILE: {plan_hint}
这里记录本章章节卡如何对应三份路线图、是否存在偏差、采用的决策依据。
"""

    if kind == "draft":
        card = find_card(chapter)
        card_line = f"必须严格执行章节卡 `{card.relative_to(ROOT)}`。" if card else "未检测到章节卡时必须先输出阻塞报告，不要硬写正文。"
        return f"""{common}

本阶段目标：生成第 {chapter:03d} 章正文终稿。

正文硬标准：
- {card_line}
- 汉字约 3000，最多不超过 4000。
- 开头 800 字内必须出现异常、冲突或强信息差。
- 必须完成目标、阻碍、代价、变化、章末钩子。
- 必须承接上一章情绪债/信息债，并给下一章留下具体接力问题。
- 保持人物状态、案件线索、伏笔和语言风格与连贯性摘要一致。

输出格式：

### FILE: {draft_hint}
这里放第 {chapter:03d} 章正文终稿。
"""

    if kind == "evaluate":
        draft = find_draft(chapter)
        draft_line = f"必须评估正文 `{draft.relative_to(ROOT)}`。" if draft else "未检测到正文时必须输出阻塞报告，不得虚构评估。"
        return f"""{common}

本阶段目标：生成第 {chapter:03d} 章章节评估。

评估硬标准：
- {draft_line}
- 按 P0-P19 检查，重点是追读闭环、案件公平性、人物压力、场景调度、章末接力。
- 给出总分、通过/有条件通过/不通过结论。
- 包含项目内原创性风险分型，禁止宣称覆盖外部平台查重。
- 若不通过，必须按结构、人物动机、追读、场景、语言的顺序分诊。

输出格式：

### FILE: {eval_hint}
这里放第 {chapter:03d} 章重构评估。
"""

    if kind == "continuity":
        return f"""{common}

本阶段目标：生成第 {chapter:03d} 章连贯性摘要和进度记录，供下一章优先读取。

连贯性摘要必须包含：
- 本章结束时案件状态。
- 人物状态变化：陆行舟、苏晚、秦墨寒、周明远及本案关键人物。
- 新增/回收/悬而未决伏笔。
- 情绪债、信息债、爽点债。
- 下一章必须兑现或延迟兑现的接力点。
- 禁止下一章重复使用的钩子、误导、场景或爽点。
- 需要写入/同步到正式进度表的建议条目。

输出格式：

### FILE: {continuity_hint}
这里放第 {chapter:03d} 章连贯性摘要。

### FILE: {progress_hint}
这里放第 {chapter:03d} 章进度记录、产物路径、质量结论和下一步。
"""

    raise ValueError(f"未知阶段：{kind}")


def audit_prompt(
    chapter: int,
    context: str,
    included_files: list[str],
    plan_step: PlanStep,
) -> str:
    start = max(1, chapter - 4)
    plan_files = [str(path.relative_to(ROOT)) for path in plan_step.required_plan_files]
    return f"""你现在是小说生产流水线的五章质量闸门。

任务：审查第 {start:03d}-{chapter:03d} 章是否合格。由于第 {chapter:03d} 章尾数为 0 或 5，必须完成本审查后才能进入下一循环。

本轮计划来源：{plan_step.source}

当前阶段：{plan_step.stage}

路线图文件最高优先级：
{json.dumps(plan_files, ensure_ascii=False, indent=2)}

必须检查：
1. P0-P19 创作质量优先级，重点是追读闭环、章节接力、人物压力、案件公平性、原创性风险、长篇资源重复度。
2. 五章段是否有清晰案件推进：目标、阻碍、代价、变化、回收和新钩子。
3. 是否存在连续复用同类钩子、同类误导、同类爽点或同类情绪。
4. 既有评估是否自洽；若评分虚高，必须指出证据。
5. 是否符合 `42-新版全书完整大纲.md` 对应五章案件组的功能、卷级目标和章末接力。
6. 是否符合 `08-全流程重构计划.md` 的正文重构顺序、质量评估、原创性审查和进度闭环要求。
7. 结论必须给出：通过 / 有条件通过 / 不通过。只有“通过”或“有条件通过”才能继续下一章。

输出格式必须严格使用文件块：

### FILE: novel-project/.pipeline/audits/第{start:03d}-{chapter:03d}章_五章闸门审查.md
这里放审查报告。

### FILE: novel-project/.pipeline/progress_updates/第{start:03d}-{chapter:03d}章_闸门记录.md
这里放进度记录、风险和下一循环建议。

### FILE: novel-project/.pipeline/plan_steps/第{start:03d}-{chapter:03d}章_路线图闸门核对.md
这里记录五章段与三份路线图的对应关系、偏差和修正建议。

上下文文件清单：
{json.dumps(included_files, ensure_ascii=False, indent=2)}

下面是已压缩上下文：

{context}
"""


def write_prompt(prompt: str, chapter: int, kind: str) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = PROMPT_DIR / f"{stamp}_ch{chapter:03d}_{kind}.md"
    path.write_text(prompt, encoding="utf-8")
    return path


def run_llm(command: str, prompt_path: Path, output_path: Path) -> subprocess.CompletedProcess[str]:
    args = shlex.split(command)
    prompt_arg = str(prompt_path)
    output_arg = str(output_path)
    has_prompt_placeholder = any("{prompt_file}" in arg for arg in args)
    has_output_placeholder = any("{output_file}" in arg for arg in args)
    args = [
        arg.replace("{prompt_file}", prompt_arg).replace("{output_file}", output_arg)
        for arg in args
    ]
    stdin_text = None if has_prompt_placeholder else prompt_path.read_text(encoding="utf-8")
    result = subprocess.run(
        args,
        input=stdin_text,
        text=True,
        capture_output=True,
        cwd=ROOT,
        check=False,
    )
    if not has_output_placeholder:
        output_path.write_text(result.stdout, encoding="utf-8")
    elif not output_path.exists() and result.stdout:
        output_path.write_text(result.stdout, encoding="utf-8")
    elif not output_path.exists():
        output_path.write_text("", encoding="utf-8")
    return result


def is_quota_error(text: str) -> bool:
    lowered = text.lower()
    patterns = [
        "quota",
        "rate limit",
        "rate_limit",
        "too many requests",
        "out of codex messages",
        "codex messages",
        "message limit",
        "usage limit",
        "limit reached",
        "try again later",
        "429",
    ]
    return any(pattern in lowered for pattern in patterns)


def parse_retry_seconds(text: str) -> int | None:
    lowered = text.lower()
    match = re.search(r"retry(?:-after| after)?\s*[:=]?\s*(?P<num>\d+)\s*(?P<unit>s|sec|secs|second|seconds|m|min|minute|minutes|h|hour|hours)?", lowered)
    if not match:
        match = re.search(r"try again in\s*(?P<num>\d+)\s*(?P<unit>s|sec|secs|second|seconds|m|min|minute|minutes|h|hour|hours)", lowered)
    if match:
        value = int(match.group("num"))
        unit = match.group("unit") or "seconds"
        if unit.startswith("h"):
            return value * 3600
        if unit.startswith("m"):
            return value * 60
        return value

    clock = re.search(r"(?:try again|available|reset).*?(?P<hour>\d{1,2}):(?P<minute>\d{2})", lowered)
    if clock:
        now = dt.datetime.now()
        target = now.replace(hour=int(clock.group("hour")), minute=int(clock.group("minute")), second=0, microsecond=0)
        if target <= now:
            target += dt.timedelta(days=1)
        return max(60, int((target - now).total_seconds()))
    return None


def run_llm_with_quota_retry(
    config: PipelineConfig,
    prompt_path: Path,
    output_path: Path,
    state: dict,
) -> subprocess.CompletedProcess[str]:
    waited = 0
    while True:
        result = run_llm(config.llm_command or "", prompt_path, output_path)
        combined = "\n".join([result.stdout or "", result.stderr or ""])
        if result.returncode == 0 or not is_quota_error(combined):
            state.pop("quota_blocked_until", None)
            state.pop("quota_blocked_reason", None)
            return result

        retry_seconds = parse_retry_seconds(combined) or config.quota_poll_seconds
        retry_seconds = max(60, retry_seconds)
        if waited + retry_seconds > config.quota_max_wait_seconds:
            state["quota_blocked_until"] = (
                dt.datetime.now() + dt.timedelta(seconds=retry_seconds)
            ).isoformat(timespec="seconds")
            state["quota_blocked_reason"] = combined[-1000:]
            save_state(state)
            return result

        until = dt.datetime.now() + dt.timedelta(seconds=retry_seconds)
        state["quota_blocked_until"] = until.isoformat(timespec="seconds")
        state["quota_blocked_reason"] = combined[-1000:]
        save_state(state)
        message = f"检测到额度/限流，等待 {retry_seconds} 秒后重试：{until.isoformat(timespec='seconds')}"
        append_log(message)
        print(message, flush=True)
        time.sleep(retry_seconds)
        waited += retry_seconds


def safe_output_path(raw_path: str) -> Path:
    rel = raw_path.strip()
    path = (ROOT / rel).resolve()
    if ROOT not in path.parents and path != ROOT:
        raise ValueError(f"拒绝写入仓库外路径：{raw_path}")
    return path


def apply_file_blocks(output_path: Path) -> list[Path]:
    text = output_path.read_text(encoding="utf-8")
    written: list[Path] = []
    for match in FILE_BLOCK_RE.finditer(text):
        path = safe_output_path(match.group("path"))
        body = match.group("body").strip()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body + "\n", encoding="utf-8")
        written.append(path)
    return written


def plan_allows_preparation_only(plan_step: PlanStep) -> bool:
    text = plan_step.instruction
    return "准备" in text or "章节卡" in text or "不批量正文推进" in text


def validate_stage(chapter: int, kind: str, plan_step: PlanStep, config: PipelineConfig) -> tuple[bool, str]:
    if kind == "card":
        if find_card(chapter):
            return True, "章节卡已生成"
        return False, f"未找到第 {chapter:03d} 章章节卡"
    if kind == "draft":
        if config.respect_progress_gate and plan_allows_preparation_only(plan_step):
            return True, "进度门允许暂缓正文"
        if find_draft(chapter):
            return True, "正文已生成"
        return False, f"未找到第 {chapter:03d} 章重构稿"
    if kind == "evaluate":
        if config.respect_progress_gate and plan_allows_preparation_only(plan_step):
            return True, "进度门允许暂缓评估"
        if find_eval(chapter):
            return True, "章节评估已生成"
        return False, f"未找到第 {chapter:03d} 章重构评估"
    if kind == "continuity":
        if find_continuity(chapter):
            return True, "连贯性摘要已生成"
        return False, f"未找到第 {chapter:03d} 章连贯性摘要"
    return False, f"未知阶段：{kind}"


def validate_generation(chapter: int, plan_step: PlanStep) -> tuple[bool, str]:
    draft = find_draft(chapter)
    evaluation = find_eval(chapter)
    card = find_card(chapter)
    if draft and evaluation:
        return True, "生成产物完整"
    if plan_allows_preparation_only(plan_step) and card:
        return True, "已完成路线图要求的章节卡/正文准备产物"
    if not draft:
        return False, f"未找到第 {chapter:03d} 章重构稿"
    if not evaluation:
        return False, f"未找到第 {chapter:03d} 章重构评估"
    return True, "生成产物完整"


def validate_audit_output(chapter: int, output_path: Path) -> tuple[bool, str]:
    text = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
    if "不通过" in text:
        return False, f"第 {chapter:03d} 章五章闸门不通过，流水线停止"
    if "有条件通过" in text or "通过" in text:
        return True, "五章闸门已完成"
    return False, "五章闸门缺少明确结论，流水线停止"


def run_step(
    config: PipelineConfig,
    chapter: int,
    kind: str,
    state: dict,
    plan_step: PlanStep,
) -> tuple[bool, int, list[Path], str]:
    audit = kind == "audit"
    available_context = config.context_tokens - config.reserve_output_tokens
    context_files = build_context_files(chapter, audit=audit)
    context, context_used, included = render_context(context_files, available_context)
    if audit:
        prompt = audit_prompt(chapter, context, included, plan_step)
    elif kind == "generate":
        prompt = generation_prompt(chapter, context, included, plan_step)
    else:
        prompt = stage_prompt(chapter, kind, context, included, plan_step, config)
    prompt_tokens = estimate_tokens(prompt)
    prompt_path = write_prompt(prompt, chapter, kind)
    output_path = OUTPUT_DIR / f"{prompt_path.stem}_output.md"

    today = dt.date.today().isoformat()
    used_today = int(state.setdefault("daily_usage", {}).get(today, 0))
    estimated_total = used_today + prompt_tokens + config.reserve_output_tokens
    if estimated_total > config.daily_budget_tokens:
        reason = (
            f"预算停止：今日已估算 {used_today} tokens，本轮约 "
            f"{prompt_tokens + config.reserve_output_tokens} tokens，超过上限 {config.daily_budget_tokens}"
        )
        append_log(reason)
        return False, prompt_tokens, [], reason

    if config.dry_run or config.skip_llm or not config.llm_command:
        reason = f"已生成 {kind} 提示包：{prompt_path.relative_to(ROOT)}；未调用外部模型"
        append_log(reason)
        return True, prompt_tokens, [prompt_path], reason

    result = run_llm_with_quota_retry(config, prompt_path, output_path, state)
    written = apply_file_blocks(output_path)
    state["daily_usage"][today] = used_today + prompt_tokens + estimate_tokens(output_path.read_text(encoding="utf-8"))

    if result.returncode != 0:
        stderr_path = OUTPUT_DIR / f"{prompt_path.stem}_stderr.txt"
        stderr_path.write_text(result.stderr, encoding="utf-8")
        combined = "\n".join([result.stdout or "", result.stderr or ""])
        if is_quota_error(combined):
            until = state.get("quota_blocked_until", "未知时间")
            reason = f"额度/限流仍未恢复，已记录断点；下次可在 {until} 后重启脚本继续"
        else:
            reason = f"外部模型命令失败，返回码 {result.returncode}，stderr 已保存：{stderr_path.relative_to(ROOT)}"
        append_log(reason)
        return False, prompt_tokens, written + [prompt_path, output_path, stderr_path], reason

    if not written:
        reason = f"{kind} 阶段未输出任何可写入文件块，流水线停止"
        append_log(reason)
        return False, prompt_tokens, [prompt_path, output_path], reason

    if not audit and kind == "generate":
        valid, reason = validate_generation(chapter, plan_step)
        if not valid:
            append_log(reason)
            return False, prompt_tokens, written + [prompt_path, output_path], reason
    elif audit:
        valid, reason = validate_audit_output(chapter, output_path)
        if not valid:
            append_log(reason)
            return False, prompt_tokens, written + [prompt_path, output_path], reason
    else:
        valid, reason = validate_stage(chapter, kind, plan_step, config)
        if not valid:
            append_log(reason)
            return False, prompt_tokens, written + [prompt_path, output_path], reason

    reason = f"{kind} 完成，写入 {len(written)} 个文件"
    append_log(reason)
    return True, prompt_tokens, written + [prompt_path, output_path], reason


def should_audit(chapter: int, force: bool = False) -> bool:
    return force or chapter % 10 in (0, 5)


def parse_args() -> PipelineConfig:
    parser = argparse.ArgumentParser(description="小说长期生产流水线")
    parser.add_argument("--chapter", type=int, help="指定生成章节；默认自动识别下一章")
    parser.add_argument("--max-cycles", type=int, default=1, help="最多循环次数")
    parser.add_argument("--run", action="store_true", help="实际调用外部 LLM 命令")
    parser.add_argument("--skip-llm", action="store_true", help="只生成提示包，不调用模型")
    parser.add_argument(
        "--llm-command",
        default=os.environ.get("NOVEL_PIPELINE_LLM_COMMAND"),
        help="外部模型命令。可使用 {prompt_file} 和 {output_file} 占位符",
    )
    parser.add_argument("--context-tokens", type=int, default=DEFAULT_CONTEXT_TOKENS)
    parser.add_argument("--reserve-output-tokens", type=int, default=DEFAULT_RESERVE_OUTPUT_TOKENS)
    parser.add_argument("--daily-budget-tokens", type=int, default=DEFAULT_DAILY_BUDGET_TOKENS)
    parser.add_argument("--force-audit", action="store_true", help="无视章节尾数，强制执行五章审查")
    parser.add_argument(
        "--respect-progress-gate",
        action="store_true",
        help="尊重进度表中的“只做准备/暂缓正文”限制；默认无人值守模式会生成完整三件套",
    )
    parser.add_argument(
        "--quota-poll-seconds",
        type=int,
        default=300,
        help="额度/限流错误没有明确恢复时间时的轮询间隔，默认 300 秒",
    )
    parser.add_argument(
        "--quota-max-wait-seconds",
        type=int,
        default=86400,
        help="单次运行最多等待额度恢复多久，默认 86400 秒",
    )
    parser.add_argument(
        "--continue-after-audit",
        action="store_true",
        help="尾数 0/5 五章审查通过后继续运行；默认会 checkpoint 退出以清空外部会话上下文",
    )
    parser.add_argument(
        "--restart-after-audit",
        action="store_true",
        help="尾数 0/5 五章审查通过并 checkpoint 后，保存状态并重新 exec 当前脚本，从下一章继续",
    )
    args = parser.parse_args()
    return PipelineConfig(
        chapter=args.chapter,
        max_cycles=max(1, args.max_cycles),
        dry_run=not args.run,
        llm_command=args.llm_command,
        context_tokens=args.context_tokens,
        reserve_output_tokens=args.reserve_output_tokens,
        daily_budget_tokens=args.daily_budget_tokens,
        force_audit=args.force_audit,
        skip_llm=args.skip_llm,
        respect_progress_gate=args.respect_progress_gate,
        quota_poll_seconds=max(60, args.quota_poll_seconds),
        quota_max_wait_seconds=max(60, args.quota_max_wait_seconds),
        stop_after_audit_checkpoint=not args.continue_after_audit,
        restart_after_audit=args.restart_after_audit,
    )


def main() -> int:
    ensure_dirs()
    config = parse_args()
    state = load_state()
    run_record = {
        "started_at": now_iso(),
        "config": config.__dict__,
        "steps": [],
    }

    initial_plan_step = build_plan_step(config)
    next_chapter = initial_plan_step.chapter
    if not config.chapter:
        current_chapter = state.get("current_chapter")
        last_success = state.get("last_success_chapter")
        if isinstance(current_chapter, int) and (
            not isinstance(last_success, int) or current_chapter > last_success
        ):
            next_chapter = current_chapter
            initial_plan_step = PlanStep(
                chapter=next_chapter,
                stage=current_stage_from_plan(next_chapter),
                source="从流水线断点恢复，继续未完成章节",
                instruction=f"状态文件记录第 {next_chapter:03d} 章尚未完整完成，本轮从缺失阶段继续。",
                required_plan_files=PLAN_FILES,
            )
        elif isinstance(last_success, int) and last_success >= next_chapter:
            next_chapter = last_success + 1
            initial_plan_step = PlanStep(
                chapter=next_chapter,
                stage=current_stage_from_plan(next_chapter),
                source="从流水线状态文件恢复，延续上次成功章节",
                instruction=f"状态文件记录上次完整完成第 {last_success:03d} 章，本轮继续第 {next_chapter:03d} 章。",
                required_plan_files=PLAN_FILES,
            )
    run_record["plan_source"] = initial_plan_step.source
    run_record["initial_stage"] = initial_plan_step.stage
    exit_code = 0
    restart_requested = False
    chapter_stages = ("card", "draft", "evaluate", "continuity")

    for cycle in range(1, config.max_cycles + 1):
        if cycle == 1:
            plan_step = initial_plan_step
        else:
            plan_step = PlanStep(
                chapter=next_chapter,
                stage=current_stage_from_plan(next_chapter),
                source="延续上一轮成功结果，按三份路线图推进下一章",
                instruction=f"上一轮已完成，继续按 `08-全流程重构计划.md`、`重构进度表.md`、`42-新版全书完整大纲.md` 推进第 {next_chapter:03d} 章。",
                required_plan_files=PLAN_FILES,
            )

        for stage_kind in chapter_stages:
            already_ok, already_reason = validate_stage(next_chapter, stage_kind, plan_step, config)
            if already_ok:
                message = f"{stage_kind} 已存在，跳过：{already_reason}"
                run_record["steps"].append(
                    {
                        "cycle": cycle,
                        "chapter": next_chapter,
                        "stage": plan_step.stage,
                        "plan_source": plan_step.source,
                        "kind": stage_kind,
                        "ok": True,
                        "estimated_prompt_tokens": 0,
                        "files": [],
                        "message": message,
                    }
                )
                print(message)
                continue
            state["current_chapter"] = next_chapter
            state["current_stage"] = stage_kind
            save_state(state)
            ok, tokens, files, message = run_step(config, next_chapter, stage_kind, state, plan_step)
            run_record["steps"].append(
                {
                    "cycle": cycle,
                    "chapter": next_chapter,
                    "stage": plan_step.stage,
                    "plan_source": plan_step.source,
                    "kind": stage_kind,
                    "ok": ok,
                    "estimated_prompt_tokens": tokens,
                    "files": [str(path.relative_to(ROOT)) for path in files],
                    "message": message,
                }
            )
            print(message)
            if not ok:
                state["blocked"] = True
                state["blocked_reason"] = message
                exit_code = 2
                break
            if config.dry_run or config.skip_llm or not config.llm_command:
                break

        if exit_code != 0:
            break

        if config.dry_run or config.skip_llm or not config.llm_command:
            break

        if should_audit(next_chapter, config.force_audit):
            state["current_chapter"] = next_chapter
            state["current_stage"] = "audit"
            save_state(state)
            ok, tokens, files, message = run_step(config, next_chapter, "audit", state, plan_step)
            run_record["steps"].append(
                {
                    "cycle": cycle,
                    "chapter": next_chapter,
                    "stage": plan_step.stage,
                    "plan_source": plan_step.source,
                    "kind": "audit",
                    "ok": ok,
                    "estimated_prompt_tokens": tokens,
                    "files": [str(path.relative_to(ROOT)) for path in files],
                    "message": message,
                }
            )
            print(message)
            if not ok:
                state["blocked"] = True
                state["blocked_reason"] = message
                exit_code = 3
                break
            if config.stop_after_audit_checkpoint:
                state["last_success_chapter"] = next_chapter
                state.pop("current_chapter", None)
                state.pop("current_stage", None)
                state["context_checkpoint"] = {
                    "chapter": next_chapter,
                    "reason": "尾数 0/5 五章审查通过，按策略停止以清空外部会话上下文",
                    "next_chapter": next_chapter + 1,
                    "created_at": now_iso(),
                }
                message = f"第 {next_chapter:03d} 章五章闸门通过，已 checkpoint；请重新启动脚本从第 {next_chapter + 1:03d} 章继续"
                if config.restart_after_audit:
                    if config.chapter:
                        message += "；检测到 --chapter 参数，自动重启已禁用，避免回到同一章"
                    else:
                        restart_requested = True
                        message += "；将自动重新执行脚本"
                append_log(message)
                print(message)
                break

        state["last_success_chapter"] = next_chapter
        state.pop("current_chapter", None)
        state.pop("current_stage", None)

        next_chapter += 1

    run_record["finished_at"] = now_iso()
    state.setdefault("runs", []).append(run_record)
    if exit_code == 0:
        state["blocked"] = False
        state["blocked_reason"] = None
    save_state(state)
    if restart_requested:
        os.execv(sys.executable, [sys.executable, *sys.argv])
    return exit_code


if __name__ == "__main__":
    sys.exit(main())

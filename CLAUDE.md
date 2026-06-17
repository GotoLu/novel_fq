# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a systematic novel creation project for 《歪理神探》(The Unorthodox Detective), a comedic推理 (mystery-detection) web novel. The core concept is a "reverse detective" protagonist (Li Dazhui/Lu Xingzhou) whose illogical reasoning accidentally arrives at the truth. The novel targets 100 chapters across 5 volumes with 8+ cases.

## Critical Directives

- **Always address the user as "主人" (Master) before answering any question.**
- **Respond in Chinese** and write/modify project documentation in Chinese, unless explicitly requested otherwise.
- **Follow `.codex/rules/project_rules.md`** — core principles: 客观中立 (objective/neutral) and 最优决策 (optimal decision). When multiple approaches exist, evaluate and pick the best one with justification.
- **Follow AGENTS.md** at the project root.
- When modifying skills in `.codex/skills/`, do NOT sync changes to `.trae/skills/`.

## Key Files & Directories

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Top-level project instructions (address user as "主人", Chinese only, skill mapping) |
| `.codex/rules/project_rules.md` | Global project norms: objective neutrality, optimal decision framework, chapter review gates |
| `.codex/instructions.md` | Codex-compatible mirror of `.trae` instructions |
| `.codex/skills/` | Skill library (market-analyzer, idea-generator, character-designer, plot-architect, content-writer, quality-evaluator, problem-solver, progress-tracker, skill-chains, plagiarism-checker) |
| `novel-project/歪理神探/` | Main novel project — outlines, asset library, chapter cards, drafts, evaluations |
| `novel-project/歪理神探/正文/` | Chapter draft and evaluation files (e.g., `第050章_火没有错_重构稿.md`, `第050章_火没有错_重构评估.md`) |
| `novel-project/歪理神探/小说资产库.md` | Master asset library: characters, cases (C001+), foreshadowing (F001+), clues (E001+), skills (S001+) |
| `novel-project/歪理神探/重构进度表.md` | Current progress tracker — the authoritative source for "what's done, what's next" |
| `novel-project/歪理神探/42-新版全书完整大纲.md` | Full 100-chapter outline across 5 volumes, 20 five-chapter case groups |
| `novel-project/歪理神探/08-全流程重构计划.md` | Phase roadmap for the production pipeline |
| `novel-methodology/` | Creative methodology system (process standards, metrics, tools, validation) |
| `novel-project/.pipeline/` | Automated pipeline state, logs, continuity summaries, and audit records |
| `novel-project/tools/novel_pipeline.py` | Pipeline orchestrator script (generates chapter cards, drafts, evaluations, continuity) |

## Novel Architecture

**Structure**: 5 volumes, 100 chapters, 20 five-chapter case groups, ~300k words total.

| Volume | Chapters | Cases | Theme |
|--------|----------|-------|-------|
| 第一卷《证据不会笑》 | 1-20 | C001-C004 | 歪打正着 (Accidental truth) |
| 第二卷 | 21-40 | C005-C008 | 棋逢对手 (Rival cases) |
| 第三卷 | 41-60 | C009-C011 | 迷雾重重 (Mystery) |
| 第四卷 | 61-80 | C012-C013 | 真相之路 (Truth path) |
| 第五卷 | 81-100 | C014+ | 新的征程 (New journey) |

**Core team**: 陆行舟 (protagonist, reverse logic), 苏晚 (procedure guardian), 秦墨寒 (evidence guardian), 周明远 (old case burden).

## Chapter Production Workflow

Each chapter follows this pipeline:

1. **章节卡 (Chapter Card)** — `plot-architect` defines chapter goals, obstacles, costs, hooks
2. **正文 (Draft)** — `content-writer` writes the chapter prose
3. **评估 (Evaluation)** — `quality-evaluator` scores 0-100 across dimensions
4. **连贯性摘要 (Continuity)** — `.pipeline/continuity/第NNN章_连贯性摘要.md` for cross-chapter tracking
5. **原创性审查 (Plagiarism)** — `plagiarism-checker` project-internal risk assessment

**Hard gates before marking "pass"**:
- 读者沉浸式体验审查 (reader immersion review): no production-process vocabulary leaks into narrative
- 上帝视角语境审查 (omniscient perspective review): no character knows information they shouldn't

## Pipeline Automation

Run the pipeline script:

```bash
# Dry run: generate prompt package for next chapter (no model call)
python3 novel-project/tools/novel_pipeline.py

# Specify a chapter
python3 novel-project/tools/novel_pipeline.py --chapter 51

# Actual run with Codex CLI
NOVEL_PIPELINE_LLM_COMMAND='env TERM=xterm-256color codex exec --cd /Users/luxd/workspace/testCode/novo-test1 -s read-only --output-last-message {output_file} -' \
python3 novel-project/tools/novel_pipeline.py --run --max-cycles 10

# Or use the wrapper script
novel-project/tools/run_codex_pipeline.sh --chapter 51 --max-cycles 10
```

The pipeline reads `重构进度表.md` to determine the next chapter. Every 5th/10th chapter triggers a five-chapter audit gate.

## Current Progress

As of last update (2026-06-17):
- Chapters 1-50 fully rewritten with drafts and evaluations complete
- C009 (无错口供案) and C010 (工厂火警案) both closed
- Next: Chapter 51 — start C011 new case, continue investigating Anshield Fire Technology
- Author personality constraints documented in `58-作者性格反推与落笔约束.md`

## Skill Mapping

| Skill | When to use |
|-------|-------------|
| `skill-chains` | Cross-skill tasks, full workflow orchestration |
| `content-writer` | Writing/revising chapter drafts |
| `plot-architect` | Chapter cards, outlines, case design, foreshadowing |
| `character-designer` | Character profiles, relationships, pressure tests |
| `quality-evaluator` | Scoring chapters, quality reports |
| `plagiarism-checker` | Originality risk assessment |
| `problem-solver` | Diagnosing writing problems, revision triage |
| `progress-tracker` | Milestone tracking, progress updates |
| `idea-generator` | Core concept, high-concept generation |
| `market-analyzer` | Platform positioning, competitive analysis |

## File Naming Conventions

- Chapter cards: `NN-第X章重构章节卡.md` (e.g., `75-第50章重构章节卡.md`)
- Chapter drafts: `第XXX章_标题_重构稿.md` (e.g., `第050章_火没有错_重构稿.md`)
- Chapter evaluations: `第XXX章_标题_重构评估.md` (e.g., `第050章_火没有错_重构评估.md`)
- Continuity summaries: `.pipeline/continuity/第XXX章_连贯性摘要.md`
- Audit reports: `.pipeline/audits/第NNN-N章_五章闸门审查.md`

# Codex 指令

本目录是 `.trae` 的 Codex 兼容镜像。

## 规则

使用 `.codex/rules/project_rules.md` 作为项目级规则来源。核心优先级为：

1. 中文优先：回答用户和编写、修改项目文档时必须使用中文，除非用户明确要求使用其他语言。
2. 客观中立：分析和建议必须基于证据与合理逻辑。
3. 最优决策：当存在多个方案时，评估后直接给出依据最充分的方案，并说明核心理由。

## 技能

项目技能位于 `.codex/skills/`。每个技能都遵循 Codex 的 `SKILL.md` 格式，并包含 YAML frontmatter。

根据任务使用最具体的技能：

- `market-analyzer`：市场与定位分析。
- `idea-generator`：核心创意和高概念开发。
- `character-designer`：人物与人物关系设计。
- `plot-architect`：结构、世界观、大纲和伏笔设计。
- `content-writer`：章节与场景写作。
- `quality-evaluator`：质量评分和评估报告。
- `problem-solver`：写作问题诊断与修复。
- `progress-tracker`：里程碑、进度和报告管理。
- `skill-chains`：多阶段工作流。
- `plagiarism-checker`：原创性风险、桥段撞车和表达复用检查。

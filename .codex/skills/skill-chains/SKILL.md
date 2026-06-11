---
name: "skill-chains"
description: "将全部小说写作技能组织为阶段化工作流。用于规划或执行从市场分析、创意生成、人物设计、情节架构、正文写作、质量评估、问题修复、原创性风险审查、进度追踪到发布完结的完整创作流程。"
---

# 技能链

当任务跨越多个写作技能，或需要端到端创作流程时，使用本技能。本技能必须整合 `.codex/skills/` 下全部相关技能，而不是只执行 P0-P19 质量条目。

## 工作流程

1. 识别项目阶段和用户需要的具体交付物。
2. 优先读取 `../创作质量优先级.md`，执行其中 P0-P19 质量优先级。
3. 读取 `README.md` 确认全技能角色、阶段执行链、数据流、阶段切换条件和失败回退。
4. 读取 `application-guide.md`，按用户意图选择主技能、协同技能和验收技能。
5. 只读取本目录下与当前阶段相关的参考文件，避免无关扩散。
6. 执行推荐技能链，并显式说明本次调用哪些技能、每个技能负责什么产出。
7. 每个阶段结束必须调用 `quality-evaluator` 做质量闸门检查。
8. 涉及创意、设定、场景、正文、对话、简介和发布材料时，必须调用 `plagiarism-checker` 做原创性检查。
9. 未通过质量或原创性闸门时，调用 `problem-solver` 做改稿分诊，并回退到对应生产技能重做。
10. 所有阶段状态、审计结果、原创性风险结论和调整依据必须交给 `progress-tracker` 记录。
11. 保持 `.codex/rules/project_rules.md` 中的项目原则：先客观分析，再给出依据最充分的决策。

## 默认技能分工

- 立项和发布：`market-analyzer`
- 创意和高概念：`idea-generator`
- 人物和群像：`character-designer`
- 结构、大纲、世界观和长篇资产：`plot-architect`
- 正文、改写和高潮：`content-writer`
- 质量验收：`quality-evaluator`
- 问题分诊和修复：`problem-solver`
- 进度、节点和反馈闭环：`progress-tracker`
- 原创性风险和桥段撞车：`plagiarism-checker`

## 参考文件

- `README.md`：全技能链系统总览。
- `application-guide.md`：全技能应用指南。
- `combination-strategy.md`：全技能组合策略。
- `architecture-diagram.md`：系统架构。
- `evaluation-system.md`：全技能评估与验收方式。
- `../创作质量优先级.md`：读者钩子、单章闭环、情节发动机、人物压力、创意独特性、场景调度、章节接力、情绪投注、爽点链、作者风格、长篇资源账本、类型专门引擎、读者反馈闭环、群像轮转、卷级防塌、改稿分诊、小说资产库、平台发布适配、最终审美统一、完结与续作设计和评分体系的最高优先级修复。
- `phase-1-market-idea.md`：市场分析和创意生成。
- `phase-2-character.md`：人物设计。
- `phase-3-plot.md`：情节架构。
- `phase-3-author-persona.md`：作者性格定标；开始写正文前必须执行，已有项目可从代表章节反推。
- `phase-4-content.md`：正文写作。
- `phase-5-integration.md`：最终整合和优化。

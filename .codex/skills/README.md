# 小说创作技能系统使用说明

本目录是 Codex 在本项目中使用的小说创作技能库。它不是零散提示词合集，而是一套从立项、创意、人物、情节、正文、质检、改稿、查重、进度管理到发布完结的完整生产系统。

使用任何技能前，先遵循 [创作质量优先级](./创作质量优先级.md)。如果流程完整和小说好看发生冲突，永远优先读者钩子、单章追读、人物压力、情节推进、原创性、情绪投入和长篇稳定性。

## 一、技能总览

| 技能 | 核心职责 | 主要产出 | 何时使用 |
|------|----------|----------|----------|
| `skill-chains` | 全技能总控和阶段编排 | 执行链、阶段计划、回退路径 | 任务跨多个技能、需要完整流程或不知道先用哪个技能 |
| `market-analyzer` | 市场、平台、题材、竞品和发布适配 | 平台定位、题材机会、竞品拆解、发布适配表 | 新项目立项、换平台、准备发布 |
| `idea-generator` | 创意生成、筛选、验证和高概念提炼 | 创意池、高概念、不可替代性评分 | 想故事核心、卖点、设定差异化 |
| `character-designer` | 主角、反派、配角、关系和群像轮转 | 人物档案、压力测试、关系网络、群像轮转表 | 设计人物或修复人物扁平、动机虚弱 |
| `plot-architect` | 结构、世界观、大纲、伏笔和长篇资产 | 分卷/分章大纲、资源账本、资产库、完结设计 | 搭建故事骨架、章节卡、长期连载规划 |
| `content-writer` | 正文写作、开篇、章节、高潮和风格控制 | 章节正文、节奏分析、章末钩子 | 写正文、改写章节、强化高潮 |
| `quality-evaluator` | 质量评估和硬性淘汰检查 | 评分报告、问题清单、版本对比 | 验收任何创作成果 |
| `problem-solver` | 问题诊断、改稿分诊和修复方案 | 诊断结果、改稿方案、保护项 | 卡文、崩线、追读差、人物失真 |
| `progress-tracker` | 项目进度、节点、周期审计和反馈闭环 | 进度记录、审计报告、调整依据 | 长篇连载管理、阶段复盘 |
| `plagiarism-checker` | 原创性、相似度和风险检查 | 查重报告、风险等级、改写建议 | 创意、设定、场景、正文和对话验收 |

## 二、总入口选择

优先从 `skill-chains` 进入以下任务：

- 从零启动一本小说。
- 同时涉及市场、创意、人物、情节、正文或改稿中的两个以上环节。
- 用户只说“帮我优化小说”“看看哪里有问题”“做完整方案”。
- 已有章节需要诊断、重写、查重、记录进度和规划后续。

只调用单项技能的情况：

- 用户明确只要某一类产出，例如“设计主角”“写第一章”“分析番茄平台”。
- 当前任务非常窄，并且前置资料已经完整。
- 单技能结束后仍要用 `quality-evaluator` 或 `plagiarism-checker` 做验收，不能裸交付。

## 三、全技能标准链路

### 1. 立项链

`progress-tracker` 初始化项目 → `market-analyzer` 做平台、题材、竞品和发布适配 → `idea-generator` 生成并验证高概念 → `plagiarism-checker` 检查核心设定原创性 → `quality-evaluator` 验收创意质量。

最低交付：

- 目标平台和目标读者。
- 类型定位和竞品风险。
- 一句话高概念。
- 不可替代性测试。
- 原创性风险结论。

### 2. 设计链

`character-designer` 建人物体系 → `plot-architect` 建结构、大纲、世界观和长篇资产 → `quality-evaluator` 验收人物压力、情节推进、资源账本和卷级稳定性 → `progress-tracker` 记录节点。

最低交付：

- 主角、反派、核心配角档案。
- 人物压力测试和群像轮转表。
- 分卷/分章大纲。
- 场景调度卡、章节接力卡、爽点链卡。
- 长篇资源账本、小说资产库、完结设计表。

### 3. 正文链

`plot-architect` 提供章节卡 → `character-designer` 确认人物状态 → `content-writer` 写正文 → `quality-evaluator` 查钩子、推进、情绪、爽点和风格 → `plagiarism-checker` 查重 → `progress-tracker` 记录。

最低交付：

- 章节目标、阻碍、代价、变化和章末钩子。
- 正文成稿。
- 质量检查结果。
- 原创性结论。
- 下一章接力点。

### 4. 改稿链

`quality-evaluator` 定位问题 → `problem-solver` 按结构、人物动机、追读、场景、语言顺序分诊 → 对应生产技能重做 → `plagiarism-checker` 查重 → `progress-tracker` 记录版本变化。

最低交付：

- 问题优先级。
- 保留、删除、增强、禁止破坏项。
- 修订稿或修订方案。
- 修订前后变化说明。

### 5. 连载链

每 5-10 章由 `progress-tracker` 触发周期审计，调用 `quality-evaluator`、`problem-solver`、`plot-architect`、`character-designer`、`market-analyzer` 和 `plagiarism-checker` 检查反馈、资源、群像、平台适配和原创风险。

最低交付：

- 读者反馈复盘。
- 长篇资源账本更新。
- 人物轮转和情绪债状态。
- 下一周期风险和调整动作。

### 6. 发布与完结链

`market-analyzer` 做发布适配 → `quality-evaluator` 做终审 → `plot-architect` 检查伏笔、主线偿付和续作空间 → `problem-solver` 清理残留问题 → `progress-tracker` 归档。

最低交付：

- 书名、简介、标签、前三章卖点。
- 最终审美统一报告。
- 伏笔回收和留白清单。
- 人物归宿、主题落点、续作空间。

## 四、调用矩阵

| 任务 | 主技能 | 必须协同 | 验收技能 |
|------|--------|----------|----------|
| 新书立项 | `skill-chains` | `market-analyzer`、`idea-generator`、`progress-tracker` | `quality-evaluator`、`plagiarism-checker` |
| 创意升级 | `idea-generator` | `market-analyzer` | `quality-evaluator`、`plagiarism-checker` |
| 人物设计 | `character-designer` | `idea-generator`、`plot-architect` | `quality-evaluator` |
| 大纲设计 | `plot-architect` | `character-designer`、`idea-generator` | `quality-evaluator`、`plagiarism-checker` |
| 写开篇 | `content-writer` | `plot-architect`、`character-designer` | `quality-evaluator`、`plagiarism-checker` |
| 写日常章 | `content-writer` | `plot-architect`、`progress-tracker` | `quality-evaluator` |
| 修卡文 | `problem-solver` | `plot-architect`、`character-designer` | `quality-evaluator` |
| 修追读 | `problem-solver` | `content-writer`、`plot-architect` | `quality-evaluator` |
| 查原创 | `plagiarism-checker` | 对应生产技能 | `quality-evaluator` |
| 连载复盘 | `progress-tracker` | 全技能按问题调用 | `quality-evaluator` |
| 发布准备 | `market-analyzer` | `content-writer`、`plot-architect` | `quality-evaluator` |
| 完稿终审 | `skill-chains` | 全技能 | `quality-evaluator`、`plagiarism-checker` |

## 五、质量闸门

所有成果必须通过三类闸门：

1. 创作质量闸门：执行 [创作质量优先级](./创作质量优先级.md) 中与当前任务相关的项目。
2. 系统协同闸门：前置资料完整、跨技能数据一致、下一步可执行。
3. 原创风险闸门：核心创意、设定、场景、正文和对话没有明显相似风险。

未通过时按以下顺序回退：

1. `quality-evaluator` 定位失败项。
2. `problem-solver` 分诊改稿优先级。
3. 回到 `idea-generator`、`character-designer`、`plot-architect` 或 `content-writer` 重做。
4. `plagiarism-checker` 复查原创性。
5. `progress-tracker` 记录问题、版本和决策依据。

## 六、最小使用闭环

即使只写一章，也不能只调用 `content-writer`。最小闭环是：

`plot-architect` 章节卡 → `character-designer` 人物状态 → `content-writer` 正文 → `quality-evaluator` 质量检查 → `problem-solver` 必要修订 → `plagiarism-checker` 原创性检查 → `progress-tracker` 记录。

## 七、文档关系

- `skill-chains/`：全技能链路总控和阶段化使用说明。
- `创作质量优先级.md`：所有技能的最高质量规则。
- 各技能目录下的 `SKILL.md`：单项技能的具体执行规范。
- `plagiarism-checker/`：查重算法、阈值、配置和实现说明。

## 八、使用原则

- 先判断阶段，再选技能。
- 先解决结构、人物和追读，再处理语言润色。
- 先让章节有目标、阻碍、代价和变化，再追求句子漂亮。
- 先确认原创性和差异化，再扩大正文产量。
- 所有重要判断都要留下依据，方便后续连载复盘。

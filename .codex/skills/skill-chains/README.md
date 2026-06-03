# 技能链总控方案

本目录负责把 `.codex/skills/` 下全部小说创作技能编排成可执行工作流。它的职责不是重复单项技能，而是决定何时调用哪个技能、怎样传递产出、如何验收、失败后回退到哪里。

任何链路都必须先读取 `../创作质量优先级.md`，再按本文件选择阶段链路。

## 一、全技能角色

| 技能 | 在技能链中的位置 | 不可缺席的原因 |
|------|------------------|----------------|
| `skill-chains` | 总控入口 | 判断阶段、编排技能、设置回退 |
| `market-analyzer` | 市场和发布前置 | 没有平台和读者，卖点容易自嗨 |
| `idea-generator` | 创意发动机 | 没有不可替代性，故事只是换皮模板 |
| `character-designer` | 人物压力源 | 人物不受压，情节就没有真实反应 |
| `plot-architect` | 长篇骨架和资产中心 | 没有资源账本，大纲越写越塌 |
| `content-writer` | 正文生产 | 所有设计必须落成可读章节 |
| `quality-evaluator` | 质量闸门 | 防止文档很完整、小说不好看 |
| `problem-solver` | 回退和改稿分诊 | 防止发现问题后只会笼统润色 |
| `progress-tracker` | 长篇记忆和节点管理 | 防止连载越长越失控 |
| `plagiarism-checker` | 原创性闸门 | 防止创意、设定、桥段和正文相似风险 |

## 二、五阶段总链路

| 阶段 | 核心目标 | 主执行链 | 必过闸门 | 交付物 |
|------|----------|----------|----------|--------|
| 阶段一：市场与创意 | 找到平台、读者、题材机会和不可替代高概念 | `progress-tracker` → `market-analyzer` → `idea-generator` → `plagiarism-checker` → `quality-evaluator` | P3、P11、P17、原创性 | 项目记录、平台定位、发布适配、创意验证、高概念 |
| 阶段二：人物与群像 | 建立会被情节逼出反应的人物体系 | `character-designer` → `plot-architect` 局部校验 → `quality-evaluator` → `progress-tracker` | P2、P13 | 人物档案、压力测试、关系网络、群像轮转表 |
| 阶段三：结构与资产 | 建立长篇能跑下去的骨架、资源和结局方向 | `plot-architect` → `character-designer` 反查 → `plagiarism-checker` → `quality-evaluator` → `progress-tracker` | P1、P5、P6、P8、P10、P11、P14、P16、P19 | 大纲、场景调度卡、章节接力卡、爽点链卡、资源账本、资产库、完结设计 |
| 阶段四：正文生产 | 把设计转成有追读、有情绪、有风格的章节 | `plot-architect` 章节卡 → `character-designer` 人物状态 → `content-writer` → `quality-evaluator` → `problem-solver` → `plagiarism-checker` → `progress-tracker` | P0、P5、P6、P7、P8、P9、P15 | 章节正文、质量报告、改稿记录、原创性结论、下一章接力点 |
| 阶段五：连载、发布与完结 | 持续审计并完成发布、终审和收束 | `progress-tracker` → 全技能按问题调用 → `quality-evaluator` → `problem-solver` → `plagiarism-checker` | P4、P12、P14、P15、P17、P18、P19 | 周期审计、反馈复盘、发布材料、终稿审美统一、完结清单 |

## 三、数据流

| 上游产出 | 下游使用 | 必须保留的信息 |
|----------|----------|----------------|
| 平台定位 | 创意、发布、正文风格 | 目标读者、阅读偏好、禁区、节奏要求 |
| 高概念 | 人物、情节、简介 | 核心冲突、第一眼卖点、差异化来源 |
| 人物档案 | 大纲、章节、改稿 | 欲望、恐惧、能力、弱点、关系压力 |
| 大纲和资产库 | 正文、质检、进度 | 主线目标、章节目标、伏笔、资源消耗、爽点回报 |
| 章节正文 | 质检、改稿、查重 | 钩子、变化、情绪债、章末接力点 |
| 质量报告 | 改稿、进度 | 未通过项、严重度、修复建议 |
| 查重报告 | 改稿、终审 | 相似位置、风险等级、需要改写的元素 |
| 进度记录 | 下一周期 | 已完成节点、风险、读者反馈、版本变化 |

## 四、阶段切换条件

| 从 | 到 | 必须满足 |
|----|----|----------|
| 阶段一 | 阶段二 | 高概念通过不可替代性和原创性检查，平台与发布方向明确 |
| 阶段二 | 阶段三 | 主角、反派、核心配角完成压力测试，人物关系能制造持续冲突 |
| 阶段三 | 阶段四 | 分卷/分章大纲、章节卡、资源账本、资产库、完结方向可执行 |
| 阶段四 | 阶段五 | 黄金三章和正文生产闭环通过质量闸门，进度记录字段完整 |
| 阶段五 | 完稿 | 主线偿付、人物归宿、伏笔处理、主题落点、发布材料和原创性终审完成 |

## 五、失败回退

| 失败类型 | 先查 | 回退到 | 禁止操作 |
|----------|------|--------|----------|
| 没有吸引力 | `quality-evaluator` | `idea-generator` 或 `content-writer` | 只改辞藻 |
| 人物不成立 | `character-designer` | 人物压力测试和关系网络 | 用剧情强行推人 |
| 情节塌陷 | `plot-architect` | 大纲、资源账本、章节接力 | 临时加设定糊墙 |
| 正文不追读 | `quality-evaluator` | 章节目标、阻碍、代价、章末钩子 | 只加悬念句 |
| 爽点无效 | `plot-architect` | 爽点链卡和情绪债 | 无铺垫硬给奖励 |
| 风格不统一 | `content-writer` | 作者风格声明和样章 | 每章换口吻 |
| 相似风险 | `plagiarism-checker` | 创意、设定、场景或表达层重构 | 只替换名词 |
| 连载失控 | `progress-tracker` | 周期审计和资源账本 | 继续盲写 |

## 六、最小闭环

任何产出都至少经过：

生产技能 → `quality-evaluator` 验收 → `problem-solver` 必要分诊 → `plagiarism-checker` 原创性检查 → `progress-tracker` 记录。

其中生产技能按任务选择：

- 市场和发布：`market-analyzer`
- 创意和高概念：`idea-generator`
- 人物和群像：`character-designer`
- 大纲和资产：`plot-architect`
- 正文和改写：`content-writer`

## 七、参考文档

- `application-guide.md`：按用户意图选择技能。
- `combination-strategy.md`：全技能组合策略和回退方式。
- `evaluation-system.md`：全技能验收体系。
- `architecture-diagram.md`：技能关系图。
- `phase-1-market-idea.md` 至 `phase-5-integration.md`：阶段细则。

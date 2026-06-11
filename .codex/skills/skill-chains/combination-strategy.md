# 全技能组合策略

本文件说明如何把全部技能组合成不同工作模式。原则只有一个：单项技能负责产出，技能链负责调度，质量、原创性和进度必须闭环。

## 一、基础组合

| 组合 | 适用场景 | 执行方式 | 风险控制 |
|------|----------|----------|----------|
| 顺序组合 | 新项目、资料不完整、需要稳 | 市场 → 创意 → 人物 → 情节 → 作者性格定标 → 正文 → 质检 → 原创性审查 → 进度 | 每阶段过闸门再进入下一阶段 |
| 并行组合 | 已有成熟设定，需要提速 | 市场和竞品可与创意池并行，人物草案可与世界观草案并行 | 由 `quality-evaluator` 检查冲突，由 `progress-tracker` 合并版本 |
| 迭代组合 | 已有稿件需要升级 | 评估 → 分诊 → 重做 → 原创性审查 → 复评 → 记录 | 每轮必须声明改动目标和保护项 |
| 快速闭环 | 只处理一章或一个问题 | 生产技能 → 质检 → 分诊 → 原创性审查 → 记录 | 不跳过质量和原创性闸门 |

## 二、任务组合

### 1. 新书立项组合

执行链：

`progress-tracker` 初始化 → `market-analyzer` 平台/题材/竞品/发布适配 → `idea-generator` 创意池和高概念 → `plagiarism-checker` 原创性检查 → `quality-evaluator` 验收 → `progress-tracker` 记录。

通过标准：

- 高概念一句话能说清。
- 卖点能对准目标平台读者。
- 同类替代测试不过分相似。
- 有明确的发布适配方向。

### 2. 人物体系组合

执行链：

`idea-generator` 提供核心冲突 → `character-designer` 设计主角、反派、配角、关系和群像轮转 → `plot-architect` 反查人物是否能支撑主线 → `quality-evaluator` 验收人物压力 → `progress-tracker` 记录。

通过标准：

- 主角欲望、恐惧、弱点和代价明确。
- 反派能持续制造压力，而不是只负责挡路。
- 配角有功能、有私线、有轮转节奏。
- 人物关系能自动产生冲突和选择。

### 3. 大纲资产组合

执行链：

`plot-architect` 结构、大纲、世界观、伏笔、资源账本、资产库和完结设计 → `character-designer` 检查人物线适配 → `plagiarism-checker` 检查设定和桥段 → `quality-evaluator` 验收 → `progress-tracker` 记录。

通过标准：

- 每章有目标、阻碍、代价、变化和接力点。
- 每卷有主问题、阶段高潮和资源变化。
- 伏笔、情绪债、爽点回报和设定消耗可追踪。
- 结局方向提前存在，不靠临时圆。

### 4. 正文生产组合

执行链：

`plot-architect` 章节卡 → `character-designer` 当前人物状态 → 作者性格声明或已有项目反推结论 → `content-writer` 写正文 → `quality-evaluator` 检查钩子、推进、情绪、爽点、作者性格一致性和风格 → `problem-solver` 必要分诊 → `plagiarism-checker` 原创性风险审查 → `progress-tracker` 记录。

通过标准：

- 开头不迟疑，章节内有明确变化。
- 场景不是背景板，必须参与冲突。
- 爽点有铺垫、有代价、有回响。
- 落笔符合作者性格声明；已有项目必须能说明反推依据。
- 章末留下下一章必须点开的理由。

### 5. 问题修复组合

执行链：

`quality-evaluator` 定位 → `problem-solver` 分诊 → 对应生产技能重做 → `plagiarism-checker` 原创性风险审查 → `quality-evaluator` 复评 → `progress-tracker` 记录。

问题和回退：

| 问题 | 回退技能 |
|------|----------|
| 没有新鲜感 | `idea-generator` |
| 不符合平台 | `market-analyzer` |
| 人物动机弱 | `character-designer` |
| 主线松散 | `plot-architect` |
| 章节不吸引 | `content-writer` |
| 改稿无方向 | `problem-solver` |
| 质量判断混乱 | `quality-evaluator` |
| 原创性风险 | `plagiarism-checker` |
| 长篇记录混乱 | `progress-tracker` |

### 6. 连载复盘组合

执行链：

`progress-tracker` 拉取节点和反馈 → `quality-evaluator` 做周期评估 → `plot-architect` 更新资源账本 → `character-designer` 更新群像轮转 → `market-analyzer` 检查发布适配变化 → `problem-solver` 制定调整 → `plagiarism-checker` 检查新增高风险内容 → `progress-tracker` 归档。

周期建议：

- 每 5-10 章查追读、章末钩子、人物轮转。
- 每 10 章查资源账本、伏笔、情绪债。
- 每 20-30 章查卷级防塌、类型机制、读者反馈。
- 每卷结束查平台适配、主线偿付、下一卷发动机。

## 三、技能调用顺序规则

1. 没有市场定位时，先 `market-analyzer`。
2. 没有高概念时，先 `idea-generator`。
3. 没有人物压力时，不进入长篇大纲。
4. 没有章节卡时，不直接写正文。
5. 没有作者性格声明或已有项目反推结论时，不直接写正文。
6. 没有质量报告时，不做大规模改稿。
7. 没有分诊结论时，不随意重写。
8. 没有原创性风险结论时，不进入发布或定稿。
9. 没有进度记录时，不进入下一周期。

## 四、优先级冲突处理

| 冲突 | 处理 |
|------|------|
| 市场热点和作者表达冲突 | 先保留作者核心表达，再由 `market-analyzer` 调整包装和入口 |
| 创意新奇但不可写长 | 回到 `idea-generator` 和 `plot-architect`，补长期冲突资源 |
| 人物真实但剧情慢 | 由 `plot-architect` 提高外部压力，不牺牲人物动机 |
| 大纲完整但正文无聊 | 由 `content-writer` 重做场景调度、情绪投注和章末接力 |
| 爽点强但逻辑伤 | 回到 `plot-architect` 修因果和代价 |
| 原创性风险可控但风格平 | 回阶段三点五重做作者性格定标，再由 `content-writer` 加强句群设计 |
| 质量评分高但读者反馈差 | 由 `progress-tracker` 触发读者反馈闭环，重新校准指标 |

## 五、输出格式

每次执行技能链，结果至少包含：

- 本次任务阶段。
- 调用技能清单。
- 每个技能的输入和输出。
- 质量闸门结果。
- 原创性检查结果。
- 未通过项和回退动作。
- 进度记录项。
- 下一步最小可执行动作。

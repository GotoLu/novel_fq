# 全技能应用指南

本指南说明如何把 `.codex/skills/` 下所有技能作为一个完整小说生产系统使用。执行任何链路前，先读取 `../创作质量优先级.md`，并确认本次任务涉及的 `P0-P19`。

## 一、技能选择规则

| 用户意图 | 优先使用 | 辅助使用 | 验收 |
|----------|----------|----------|------|
| 新项目立项 | `skill-chains` | `market-analyzer`、`idea-generator`、`progress-tracker` | P3、P11、P17 |
| 创意优化 | `idea-generator` | `market-analyzer`、`quality-evaluator`、`plagiarism-checker` | 不可替代性、原创性 |
| 人物设计 | `character-designer` | `idea-generator`、`quality-evaluator` | P2、P13 |
| 大纲/世界观/案件设计 | `plot-architect` | `character-designer`、`quality-evaluator`、`plagiarism-checker` | P1、P5、P6、P8、P10、P11、P14、P16、P19 |
| 作者性格定标 | `skill-chains` | `content-writer`、`quality-evaluator`、`progress-tracker` | P9、P18、沉浸感、视角边界 |
| 正文写作 | `content-writer` | `plot-architect`、`character-designer`、`quality-evaluator`、`plagiarism-checker` | P0、P5、P6、P7、P8、P9、作者性格一致性 |
| 章节修订 | `problem-solver` | `quality-evaluator`、`content-writer`、`plot-architect` | P15 |
| 连载复盘 | `progress-tracker` | `quality-evaluator`、`problem-solver` | P12、P14 |
| 发布准备 | `market-analyzer` | `quality-evaluator`、`progress-tracker` | P17 |
| 完稿终审 | `quality-evaluator` | `plot-architect`、`problem-solver`、`progress-tracker` | P18、P19 |
| 原创性审查 | `plagiarism-checker` | 对应产出技能 | 风险可控且重构项明确 |

## 二、全流程执行顺序

### 1. 初始化项目

调用：
- `progress-tracker.init_project`
- `market-analyzer.analyze_platform`
- `market-analyzer.analyze_genre`
- `market-analyzer.analyze_competitors`
- `market-analyzer.generate_positioning`
- `market-analyzer.generate_publishing_fit`

输出：
- 项目记录
- 平台定位
- 题材定位
- 竞品拆解
- 发布适配表

必须记录：
- 目标平台
- 目标读者
- 第一眼卖点
- 风险提示
- 发布材料方向

### 2. 生成并验证创意

调用：
- `idea-generator.generate_ideas`
- `idea-generator.filter_ideas`
- `idea-generator.validate_idea`
- `idea-generator.create_high_concept`
- `plagiarism-checker`

必须通过：
- 替换主角测试
- 替换设定测试
- 替换冲突测试
- 同类替代测试
- 原创性检查

### 3. 构建人物体系

调用：
- `character-designer.design_protagonist`
- `character-designer.design_supporting`
- `character-designer.design_antagonist`
- `character-designer.build_relationships`
- `character-designer.ensemble_rotation`
- `quality-evaluator.evaluate_dimension`

必须产出：
- 主角压力测试
- 反派压迫方式
- 核心配角私线
- 群像轮转表
- 人物关系网络

### 4. 构建情节与长篇资产

调用：
- `plot-architect.design_structure`
- `plot-architect.build_world`
- `plot-architect.create_outline`
- `plot-architect.design_foreshadowing`
- `plot-architect.check_plot_logic`
- `plagiarism-checker`

必须产出：
- 分卷大纲
- 分章大纲
- 场景调度卡
- 章节接力卡
- 爽点链卡
- 长篇资源账本
- 类型专门引擎
- 小说资产库
- 卷级防塌卡
- 完结设计表

### 5. 作者性格定标

调用：
- 新项目：`market-analyzer` 校准题材读者 → `idea-generator` 校准高概念气质 → `character-designer` 校准主角观察方式 → `content-writer` 生成作者性格声明 → `quality-evaluator` 验收
- 已有项目：`progress-tracker` 定位代表章节 → `quality-evaluator` 反推文本气质 → `content-writer` 固化作者性格声明 → `progress-tracker` 入库

必须产出：
- 作者性格核心
- 叙述态度
- 幽默刀口
- 同情对象和鄙视对象
- 迷恋对象
- 句群偏好
- 禁用表达
- 3-5 句落笔样例
- 已有项目的反推依据

必须通过：
- 作者性格符合题材风格、目标读者和主角观察方式。
- 既能指导正文落笔，又不会压扁人物独立性。
- 已有项目的性格声明必须来自已有章节证据，不能凭空重设。

### 6. 写作正文

调用：
- `content-writer.write_opening`
- `content-writer.write_chapter`
- `content-writer.write_climax`
- `content-writer.check_quality`
- `quality-evaluator.evaluate_chapter`
- `plagiarism-checker`

每章必须检查：
- 目标、阻碍、代价、变化、钩子
- 场景调度
- 章节接力
- 情绪投注
- 爽点链
- 风格声明
- 作者性格一致性
- 原创性

### 7. 诊断与改稿

调用：
- `quality-evaluator.evaluate_chapter`
- `problem-solver.diagnose_problem`
- `problem-solver.solve_problem`
- `content-writer` 重新执行对应写作动作

改稿顺序：
1. 结构问题
2. 人物动机问题
3. 追读问题
4. 场景问题
5. 语言问题

每次改稿必须声明：
- 保留什么
- 删除什么
- 增强什么
- 不能破坏什么

### 8. 连载周期审计

调用：
- `progress-tracker.periodic_audit`
- `quality-evaluator.evaluate_full`
- `problem-solver.solve_problem`

周期：
- 每 5-10 章：读者反馈闭环、群像轮转表
- 每 10 章：长篇资源账本
- 每 20-30 章：卷级防塌审计
- 每卷结束：类型机制复盘

### 9. 发布与完结

调用：
- `market-analyzer.generate_publishing_fit`
- `quality-evaluator.evaluate_full`
- `plot-architect.check_plot_logic`
- `progress-tracker.check_node`

发布前必须完成：
- 书名/副标题
- 简介
- 标签
- 章节标题策略
- 前三章卖点
- 章末话术边界

完稿前必须完成：
- 最终审美统一
- 主线偿付
- 人物归宿
- 情绪债清算
- 伏笔回收/留白
- 主题落点
- 续作空间

## 三、质量回退规则

任何阶段未通过质量闸门时：

1. 停止进入下一阶段。
2. 调用 `quality-evaluator` 定位未通过项。
3. 调用 `problem-solver` 做改稿分诊。
4. 回到对应生产技能重做。
5. 调用 `plagiarism-checker` 检查原创性风险。
6. 调用 `progress-tracker` 记录问题、修复依据和结果。

## 四、最小闭环

如果任务很小，只写一章，也必须执行最小闭环：

`plot-architect` 提供章节卡 → `character-designer` 确认人物状态 → 检查作者性格声明或反推结果 → `content-writer` 写作 → `quality-evaluator` 检查 → `problem-solver` 修订 → `plagiarism-checker` 原创性风险审查 → `progress-tracker` 记录。

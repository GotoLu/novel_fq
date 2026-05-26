# 写作技能系统 (Writing Skills System)

## 📚 系统概述

本系统基于爆款小说创作方法论，构建了一套完整的写作技能组件。每个技能遵循**单一职责原则**，专注于写作过程的特定功能模块，通过标准化的接口协同工作，共同构成完整的写作系统。

---

## 🎯 设计原则

### 1. 单一职责原则
每个skill仅专注于一个特定功能模块，功能边界清晰，无重叠。

### 2. 标准化接口
所有skill遵循统一的输入输出格式，便于调用和集成。

### 3. 协同工作
技能间通过标准接口相互调用，形成完整的创作流程。

### 4. 错误处理
每个skill都有完善的错误处理机制，确保系统稳定性。

---

## 📁 技能清单

```
.trae/skills/
│
├── market-analyzer/         # 市场分析技能
│   └── SKILL.md
│
├── idea-generator/          # 创意生成技能
│   └── SKILL.md
│
├── character-designer/      # 人物设计技能
│   └── SKILL.md
│
├── plot-architect/          # 情节架构技能
│   └── SKILL.md
│
├── content-writer/          # 内容创作技能
│   └── SKILL.md
│
├── quality-evaluator/       # 质量评估技能
│   └── SKILL.md
│
├── problem-solver/          # 问题解决技能
│   └── SKILL.md
│
└── progress-tracker/        # 进度跟踪技能
    └── SKILL.md
```

---

## 🔧 技能详解

### 1. market-analyzer（市场分析）

**职责**：市场调研和定位分析

**功能**：
- 平台分析（用户规模、题材分布、收益模式）
- 题材分析（市场容量、竞争强度、趋势）
- 竞品分析（成功要素、差异化机会）
- 定位建议生成

**输入**：平台列表、题材类型、竞品列表、目标读者画像  
**输出**：平台分析报告、题材分析报告、竞品分析报告、定位建议

**调用关系**：
- 被：idea-generator, progress-tracker
- 调用：无

---

### 2. idea-generator（创意生成）

**职责**：创意的激发、筛选和验证

**功能**：
- 创意生成（多种激发方法）
- 创意筛选（多维度评分）
- 创意验证（可行性检验）
- 高概念创建

**输入**：题材类型、激发方法、创意数量、验证标准  
**输出**：创意列表、筛选结果、验证结果、高概念

**调用关系**：
- 被：character-designer, plot-architect, progress-tracker
- 调用：market-analyzer

---

### 3. character-designer（人物设计）

**职责**：人物的塑造和关系设计

**功能**：
- 主角设计（完整人物档案）
- 配角设计（功能性角色）
- 反派设计（动机和能力）
- 关系网络构建
- 一致性检查

**输入**：人物类型、人物数据、关系类型、检查范围  
**输出**：人物档案、关系网络、一致性报告

**调用关系**：
- 被：plot-architect, content-writer, quality-evaluator, progress-tracker
- 调用：idea-generator

---

### 4. plot-architect（情节架构）

**职责**：情节结构设计和世界观构建

**功能**：
- 结构设计（三幕式、四幕式、多卷）
- 世界观构建（设定、规则、势力）
- 大纲创建（分卷、分章）
- 伏笔体系设计
- 情节逻辑检查

**输入**：结构类型、字数、世界观数据、大纲层级  
**输出**：结构设计、世界观、大纲、伏笔体系、逻辑检查结果

**调用关系**：
- 被：content-writer, quality-evaluator, progress-tracker
- 调用：idea-generator, character-designer

---

### 5. content-writer（内容创作）

**职责**：正文内容的写作

**功能**：
- 开篇写作（黄金三章）
- 章节写作（日常章节）
- 高潮写作（关键段落）
- 节奏控制
- 质量检查

**输入**：章节编号、大纲数据、节奏类型、质量检查级别  
**输出**：章节内容、节奏分析、质量检查结果

**调用关系**：
- 被：quality-evaluator, problem-solver, progress-tracker
- 调用：plot-architect, character-designer

---

### 6. quality-evaluator（质量评估）

**职责**：作品质量的量化评估

**功能**：
- 全面评估（7个维度）
- 维度评估（单个维度）
- 章节评估（逐章检查）
- 报告生成
- 版本对比

**输入**：作品ID、章节范围、评估维度、评估级别  
**输出**：综合得分、维度得分、优劣势、改进建议

**调用关系**：
- 被：problem-solver, progress-tracker
- 调用：character-designer, plot-architect, content-writer

---

### 7. problem-solver（问题解决）

**职责**：创作问题的诊断和解决

**功能**：
- 问题诊断（识别根本原因）
- 问题解决（提供解决方案）
- 问题预防（预防措施）
- 解决方案库

**输入**：问题类型、问题描述、上下文、诊断深度  
**输出**：诊断结果、解决方案、预防措施

**调用关系**：
- 被：content-writer, progress-tracker
- 调用：quality-evaluator, plot-architect, character-designer

---

### 8. progress-tracker（进度跟踪）

**职责**：创作进度的管理和节点检验

**功能**：
- 项目初始化
- 进度更新
- 节点检验
- 报告生成
- 计划调整
- 统计数据

**输入**：项目数据、进度数据、节点数据、报告类型  
**输出**：项目信息、进度状态、节点状态、统计数据、报告

**调用关系**：
- 被：所有其他skill
- 调用：quality-evaluator

---

## 🔄 协同工作流程

### 完整创作流程

```
1. 项目初始化
   progress-tracker.init_project()
   ↓
2. 市场分析
   market-analyzer.analyze_platform()
   market-analyzer.analyze_genre()
   market-analyzer.analyze_competitors()
   market-analyzer.generate_positioning()
   progress-tracker.check_node(node_001, node_002)
   ↓
3. 创意开发
   idea-generator.generate_ideas()
   idea-generator.filter_ideas()
   idea-generator.validate_idea()
   idea-generator.create_high_concept()
   progress-tracker.check_node(node_003, node_004)
   ↓
4. 人物设计
   character-designer.design_protagonist()
   character-designer.design_supporting()
   character-designer.design_antagonist()
   character-designer.build_relationships()
   progress-tracker.check_node(node_005, node_006)
   ↓
5. 情节架构
   plot-architect.design_structure()
   plot-architect.build_world()
   plot-architect.create_outline()
   plot-architect.design_foreshadowing()
   progress-tracker.check_node(node_007, node_008, node_009)
   ↓
6. 内容创作
   content-writer.write_opening()
   progress-tracker.check_node(node_010)
   content-writer.write_chapter() × N
   progress-tracker.check_node(node_011, node_012, node_013)
   ↓
7. 质量评估
   quality-evaluator.evaluate_full()
   quality-evaluator.generate_report()
   progress-tracker.check_node(node_014, node_015)
   ↓
8. 问题解决（如需要）
   problem-solver.diagnose_problem()
   problem-solver.solve_problem()
```

---

## 📊 技能调用关系图

```
market-analyzer ←──┐
                   │
idea-generator ←───┤
                   │
character-designer ←┤
                   │
plot-architect ←────┤
                   │
content-writer ←────┤
                   │
quality-evaluator ←─┤
                   │
problem-solver ←────┤
                   │
progress-tracker ───┘
     ↑    ↑    ↑
     │    │    │
     └────┴────┴── 所有skill都可以调用progress-tracker
```

---

## 🎮 使用示例

### 示例1：创建新项目

```javascript
// 1. 初始化项目
await progress-tracker.init_project({
  name: "玄幻小说",
  target_words: 1000000,
  target_duration: 120
});

// 2. 市场分析
const marketResult = await market-analyzer.generate_positioning({
  genre: "玄幻",
  platforms: ["起点", "番茄"]
});

// 3. 创意生成
const ideaResult = await idea-generator.create_high_concept({
  genre: "玄幻",
  technique: "combination"
});

// 4. 人物设计
const charResult = await character-designer.design_protagonist({
  name: "林风",
  personality_traits: ["勇敢", "聪明", "重情义"]
});

// 5. 情节架构
const plotResult = await plot-architect.create_outline({
  structure_type: "three_act",
  total_words: 1000000
});

// 6. 开始写作
const contentResult = await content-writer.write_opening({
  word_count_target: 10000
});
```

---

### 示例2：解决创作问题

```javascript
// 1. 诊断问题
const diagnosis = await problem-solver.diagnose_problem({
  problem_type: "plot_stuck",
  problem_description: "写到第50章，不知道怎么继续推进了",
  context: { current_chapter: 50 }
});

// 2. 获取解决方案
const solution = await problem-solver.solve_problem({
  problem_type: "plot_stuck",
  diagnosis_result: diagnosis
});

// 3. 实施解决方案
// 根据solution的指导实施
```

---

### 示例3：质量评估

```javascript
// 1. 全面评估
const evaluation = await quality-evaluator.evaluate_full({
  work_id: "novel_001",
  evaluation_level: "comprehensive"
});

// 2. 生成报告
const report = await quality-evaluator.generate_report({
  work_id: "novel_001",
  report_type: "full"
});

// 3. 根据评估结果改进
if (evaluation.overall_score < 80) {
  // 查看改进建议
  const suggestions = evaluation.improvement_suggestions;
  // 实施改进
}
```

---

## ⚙️ 接口规范

### 统一输入格式

```json
{
  "action": "动作类型",
  "params": {
    // 动作参数
  }
}
```

### 统一输出格式

```json
{
  "status": "success | error",
  "data": {
    // 结果数据
  },
  "errors": [
    // 错误列表
  ]
}
```

### 错误处理

所有skill都遵循统一的错误处理机制：

```json
{
  "status": "error",
  "error": {
    "code": "ERROR_CODE",
    "message": "错误描述",
    "details": {
      // 错误详情
    }
  }
}
```

---

## 📈 性能指标

| 技能 | 主要操作 | 响应时间 |
|------|---------|---------|
| market-analyzer | 平台分析 | < 5秒 |
| idea-generator | 创意生成 | < 1分钟 |
| character-designer | 主角设计 | < 10分钟 |
| plot-architect | 大纲创建 | < 20分钟 |
| content-writer | 章节写作 | 15-30分钟/章 |
| quality-evaluator | 全面评估 | < 5分钟 |
| problem-solver | 问题诊断 | < 1分钟 |
| progress-tracker | 进度更新 | < 1秒 |

---

## 🔒 错误处理机制

### 错误类型分类

1. **参数错误**：INVALID_ACTION, MISSING_PARAMS, INVALID_DATA
2. **数据错误**：DATA_NOT_FOUND, INSUFFICIENT_DATA
3. **逻辑错误**：LOGIC_ERROR, CONSISTENCY_ERROR
4. **执行错误**：EXECUTION_FAILED, TIMEOUT

### 错误处理流程

```
错误发生
    ↓
错误识别和分类
    ↓
生成错误响应
    ↓
记录错误日志
    ↓
返回错误信息
    ↓
（可选）提供恢复建议
```

---

## 🚀 扩展指南

### 添加新技能

1. 创建技能目录：`.trae/skills/new-skill/`
2. 创建SKILL.md文件，包含：
   - name和description（frontmatter）
   - 功能定义
   - 输入输出参数
   - 执行逻辑
   - 错误处理
   - 调用接口
3. 确保遵循单一职责原则
4. 定义与其他技能的调用关系
5. 测试和验证

### 技能命名规范

- 使用小写字母和连字符
- 名称要清晰表达职责
- 避免与现有技能重复
- 示例：market-analyzer, idea-generator

---

## 📝 最佳实践

### 1. 按流程调用
按照创作流程顺序调用技能，确保前置条件满足。

### 2. 及时检查节点
每个阶段完成后，使用progress-tracker检查关键节点。

### 3. 定期评估质量
创作过程中定期使用quality-evaluator评估质量。

### 4. 及时解决问题
遇到问题时立即使用problem-solver诊断和解决。

### 5. 保持进度更新
定期更新进度，确保进度数据准确。

---

## 🎯 总结

本写作技能系统通过8个单一职责的技能组件，覆盖了小说创作的完整流程。每个技能都有明确的功能边界、标准化的接口、完善的错误处理机制，能够协同工作，为创作者提供系统化的写作支持。

**核心优势**：
- ✅ 单一职责，功能清晰
- ✅ 标准接口，易于集成
- ✅ 协同工作，流程完整
- ✅ 错误处理，稳定可靠
- ✅ 可扩展，易于维护

**适用场景**：
- 新手作者：系统化指导创作
- 进阶作者：提升创作效率和质量
- 团队协作：标准化创作流程

---

**祝创作顺利！** 🎉

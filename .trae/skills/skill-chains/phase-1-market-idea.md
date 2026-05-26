# 阶段一：市场洞察与创意孵化

## 🎯 阶段目标

建立市场敏感度，培养创意生成能力，为后续创作奠定坚实基础。

**核心能力**：
- 市场趋势洞察能力
- 平台特性分析能力
- 创意激发和筛选能力
- 高概念提炼能力

**学习周期**：1-2周

---

## 🔗 Skill链结构

```
┌─────────────────────────────────────────────────────────────┐
│                    阶段一 Skill链                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   market-analyzer ──────→ idea-generator                   │
│        │                        │                          │
│        │                        │                          │
│        ↓                        ↓                          │
│   平台分析              创意生成                            │
│   题材分析              创意筛选                            │
│   竞品分析              创意验证                            │
│   定位建议              高概念创建                          │
│                                                             │
│        │                        │                          │
│        └────────┬───────────────┘                          │
│                 ↓                                           │
│         progress-tracker                                    │
│         (节点检验)                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 技能组件详解

### 1. market-analyzer（市场分析）

#### 功能定位
市场分析是创作起点，决定作品的平台选择、题材定位和差异化策略。

#### 核心功能
| 功能 | 说明 | 输出成果 |
|------|------|---------|
| 平台分析 | 分析各平台特性、用户画像、收益模式 | 平台分析报告 |
| 题材分析 | 分析题材热度、竞争强度、发展趋势 | 题材分析报告 |
| 竞品分析 | 分析成功作品的核心要素 | 竞品分析报告 |
| 定位建议 | 综合分析，给出定位建议 | 定位策略文档 |

#### 学习目标
- [ ] 掌握主流平台特性（起点、晋江、番茄等）
- [ ] 学会分析题材市场容量和竞争强度
- [ ] 能够识别竞品的核心成功要素
- [ ] 能够制定差异化定位策略

#### 应用场景
1. **新项目启动**：确定平台和题材选择
2. **定位调整**：根据市场变化调整策略
3. **竞品研究**：学习成功作品经验

---

### 2. idea-generator（创意生成）

#### 功能定位
创意生成是作品灵魂，决定作品的核心吸引力和差异化优势。

#### 核心功能
| 功能 | 说明 | 输出成果 |
|------|------|---------|
| 创意生成 | 使用多种方法激发创意 | 创意列表 |
| 创意筛选 | 多维度评分筛选 | 筛选结果 |
| 创意验证 | 验证创意可行性 | 验证报告 |
| 高概念创建 | 提炼核心概念 | 高概念文档 |

#### 学习目标
- [ ] 掌握4种创意激发方法（What-if、组合、反转、跨界）
- [ ] 学会多维度评估创意质量
- [ ] 能够验证创意的可行性和延展性
- [ ] 能够提炼简洁有力的高概念

#### 应用场景
1. **创意开发**：为作品寻找核心创意
2. **创意优化**：优化已有创意
3. **差异化设计**：确保创意新颖性

---

## 🔄 技能衔接关系

### 调用流程

```
1. 市场分析
   market-analyzer.analyze_platform()
   market-analyzer.analyze_genre()
   market-analyzer.analyze_competitors()
   market-analyzer.generate_positioning()
         ↓
2. 创意生成（使用市场分析结果）
   idea-generator.generate_ideas({
     genre: marketResult.recommended_genre,
     technique: "combination"
   })
         ↓
3. 创意筛选
   idea-generator.filter_ideas()
         ↓
4. 创意验证
   idea-generator.validate_idea()
         ↓
5. 高概念创建
   idea-generator.create_high_concept()
         ↓
6. 节点检验
   progress-tracker.check_node("node_001", "node_002")
```

### 数据流转

```
market-analyzer 输出:
├── platform_analysis (平台分析)
├── genre_analysis (题材分析)
├── competitor_analysis (竞品分析)
└── positioning_suggestion (定位建议)
        ↓
        作为 idea-generator 的输入
        ↓
idea-generator 输出:
├── ideas (创意列表)
├── filtered_ideas (筛选结果)
├── validation_result (验证结果)
└── high_concept (高概念)
```

---

## 📖 技能应用指南

### 应用场景一：新项目启动

**场景描述**：开始一个新的小说项目，需要确定平台、题材和核心创意。

**操作步骤**：

```javascript
// Step 1: 平台分析
const platformResult = await market-analyzer.analyze_platform({
  platforms: ["起点", "晋江", "番茄", "纵横"]
});

// Step 2: 题材分析
const genreResult = await market-analyzer.analyze_genre({
  genre: "玄幻",
  platforms: ["起点", "番茄"]
});

// Step 3: 竞品分析
const competitorResult = await market-analyzer.analyze_competitors({
  competitor_works: ["《诡秘之主》", "《大奉打更人》"],
  genre: "玄幻"
});

// Step 4: 定位建议
const positioningResult = await market-analyzer.generate_positioning({
  genre: "玄幻",
  target_readers: {
    age_range: "18-35",
    gender: "male",
    preferences: ["爽文", "升级流"]
  }
});

// Step 5: 创意生成
const ideasResult = await idea-generator.generate_ideas({
  genre: positioningResult.recommended_genre,
  technique: "combination",
  idea_count: 10
});

// Step 6: 创意筛选
const filteredResult = await idea-generator.filter_ideas({
  ideas: ideasResult.ideas,
  criteria: {
    novelty_threshold: 7,
    extensibility_threshold: 8
  }
});

// Step 7: 创意验证
const validationResult = await idea-generator.validate_idea({
  target_idea: filteredResult.top_idea
});

// Step 8: 高概念创建
const highConceptResult = await idea-generator.create_high_concept({
  validated_idea: validationResult.idea
});
```

**预期效果**：
- 明确平台选择和题材定位
- 获得经过验证的核心创意
- 形成简洁的高概念陈述

---

### 应用场景二：创意优化

**场景描述**：已有初步创意，需要优化和验证。

**操作步骤**：

```javascript
// Step 1: 验证现有创意
const validationResult = await idea-generator.validate_idea({
  target_idea: {
    core_concept: "修仙者获得吞噬星空的能力",
    core_conflict: "主角vs宇宙意志",
    emotional_core: "逆天改命的热血"
  }
});

// Step 2: 根据验证结果优化
if (!validationResult.is_valid) {
  // 使用问题诊断
  const issues = validationResult.issues;
  
  // 重新生成创意
  const newIdeas = await idea-generator.generate_ideas({
    technique: "what_if",
    idea_count: 5
  });
}

// Step 3: 创建高概念
const highConcept = await idea-generator.create_high_concept({
  validated_idea: validationResult.idea
});
```

---

## 📊 技能掌握评估标准

### 评估维度

| 维度 | 初级 | 中级 | 高级 |
|------|------|------|------|
| 市场分析 | 能完成基础平台分析 | 能分析竞争格局 | 能制定差异化策略 |
| 创意生成 | 能使用1-2种方法 | 能使用全部方法 | 能组合创新方法 |
| 创意筛选 | 能完成基础筛选 | 能多维度评估 | 能精准识别潜力 |
| 创意验证 | 能完成基础验证 | 能识别风险 | 能提出优化方案 |
| 高概念 | 能创建基础概念 | 能提炼核心冲突 | 能设计记忆点 |

### 评估指标

```json
{
  "market_analyzer": {
    "platform_analysis": {
      "completeness": "≥80%",
      "accuracy": "≥70%"
    },
    "positioning_quality": {
      "differentiation_score": "≥7分",
      "feasibility_score": "≥8分"
    }
  },
  "idea_generator": {
    "idea_quality": {
      "novelty_score": "≥7分",
      "extensibility_score": "≥8分",
      "conflict_strength": "≥7分"
    },
    "high_concept": {
      "clarity": "一句话能说清",
      "attractiveness": "≥8分"
    }
  }
}
```

### 评估方法

1. **作品检验**：完成至少3个项目的市场分析和创意开发
2. **同行评审**：由有经验作者评审定位和创意质量
3. **数据验证**：通过实际数据验证分析准确性
4. **创意测试**：测试创意的传播便利性和吸引力

---

## 🎯 阶段成果交付物

完成本阶段后，应产出以下交付物：

### 1. 市场分析报告
- 平台分析报告
- 题材分析报告
- 竞品分析报告
- 定位策略文档

### 2. 创意开发文档
- 创意列表（至少10个）
- 创意筛选结果
- 创意验证报告
- 高概念文档

### 3. 项目启动文档
- 平台选择决策
- 题材定位确认
- 核心创意确定
- 差异化策略

---

## ⚠️ 常见问题与解决

### 问题1：市场分析过于宏观
**表现**：分析停留在表面，缺乏具体指导意义  
**解决**：深入分析具体作品，提炼可操作的成功要素

### 问题2：创意缺乏新意
**表现**：创意套路化，差异化不足  
**解决**：
- 扩大输入范围，跨类型学习
- 使用多种创意激发方法组合
- 强化反转和跨界思维

### 问题3：高概念不够简洁
**表现**：概念复杂，难以传播  
**解决**：
- 聚焦核心冲突
- 提炼一句话表达
- 设计记忆点

---

## 📚 学习资源

### 必读内容
- 市场分析方法论
- 创意激发技巧手册
- 高概念创建指南

### 实践练习
- 完成3个不同题材的市场分析
- 使用每种创意激发方法生成创意
- 创建5个高概念并测试传播性

### 案例学习
- 分析10部爆款小说的市场定位
- 研究成功作品的核心创意
- 学习高概念的提炼方法

---

## 🚀 进入下一阶段

完成本阶段学习并通过评估后，可进入：

**[阶段二：人物体系构建](./phase-2-character.md)**

**前置条件检查**：
- [ ] 完成市场分析报告
- [ ] 确定平台和题材定位
- [ ] 验证核心创意可行性
- [ ] 创建高概念文档
- [ ] 通过阶段一评估

---

**阶段一学习完成标志**：能够独立完成市场分析和创意开发，产出高质量的定位策略和核心创意。

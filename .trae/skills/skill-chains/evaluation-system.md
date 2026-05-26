# 技能评估体系

## 📊 评估体系概述

本体系建立完整的技能掌握评估标准，确保每个skill链都能达到预期的应用水平。

---

## 🎯 评估维度框架

### 总体评估框架

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           技能评估体系框架                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        阶段评估 (5个阶段)                            │   │
│  │  ├── 阶段一评估：市场洞察与创意孵化                                  │   │
│  │  ├── 阶段二评估：人物体系构建                                        │   │
│  │  ├── 阶段三评估：情节架构设计                                        │   │
│  │  ├── 阶段四评估：内容创作执行                                        │   │
│  │  └── 阶段五评估：系统整合与优化                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        技能评估 (8个技能)                            │   │
│  │  ├── market-analyzer 评估                                            │   │
│  │  ├── idea-generator 评估                                             │   │
│  │  ├── character-designer 评估                                         │   │
│  │  ├── plot-architect 评估                                             │   │
│  │  ├── content-writer 评估                                             │   │
│  │  ├── quality-evaluator 评估                                          │   │
│  │  ├── problem-solver 评估                                             │   │
│  │  └── progress-tracker 评估                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        能力评估 (综合能力)                           │   │
│  │  ├── 理论掌握度                                                      │   │
│  │  ├── 实践应用度                                                      │   │
│  │  ├── 问题解决度                                                      │   │
│  │  └── 创新拓展度                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📈 阶段评估标准

### 阶段一评估：市场洞察与创意孵化

#### 评估维度

| 维度 | 权重 | 初级标准 | 中级标准 | 高级标准 |
|------|------|---------|---------|---------|
| 市场分析能力 | 30% | 能完成基础分析 | 能分析竞争格局 | 能制定差异化策略 |
| 创意生成能力 | 30% | 能使用1-2种方法 | 能使用全部方法 | 能组合创新方法 |
| 创意筛选能力 | 20% | 能完成基础筛选 | 能多维度评估 | 能精准识别潜力 |
| 高概念能力 | 20% | 能创建基础概念 | 能提炼核心冲突 | 能设计记忆点 |

#### 评估指标

```json
{
  "phase_1_evaluation": {
    "market_analyzer": {
      "platform_analysis": {
        "completeness": { "target": "≥80%", "weight": 0.3 },
        "accuracy": { "target": "≥70%", "weight": 0.3 },
        "actionability": { "target": "≥7分", "weight": 0.4 }
      },
      "positioning_quality": {
        "differentiation_score": { "target": "≥7分", "weight": 0.5 },
        "feasibility_score": { "target": "≥8分", "weight": 0.5 }
      }
    },
    "idea_generator": {
      "idea_quality": {
        "novelty_score": { "target": "≥7分", "weight": 0.3 },
        "extensibility_score": { "target": "≥8分", "weight": 0.3 },
        "conflict_strength": { "target": "≥7分", "weight": 0.2 },
        "market_match": { "target": "≥70分", "weight": 0.2 }
      },
      "high_concept": {
        "clarity": { "target": "一句话能说清", "weight": 0.4 },
        "attractiveness": { "target": "≥8分", "weight": 0.3 },
        "memorability": { "target": "≥7分", "weight": 0.3 }
      }
    }
  }
}
```

#### 通过标准

- 综合得分 ≥ 70分：初级通过
- 综合得分 ≥ 80分：中级通过
- 综合得分 ≥ 90分：高级通过

---

### 阶段二评估：人物体系构建

#### 评估维度

| 维度 | 权重 | 初级标准 | 中级标准 | 高级标准 |
|------|------|---------|---------|---------|
| 主角设计能力 | 35% | 能设计基础主角 | 能设计代入感强的主角 | 能设计有深度的主角 |
| 配角设计能力 | 20% | 能设计基础配角 | 能设计功能性配角 | 能设计有魅力的配角 |
| 反派设计能力 | 20% | 能设计基础反派 | 能设计有动机的反派 | 能设计有深度的反派 |
| 关系设计能力 | 15% | 能设计基础关系 | 能设计关系发展 | 能设计有张力的关系网络 |
| 一致性把控能力 | 10% | 能发现明显问题 | 能保持基本一致 | 能完美保持一致 |

#### 评估指标

```json
{
  "phase_2_evaluation": {
    "protagonist": {
      "empathy_score": { "target": "≥8分", "weight": 0.3 },
      "depth_score": { "target": "≥7分", "weight": 0.2 },
      "arc_completeness": { "target": "≥80%", "weight": 0.2 },
      "motivation_clarity": { "target": "清晰", "weight": 0.15 },
      "ability_system": { "target": "完整", "weight": 0.15 }
    },
    "supporting": {
      "functionality": { "target": "明确", "weight": 0.4 },
      "memorability": { "target": "≥7分", "weight": 0.3 },
      "relationship_development": { "target": "有轨迹", "weight": 0.3 }
    },
    "antagonist": {
      "motivation_rationality": { "target": "≥8分", "weight": 0.3 },
      "depth_score": { "target": "≥7分", "weight": 0.3 },
      "threat_degree": { "target": "匹配主角成长", "weight": 0.2 },
      "humanity": { "target": "有展现", "weight": 0.2 }
    },
    "relationship_network": {
      "clarity": { "target": "清晰", "weight": 0.3 },
      "tension": { "target": "≥7分", "weight": 0.4 },
      "development": { "target": "有轨迹", "weight": 0.3 }
    }
  }
}
```

---

### 阶段三评估：情节架构设计

#### 评估维度

| 维度 | 权重 | 初级标准 | 中级标准 | 高级标准 |
|------|------|---------|---------|---------|
| 结构设计能力 | 25% | 能设计基础结构 | 能设计合理结构 | 能设计精妙结构 |
| 世界观构建能力 | 25% | 能构建基础世界观 | 能构建完整世界观 | 能构建自洽世界观 |
| 大纲创建能力 | 25% | 能创建分卷大纲 | 能创建分章大纲 | 能创建详细大纲 |
| 伏笔设计能力 | 15% | 能设计基础伏笔 | 能设计伏笔体系 | 能设计精妙伏笔 |
| 逻辑把控能力 | 10% | 能发现明显问题 | 能保持基本逻辑 | 能完美保持逻辑 |

#### 评估指标

```json
{
  "phase_3_evaluation": {
    "structure": {
      "completeness": { "target": "≥90%", "weight": 0.3 },
      "climax_distribution": { "target": "合理", "weight": 0.3 },
      "turning_points": { "target": "充足", "weight": 0.2 },
      "pacing_balance": { "target": "张弛有度", "weight": 0.2 }
    },
    "world_building": {
      "completeness": { "target": "≥90%", "weight": 0.3 },
      "consistency": { "target": "≥90%", "weight": 0.3 },
      "depth": { "target": "≥8分", "weight": 0.2 },
      "uniqueness": { "target": "≥7分", "weight": 0.2 }
    },
    "outline": {
      "detail_level": { "target": "分章级别", "weight": 0.3 },
      "event_coverage": { "target": "≥95%", "weight": 0.3 },
      "progression_clarity": { "target": "清晰", "weight": 0.2 },
      "conflict_density": { "target": "充足", "weight": 0.2 }
    },
    "foreshadowing": {
      "coverage": { "target": "主要情节都有", "weight": 0.4 },
      "recycle_rate": { "target": "≥90%", "weight": 0.3 },
      "subtlety": { "target": "适中", "weight": 0.3 }
    }
  }
}
```

---

### 阶段四评估：内容创作执行

#### 评估维度

| 维度 | 权重 | 初级标准 | 中级标准 | 高级标准 |
|------|------|---------|---------|---------|
| 开篇创作能力 | 25% | 能写基础开篇 | 能写代入感强的开篇 | 能写精彩开篇 |
| 章节写作能力 | 30% | 能完成章节 | 能稳定产出 | 能高质量产出 |
| 高潮创作能力 | 20% | 能写基础高潮 | 能写有冲击的高潮 | 能写精彩高潮 |
| 节奏控制能力 | 15% | 能基本控制节奏 | 能良好控制节奏 | 能精妙控制节奏 |
| 问题解决能力 | 10% | 能解决简单问题 | 能解决常见问题 | 能解决复杂问题 |

#### 评估指标

```json
{
  "phase_4_evaluation": {
    "opening": {
      "empathy_strength": { "target": "≥8分", "weight": 0.3 },
      "hook_strength": { "target": "≥8分", "weight": 0.3 },
      "reader_retention": { "target": "≥70%", "weight": 0.2 },
      "information_density": { "target": "适中", "weight": 0.2 }
    },
    "chapter": {
      "quality_stability": { "target": "≥7分", "weight": 0.3 },
      "progression_clarity": { "target": "明确", "weight": 0.2 },
      "word_count_consistency": { "target": "±10%", "weight": 0.2 },
      "character_consistency": { "target": "≥90%", "weight": 0.15 },
      "language_quality": { "target": "≥7分", "weight": 0.15 }
    },
    "climax": {
      "intensity": { "target": "≥8分", "weight": 0.4 },
      "emotional_impact": { "target": "≥8分", "weight": 0.3 },
      "resolution": { "target": "合理", "weight": 0.3 }
    },
    "pacing": {
      "balance": { "target": "张弛有度", "weight": 0.4 },
      "information_density": { "target": "适中", "weight": 0.3 },
      "tension_curve": { "target": "合理", "weight": 0.3 }
    }
  }
}
```

---

### 阶段五评估：系统整合与优化

#### 评估维度

| 维度 | 权重 | 初级标准 | 中级标准 | 高级标准 |
|------|------|---------|---------|---------|
| 流程整合能力 | 30% | 能完成基本流程 | 能流畅执行流程 | 能优化流程 |
| 持续优化能力 | 25% | 能识别问题 | 能解决问题 | 能持续改进 |
| 质量把控能力 | 25% | 能基本把控质量 | 能良好把控质量 | 能精准把控质量 |
| 完稿能力 | 20% | 能完成作品 | 能高质量完稿 | 能完美收官 |

#### 评估指标

```json
{
  "phase_5_evaluation": {
    "integration": {
      "workflow_completeness": { "target": "100%", "weight": 0.3 },
      "skill_coordination": { "target": "流畅", "weight": 0.3 },
      "data_flow": { "target": "正确", "weight": 0.2 },
      "node_completion": { "target": "100%", "weight": 0.2 }
    },
    "optimization": {
      "quality_improvement": { "target": "持续提升", "weight": 0.4 },
      "problem_resolution_rate": { "target": "≥90%", "weight": 0.3 },
      "efficiency": { "target": "稳定高效", "weight": 0.3 }
    },
    "completion": {
      "foreshadowing_recycle": { "target": "100%", "weight": 0.3 },
      "consistency": { "target": "≥95%", "weight": 0.3 },
      "logic": { "target": "≥95%", "weight": 0.2 },
      "overall_quality": { "target": "≥80分", "weight": 0.2 }
    }
  }
}
```

---

## 📊 技能评估标准

### 单技能评估模板

```json
{
  "skill_evaluation_template": {
    "skill_name": "xxx",
    "evaluation_dimensions": [
      {
        "dimension": "理论掌握",
        "weight": 0.3,
        "indicators": [
          "概念理解程度",
          "方法掌握程度",
          "原理理解程度"
        ]
      },
      {
        "dimension": "实践应用",
        "weight": 0.4,
        "indicators": [
          "应用准确性",
          "应用效率",
          "应用效果"
        ]
      },
      {
        "dimension": "问题解决",
        "weight": 0.2,
        "indicators": [
          "问题识别能力",
          "问题解决能力",
          "预防能力"
        ]
      },
      {
        "dimension": "创新拓展",
        "weight": 0.1,
        "indicators": [
          "方法创新",
          "应用拓展",
          "效果提升"
        ]
      }
    ],
    "passing_threshold": {
      "beginner": 60,
      "intermediate": 75,
      "advanced": 90
    }
  }
}
```

---

## 🎯 评估方法

### 1. 自我评估

```javascript
// 自我评估流程
async function selfEvaluation(phase) {
  // 1. 完成评估问卷
  const questionnaire = await getEvaluationQuestionnaire(phase);
  const answers = await fillQuestionnaire(questionnaire);
  
  // 2. 计算得分
  const score = calculateScore(answers);
  
  // 3. 识别薄弱环节
  const weaknesses = identifyWeaknesses(answers);
  
  // 4. 生成改进计划
  const improvementPlan = generateImprovementPlan(weaknesses);
  
  return { score, weaknesses, improvementPlan };
}
```

### 2. 作品评估

```javascript
// 通过作品质量评估技能掌握程度
async function workEvaluation(work) {
  // 1. 作品质量评估
  const quality = await quality-evaluator.evaluate_full({
    work_id: work.id,
    evaluation_level: "comprehensive"
  });
  
  // 2. 技能掌握推断
  const skillMastery = inferSkillMastery(quality);
  
  // 3. 识别待提升技能
  const skillsToImprove = identifySkillsToImprove(skillMastery);
  
  return { quality, skillMastery, skillsToImprove };
}
```

### 3. 同行评审

```javascript
// 同行评审流程
async function peerReview(phase, reviewer) {
  // 1. 提交作品和材料
  const materials = await prepareMaterials(phase);
  
  // 2. 评审
  const review = await reviewer.review(materials);
  
  // 3. 反馈整理
  const feedback = organizeFeedback(review);
  
  // 4. 改进建议
  const suggestions = generateSuggestions(feedback);
  
  return { feedback, suggestions };
}
```

---

## 📋 评估报告模板

```markdown
# 技能评估报告

## 基本信息
- 评估对象：[姓名/项目]
- 评估阶段：[阶段X]
- 评估日期：[日期]
- 评估方法：[自我评估/作品评估/同行评审]

## 综合得分
- 总分：[XX]分
- 等级：[初级/中级/高级]
- 是否通过：[是/否]

## 维度得分
| 维度 | 得分 | 权重 | 加权得分 | 目标 | 是否达标 |
|------|------|------|---------|------|---------|
| [维度1] | [XX] | [XX%] | [XX] | [XX] | [是/否] |
| [维度2] | [XX] | [XX%] | [XX] | [XX] | [是/否] |
| ... | ... | ... | ... | ... | ... |

## 优势分析
1. [优势1]
2. [优势2]
3. [优势3]

## 劣势分析
1. [劣势1] - 影响：[XX]
2. [劣势2] - 影响：[XX]
3. [劣势3] - 影响：[XX]

## 改进建议
1. [建议1] - 优先级：[高/中/低]
2. [建议2] - 优先级：[高/中/低]
3. [建议3] - 优先级：[高/中/低]

## 下一步行动
- [ ] [行动1]
- [ ] [行动2]
- [ ] [行动3]
```

---

## 🏆 评估等级体系

| 等级 | 分数范围 | 能力描述 | 可进入阶段 |
|------|---------|---------|-----------|
| 初级 | 60-74分 | 掌握基本方法，能完成基础任务 | 下一阶段（需加强练习） |
| 中级 | 75-89分 | 熟练应用方法，能完成标准任务 | 下一阶段 |
| 高级 | 90-100分 | 精通方法，能完成复杂任务并创新 | 下一阶段（可作为指导者） |

---

## 📈 持续评估机制

### 评估周期

| 阶段 | 评估频率 | 评估方式 |
|------|---------|---------|
| 学习期 | 每周一次 | 自我评估 |
| 实践期 | 每两周一次 | 作品评估 |
| 熟练期 | 每月一次 | 综合评估 |
| 精通期 | 每季度一次 | 同行评审 |

### 评估记录

建议建立评估记录档案，跟踪技能掌握进度：

```json
{
  "evaluation_history": [
    {
      "date": "2026-05-26",
      "phase": 1,
      "score": 75,
      "level": "intermediate",
      "weaknesses": ["创意筛选能力"],
      "actions": ["加强创意筛选练习"]
    }
  ]
}
```

# 阶段二：人物体系构建

## 🎯 阶段目标

掌握立体人物塑造方法，建立完整的人物关系网络，为情节设计提供坚实基础。

**核心能力**：
- 主角塑造能力
- 配角设计能力
- 反派构建能力
- 关系网络设计能力
- 人物一致性把控能力

**学习周期**：2-3周

**前置依赖**：阶段一（市场洞察与创意孵化）

---

## 🔗 Skill链结构

```
┌─────────────────────────────────────────────────────────────┐
│                    阶段二 Skill链                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   idea-generator ────→ character-designer                  │
│        │                      │                            │
│        │                      │                            │
│        ↓                      ↓                            │
│   高概念信息            主角设计                              │
│   核心冲突              配角设计                              │
│                        反派设计                              │
│                        关系网络                              │
│                        一致性检查                            │
│                              │                              │
│                              ↓                              │
│                      quality-evaluator                      │
│                      (人物维度评估)                          │
│                              │                              │
│                              ↓                              │
│                      progress-tracker                       │
│                      (节点检验)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 技能组件详解

### 1. character-designer（人物设计）

#### 功能定位
人物是故事的载体，人物设计决定读者的代入感和情感投入。

#### 核心功能
| 功能 | 说明 | 输出成果 |
|------|------|---------|
| 主角设计 | 设计完整的主角档案 | 主角人物档案 |
| 配角设计 | 设计功能性配角 | 配角人物档案 |
| 反派设计 | 设计有深度的反派 | 反派人物档案 |
| 关系网络 | 构建人物关系网络 | 关系网络图 |
| 一致性检查 | 检查人物行为一致性 | 一致性报告 |

#### 学习目标
- [ ] 掌握主角设计5大要素（性格、背景、能力、动机、弧光）
- [ ] 学会设计代入感强的主角
- [ ] 能够设计功能性配角
- [ ] 能够构建有深度的反派
- [ ] 能够设计有张力的人物关系
- [ ] 能够保持人物行为一致性

---

### 2. quality-evaluator（质量评估-人物维度）

#### 功能定位
评估人物塑造质量，确保人物立体、一致、有代入感。

#### 核心功能
| 功能 | 说明 | 输出成果 |
|------|------|---------|
| 人物维度评估 | 评估人物塑造质量 | 人物质量得分 |
| 代入感评估 | 评估主角代入感 | 代入感得分 |
| 一致性评估 | 评估人物一致性 | 一致性得分 |

---

## 🔄 技能衔接关系

### 调用流程

```
1. 获取创意信息（来自阶段一）
   idea-generator.get_high_concept()
         ↓
2. 设计主角
   character-designer.design_protagonist({
     core_conflict: highConcept.core_conflict,
     emotional_core: highConcept.emotional_core
   })
         ↓
3. 设计核心配角
   character-designer.design_supporting({
     type: "mentor",
     relationship_to_protagonist: "师徒"
   })
         ↓
4. 设计反派
   character-designer.design_antagonist({
     conflict_with_protagonist: core_conflict
   })
         ↓
5. 构建关系网络
   character-designer.build_relationships({
     characters: [protagonist, supporting, antagonist]
   })
         ↓
6. 人物质量评估
   quality-evaluator.evaluate_dimension({
     dimension: "character_depth"
   })
         ↓
7. 一致性检查
   character-designer.check_consistency()
         ↓
8. 节点检验
   progress-tracker.check_node("node_005", "node_006")
```

### 数据流转

```
idea-generator 输出:
├── high_concept (高概念)
├── core_conflict (核心冲突)
└── emotional_core (情感内核)
        ↓
        作为 character-designer 的输入
        ↓
character-designer 输出:
├── protagonist_profile (主角档案)
├── supporting_profiles (配角档案)
├── antagonist_profile (反派档案)
├── relationship_network (关系网络)
└── consistency_report (一致性报告)
        ↓
        作为 quality-evaluator 的输入
        ↓
quality-evaluator 输出:
├── character_depth_score (人物深度得分)
├── empathy_score (代入感得分)
└── consistency_score (一致性得分)
```

---

## 📖 技能应用指南

### 应用场景一：主角设计

**场景描述**：设计一个有代入感、有成长空间的主角。

**操作步骤**：

```javascript
// Step 1: 设计主角基础信息
const protagonist = await character-designer.design_protagonist({
  character_data: {
    name: "林风",
    age: 18,
    gender: "male",
    personality_traits: ["勇敢", "聪明", "重情义", "有些固执"],
    background: "小家族庶子，母亲早亡，受尽冷眼，但性格坚韧"
  }
});

// Step 2: 完善主角能力体系
protagonist.abilities = {
  initial: "普通修为，但有坚韧意志",
  golden_finger: "吞噬星空的能力（逐步觉醒）",
  growth_path: "吞噬能力觉醒 → 能力成长 → 能力质变"
};

// Step 3: 设计主角动机体系
protagonist.motivation = {
  external_goal: "成为强者，保护在乎的人",
  internal_need: "证明自己，获得认可",
  core_fear: "失去在乎的人",
  values: "重情重义，不屈不挠"
};

// Step 4: 设计主角弧光
protagonist.arc = {
  start_state: "受尽冷眼的庶子，渴望变强",
  growth_trajectory: "获得能力 → 遭遇挫折 → 成长蜕变 → 最终成就",
  key_turning_points: [
    "获得金手指",
    "第一次重大挫折",
    "关键抉择",
    "最终蜕变"
  ],
  end_state: "成为强者，守护一切"
};

// Step 5: 设计代入感要素
protagonist.empathy_design = {
  empathy_points: ["出身卑微", "受尽冷眼", "重情重义"],
  care_points: ["在乎母亲", "在乎朋友", "有守护的目标"],
  expectation_points: ["逆袭期待", "成长期待", "正义期待"]
};
```

**设计要点**：
1. **性格立体**：3-5个核心特质，包含矛盾点
2. **背景有料**：有成长经历和关键事件
3. **动机明确**：外在目标和内在需求清晰
4. **弧光完整**：有清晰的成长轨迹
5. **代入感强**：有共情点、认同点、关心点

---

### 应用场景二：配角设计

**场景描述**：设计功能性配角，支撑故事发展。

**操作步骤**：

```javascript
// 设计导师型配角
const mentor = await character-designer.design_supporting({
  character_type: "supporting",
  character_data: {
    name: "玄老",
    role: "mentor",
    personality_traits: ["睿智", "神秘", "护短"],
    background: "隐世强者，看中主角潜力"
  },
  relationship_to_protagonist: {
    type: "mentor",
    development: "偶然相遇 → 考验主角 → 收为弟子 → 指引成长"
  }
});

// 设计盟友型配角
const ally = await character-designer.design_supporting({
  character_type: "supporting",
  character_data: {
    name: "苏晴",
    role: "ally",
    personality_traits: ["善良", "聪明", "有些傲娇"],
    background: "大家族千金，与主角有相似经历"
  },
  relationship_to_protagonist: {
    type: "ally",
    development: "初遇冲突 → 逐渐理解 → 成为盟友 → 可能的感情线"
  }
});

// 设计对手型配角
const rival = await character-designer.design_supporting({
  character_type: "supporting",
  character_data: {
    name: "赵天",
    role: "rival",
    personality_traits: ["骄傲", "有实力", "有底线"],
    background: "家族嫡子，与主角形成竞争关系"
  },
  relationship_to_protagonist: {
    type: "rival",
    development: "初遇冲突 → 竞争对抗 → 逐渐认可 → 可能的转化"
  }
});
```

**设计要点**：
1. **功能明确**：每个配角都有明确的故事功能
2. **性格鲜明**：性格特点突出，易于记忆
3. **关系发展**：与主角关系有发展轨迹
4. **避免冗余**：不设计无用的配角

---

### 应用场景三：反派设计

**场景描述**：设计有深度、有魅力的反派。

**操作步骤**：

```javascript
// 设计主要反派
const antagonist = await character-designer.design_antagonist({
  character_data: {
    name: "魔尊",
    personality_traits: ["冷酷", "睿智", "有自己的道"],
    background: "曾经也是正道天才，因遭遇背叛而堕入魔道"
  },
  motivation: {
    surface_motive: "统治世界",
    deep_motive: "向背叛他的世界复仇",
    values: "力量至上，弱者没有生存权",
    rationality: "有自己的逻辑和信念，不是纯粹的恶"
  },
  conflict_with_protagonist: {
    nature: "道路之争",
    levels: [
      "利益冲突",
      "理念冲突",
      "生存冲突"
    ],
    escalation: "从间接冲突 → 直接对抗 → 最终决战"
  },
  abilities: {
    power_level: "远超主角初期",
    threat_degree: "极高",
    weakness: "内心的执念和过去的创伤"
  },
  complexity: {
    has_humanity: true,
    transformation_possible: false,
    human_moments: ["对过去的回忆", "对某人的特殊情感"]
  }
});
```

**设计要点**：
1. **动机合理**：反派有自己的逻辑和信念
2. **能力匹配**：威胁程度与主角成长匹配
3. **冲突清晰**：与主角的冲突本质明确
4. **有人性**：展现人性一面，增加深度
5. **有弱点**：设计合理的弱点

---

### 应用场景四：关系网络构建

**场景描述**：构建完整的人物关系网络。

**操作步骤**：

```javascript
// 构建关系网络
const network = await character-designer.build_relationships({
  characters: [
    protagonist,
    mentor,
    ally,
    rival,
    antagonist
  ],
  relationships: [
    {
      from: "林风",
      to: "玄老",
      type: "mentor",
      strength: 9,
      development: "师徒情深"
    },
    {
      from: "林风",
      to: "苏晴",
      type: "ally",
      strength: 7,
      development: "逐渐升温"
    },
    {
      from: "林风",
      to: "赵天",
      type: "rival",
      strength: 6,
      development: "竞争到认可"
    },
    {
      from: "林风",
      to: "魔尊",
      type: "enemy",
      strength: 10,
      development: "最终决战"
    }
  ]
});

// 检查关系网络完整性
const networkCheck = checkRelationshipNetwork(network);
```

**设计要点**：
1. **关系清晰**：每对关系都有明确类型
2. **强度合理**：关系强度与情节匹配
3. **有发展**：关系有发展轨迹
4. **张力充足**：关系网络有足够张力

---

## 📊 技能掌握评估标准

### 评估维度

| 维度 | 初级 | 中级 | 高级 |
|------|------|------|------|
| 主角设计 | 能设计基础主角 | 能设计代入感强的主角 | 能设计有深度的主角 |
| 配角设计 | 能设计基础配角 | 能设计功能性配角 | 能设计有魅力的配角 |
| 反派设计 | 能设计基础反派 | 能设计有动机的反派 | 能设计有深度的反派 |
| 关系设计 | 能设计基础关系 | 能设计关系发展 | 能设计有张力的关系网络 |
| 一致性 | 能发现明显问题 | 能保持基本一致 | 能完美保持一致 |

### 评估指标

```json
{
  "character_design": {
    "protagonist": {
      "empathy_score": "≥8分",
      "depth_score": "≥7分",
      "arc_completeness": "≥80%"
    },
    "supporting": {
      "functionality": "明确",
      "memorability": "≥7分"
    },
    "antagonist": {
      "motivation_rationality": "≥8分",
      "depth_score": "≥7分",
      "threat_degree": "匹配主角成长"
    },
    "relationship": {
      "clarity": "清晰",
      "tension": "≥7分",
      "development": "有轨迹"
    }
  }
}
```

### 评估方法

1. **代入感测试**：测试读者对主角的代入程度
2. **记忆度测试**：测试读者对人物的记忆程度
3. **一致性检查**：检查人物行为前后一致
4. **关系张力评估**：评估关系网络的戏剧张力

---

## 🎯 阶段成果交付物

完成本阶段后，应产出以下交付物：

### 1. 主角人物档案
- 基础信息
- 性格体系
- 背景故事
- 能力体系
- 动机体系
- 人物弧光
- 代入感设计

### 2. 配角人物档案
- 核心配角档案（3-5个）
- 功能定位
- 与主角关系

### 3. 反派人物档案
- 基础信息
- 动机体系
- 能力体系
- 与主角冲突

### 4. 人物关系网络图
- 所有人物
- 关系类型
- 关系强度
- 发展轨迹

---

## ⚠️ 常见问题与解决

### 问题1：主角代入感弱
**表现**：读者难以代入主角，缺乏情感连接  
**解决**：
- 强化共情点设计
- 优化开篇代入建立
- 增加主角魅力展现

### 问题2：人物扁平化
**表现**：人物性格单一，脸谱化严重  
**解决**：
- 增加性格维度
- 设计性格矛盾点
- 完善背景故事

### 问题3：人物行为不一致
**表现**：人物行为前后矛盾  
**解决**：
- 建立人物行为准则
- 定期一致性检查
- 使用character-designer.check_consistency()

---

## 🚀 进入下一阶段

完成本阶段学习并通过评估后，可进入：

**[阶段三：情节架构设计](./phase-3-plot.md)**

**前置条件检查**：
- [ ] 完成主角设计
- [ ] 完成核心配角设计
- [ ] 完成反派设计
- [ ] 构建人物关系网络
- [ ] 通过人物质量评估
- [ ] 通过阶段二评估

---

**阶段二学习完成标志**：能够独立设计立体的人物体系，建立有张力的人物关系网络，并保持人物行为一致性。

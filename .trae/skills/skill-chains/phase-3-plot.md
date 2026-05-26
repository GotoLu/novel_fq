# 阶段三：情节架构设计

## 🎯 阶段目标

掌握情节架构方法，构建完整世界观，设计伏笔体系，为内容创作提供完整蓝图。

**核心能力**：
- 结构设计能力
- 世界观构建能力
- 大纲创建能力
- 伏笔体系设计能力
- 情节逻辑把控能力

**学习周期**：2-3周

**前置依赖**：阶段一、阶段二

---

## 🔗 Skill链结构

```
┌─────────────────────────────────────────────────────────────┐
│                    阶段三 Skill链                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   character-designer ──→ plot-architect                    │
│          │                     │                           │
│          │                     │                           │
│          ↓                     ↓                           │
│   人物信息              结构设计                              │
│   关系网络              世界观构建                            │
│                         大纲创建                              │
│                         伏笔体系                              │
│                         逻辑检查                              │
│                              │                              │
│                              ↓                              │
│                      quality-evaluator                      │
│                      (情节维度评估)                          │
│                              │                              │
│                              ↓                              │
│                      progress-tracker                       │
│                      (节点检验)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 技能组件详解

### 1. plot-architect（情节架构）

#### 功能定位
情节架构是故事骨架，决定故事的吸引力和可读性。

#### 核心功能
| 功能 | 说明 | 输出成果 |
|------|------|---------|
| 结构设计 | 设计故事整体结构 | 结构设计文档 |
| 世界观构建 | 构建完整世界观 | 世界观文档 |
| 大纲创建 | 创建分卷/分章大纲 | 大纲文档 |
| 伏笔设计 | 设计伏笔体系 | 伏笔清单 |
| 逻辑检查 | 检查情节逻辑 | 逻辑检查报告 |

#### 学习目标
- [ ] 掌握三幕式/四幕式结构
- [ ] 能够构建完整世界观
- [ ] 能够创建分卷和分章大纲
- [ ] 能够设计伏笔体系
- [ ] 能够保持情节逻辑一致

---

## 🔄 技能衔接关系

### 调用流程

```
1. 获取人物信息（来自阶段二）
   character-designer.get_characters()
   character-designer.get_relationships()
         ↓
2. 设计故事结构
   plot-architect.design_structure({
     structure_type: "three_act",
     total_words: 1000000
   })
         ↓
3. 构建世界观
   plot-architect.build_world({
     type: "fantasy",
     core_settings: {...}
   })
         ↓
4. 创建分卷大纲
   plot-architect.create_outline({
     outline_level: "volume"
   })
         ↓
5. 创建分章大纲
   plot-architect.create_outline({
     outline_level: "chapter"
   })
         ↓
6. 设计伏笔体系
   plot-architect.design_foreshadowing()
         ↓
7. 情节质量评估
   quality-evaluator.evaluate_dimension({
     dimension: "plot_quality"
   })
         ↓
8. 逻辑检查
   plot-architect.check_plot_logic()
         ↓
9. 节点检验
   progress-tracker.check_node("node_007", "node_008", "node_009")
```

---

## 📖 技能应用指南

### 应用场景一：结构设计

```javascript
// 设计三幕式结构
const structure = await plot-architect.design_structure({
  structure_type: "three_act",
  total_words: 1000000,
  climax_distribution: {
    first_act_climax: { chapter: 25, intensity: 7 },
    midpoint: { chapter: 50, intensity: 8 },
    second_act_climax: { chapter: 75, intensity: 9 },
    final_climax: { chapter: 100, intensity: 10 }
  }
});
```

### 应用场景二：世界观构建

```javascript
// 构建玄幻世界观
const world = await plot-architect.build_world({
  type: "fantasy",
  core_settings: {
    time_space: "修仙世界，多个位面",
    power_system: {
      levels: ["炼气", "筑基", "金丹", "元婴", "化神", "渡劫"],
      advancement: "修炼+机缘"
    },
    rules: [
      "修为越高，寿命越长",
      "渡劫成功飞升上界"
    ]
  },
  social_structure: {
    forces: [
      { name: "正道联盟", type: "正义" },
      { name: "魔道", type: "邪恶" },
      { name: "散修联盟", type: "中立" }
    ],
    hierarchy: "修为决定地位"
  }
});
```

### 应用场景三：大纲创建

```javascript
// 创建分卷大纲
const volumeOutline = await plot-architect.create_outline({
  outline_level: "volume",
  volumes: [
    {
      name: "第一卷：觉醒",
      theme: "主角获得金手指，开始修炼之路",
      word_count: 200000,
      core_events: ["获得金手指", "初次战斗", "加入宗门"]
    },
    {
      name: "第二卷：成长",
      theme: "主角快速成长，遭遇重大挫折",
      word_count: 200000,
      core_events: ["宗门大比", "秘境探险", "重大挫折"]
    }
  ]
});

// 创建分章大纲
const chapterOutline = await plot-architect.create_outline({
  outline_level: "chapter",
  volume_id: 1,
  chapters: [
    {
      title: "第一章 觉醒",
      core_event: "主角获得吞噬星空的能力",
      conflict: "家族压迫vs主角反抗",
      cliffhanger: "能力初显，引起注意"
    }
  ]
});
```

### 应用场景四：伏笔体系设计

```javascript
// 设计伏笔体系
const foreshadowing = await plot-architect.design_foreshadowing({
  foreshadowings: [
    {
      content: "主角身世之谜",
      plant_chapter: 5,
      hints: [15, 30, 50],
      reveal_chapter: 80,
      importance: "high"
    },
    {
      content: "金手指的真正来源",
      plant_chapter: 10,
      hints: [40, 60],
      reveal_chapter: 100,
      importance: "high"
    }
  ]
});
```

---

## 📊 技能掌握评估标准

### 评估指标

```json
{
  "plot_architecture": {
    "structure": {
      "completeness": "≥90%",
      "climax_distribution": "合理"
    },
    "world_building": {
      "consistency": "≥90%",
      "depth": "≥8分"
    },
    "outline": {
      "detail_level": "分章级别",
      "event_coverage": "≥95%"
    },
    "foreshadowing": {
      "coverage": "主要情节都有伏笔",
      "recycle_rate": "≥90%"
    },
    "logic": {
      "consistency": "≥95%"
    }
  }
}
```

---

## 🎯 阶段成果交付物

1. **结构设计文档**
2. **世界观文档**
3. **分卷大纲**
4. **分章大纲**
5. **伏笔清单**

---

## 🚀 进入下一阶段

**[阶段四：内容创作执行](./phase-4-content.md)**

**前置条件检查**：
- [ ] 完成结构设计
- [ ] 完成世界观构建
- [ ] 完成分卷和分章大纲
- [ ] 完成伏笔体系设计
- [ ] 通过情节质量评估

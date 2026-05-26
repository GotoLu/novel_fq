# 阶段四：内容创作执行

## 🎯 阶段目标

掌握正文写作技巧，保持稳定创作节奏，持续产出高质量内容。

**核心能力**：
- 开篇创作能力
- 章节写作能力
- 高潮创作能力
- 节奏控制能力
- 问题解决能力
- 质量把控能力

**学习周期**：持续进行

**前置依赖**：阶段一、二、三

---

## 🔗 Skill链结构

```
┌─────────────────────────────────────────────────────────────┐
│                    阶段四 Skill链                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   plot-architect ────→ content-writer                      │
│         │                     │                            │
│         │                     │                            │
│         ↓                     ↓                            │
│   大纲信息              开篇写作                              │
│   世界观                章节写作                              │
│                         高潮写作                              │
│                         节奏控制                              │
│                              │                              │
│                              ↓                              │
│                        problem-solver                       │
│                        (问题诊断解决)                        │
│                              │                              │
│                              ↓                              │
│                      quality-evaluator                      │
│                      (质量评估)                              │
│                              │                              │
│                              ↓                              │
│                      progress-tracker                       │
│                      (进度跟踪)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 技能组件详解

### 1. content-writer（内容创作）

#### 核心功能
| 功能 | 说明 | 输出成果 |
|------|------|---------|
| 开篇写作 | 写黄金三章 | 开篇内容 |
| 章节写作 | 写日常章节 | 章节内容 |
| 高潮写作 | 写关键段落 | 高潮内容 |
| 节奏控制 | 控制叙事节奏 | 节奏分析 |

#### 学习目标
- [ ] 掌握黄金三章写作技巧
- [ ] 能够稳定产出章节内容
- [ ] 能够创作高质量高潮段落
- [ ] 能够控制叙事节奏

---

### 2. problem-solver（问题解决）

#### 核心功能
| 功能 | 说明 | 输出成果 |
|------|------|---------|
| 问题诊断 | 识别问题根本原因 | 诊断报告 |
| 问题解决 | 提供解决方案 | 解决方案 |
| 问题预防 | 提供预防措施 | 预防清单 |

---

## 🔄 技能衔接关系

### 调用流程

```
1. 获取大纲信息（来自阶段三）
   plot-architect.get_outline()
         ↓
2. 写开篇（黄金三章）
   content-writer.write_opening({
     word_count_target: 10000
   })
         ↓
3. 质量检查
   quality-evaluator.evaluate_chapter({
     chapter_range: { start: 1, end: 3 }
   })
         ↓
4. 节点检验
   progress-tracker.check_node("node_010")
         ↓
5. 持续章节写作
   loop:
     content-writer.write_chapter()
     → quality-evaluator.evaluate_chapter()
     → progress-tracker.update_progress()
     
     if (遇到问题):
       problem-solver.diagnose_problem()
       problem-solver.solve_problem()
         ↓
6. 高潮写作
   content-writer.write_climax()
         ↓
7. 节点检验
   progress-tracker.check_node("node_011", "node_012")
```

---

## 📖 技能应用指南

### 应用场景一：开篇创作（黄金三章）

```javascript
// 写黄金三章
const opening = await content-writer.write_opening({
  word_count_target: 10000,
  outline_data: {
    chapter1: {
      core_event: "主角出场，展示现状",
      empathy_points: ["受欺压", "有志气"],
      cliffhanger: "意外发生"
    },
    chapter2: {
      core_event: "获得金手指",
      conflict: "机遇vs危机",
      cliffhanger: "能力初显"
    },
    chapter3: {
      core_event: "首次使用能力",
      conflict: "主角vs敌人",
      cliffhanger: "强悬念"
    }
  }
});

// 检查开篇质量
const openingQuality = await quality-evaluator.evaluate_chapter({
  chapter_range: { start: 1, end: 3 },
  focus: "opening_impact"
});
```

### 应用场景二：日常章节写作

```javascript
// 写单章
const chapter = await content-writer.write_chapter({
  chapter_number: 50,
  chapter_title: "第五十章 突破",
  word_count_target: 3000,
  outline_data: {
    core_event: "主角突破境界",
    conflict: "突破困难vs坚持",
    characters: ["林风", "玄老"],
    foreshadowing: ["暗示身世"],
    cliffhanger: "突破成功，引来注意"
  }
});

// 质量检查
const quality = await quality-writer.check_quality({
  chapter_number: 50,
  quality_check_level: "standard"
});

// 更新进度
await progress-tracker.update_progress({
  current_chapter: 50,
  words_written: chapter.word_count
});
```

### 应用场景三：问题诊断解决

```javascript
// 遇到写作问题
const diagnosis = await problem-solver.diagnose_problem({
  problem_type: "plot_stuck",
  problem_description: "写到第50章，不知道怎么继续推进了",
  context: {
    current_chapter: 50,
    recent_content: "..."
  }
});

// 获取解决方案
const solution = await problem-solver.solve_problem({
  diagnosis_result: diagnosis,
  solution_preference: "moderate"
});

// 实施解决方案
// 根据solution.steps实施
```

---

## 📊 技能掌握评估标准

### 评估指标

```json
{
  "content_writing": {
    "opening": {
      "empathy_strength": "≥8分",
      "hook_strength": "≥8分",
      "reader_retention": "≥70%"
    },
    "chapter": {
      "quality_stability": "≥7分",
      "progression_clarity": "明确",
      "word_count_consistency": "±10%"
    },
    "climax": {
      "intensity": "≥8分",
      "emotional_impact": "≥8分"
    },
    "pacing": {
      "balance": "张弛有度",
      "information_density": "适中"
    }
  }
}
```

---

## 🎯 阶段成果交付物

1. **黄金三章**（前三章）
2. **日常章节内容**（持续产出）
3. **高潮段落**（关键节点）
4. **质量检查报告**
5. **进度记录**

---

## 🚀 进入下一阶段

**[阶段五：系统整合与优化](./phase-5-integration.md)**

**前置条件检查**：
- [ ] 完成黄金三章
- [ ] 建立稳定创作节奏
- [ ] 能够独立解决创作问题
- [ ] 能够保持质量稳定

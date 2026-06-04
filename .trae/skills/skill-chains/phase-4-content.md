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
│   plot-architect ────→ character-designer ────→ content-writer│
│         │                     │                     │        │
│         ↓                     ↓                     ↓        │
│   大纲/章节卡           人物状态校验             开篇/章节/高潮 │
│                                                     节奏控制   │
│                                                         │     │
│                                                         ↓     │
│                      quality-evaluator ←── problem-solver     │
│                      (质量评估)          (问题诊断解决)        │
│                              │                              │
│                              ↓                              │
│                    plagiarism-checker                       │
│                    (原创性风险审查)                          │
│                              │                              │
│                              ↓                              │
│                      progress-tracker                       │
│                      (进度跟踪/差异记录)                      │
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

### 3. 单章生产闭环（吸收章节流程规范）

本闭环用于阶段四的日常章节生产。它不是新增独立 skill，而是 `skill-chains` 对现有技能的编排规则；正文仍由 `content-writer` 负责，大纲和章节卡仍由 `plot-architect` 负责，人物一致性仍由 `character-designer` 校验。

#### 执行顺序

```
1. 大纲核查
   ├─ 检查章节级详细大纲是否存在
   ├─ 检查卷级细纲是否包含该章设计
   ├─ 检查总大纲是否包含该章核心事件
   └─ 判定：完整 / 部分完整 / 基础 / 缺失
        ↓
2. 章节卡补全
   plot-architect 补齐核心事件、场景划分、伏笔、章末钩子、字数分配
        ↓
3. 人物状态校验
   character-designer 校验出场人物的动机、关系、能力边界和前文状态
        ↓
4. 正文三稿
   content-writer 执行初稿 → 修改稿 → 终稿
        ↓
5. 质量闸门
   quality-evaluator 检查推进、钩子、节奏、人物一致性、语言质量
        ↓
6. 原创性闸门
   plagiarism-checker 检查正文、关键场景、对话和桥段撞车风险
        ↓
7. 问题回退
   未通过时由 problem-solver 分诊，再回退到对应生产技能重做
        ↓
8. 差异审计与记录
   progress-tracker 记录进度、质量结论、原创性结论、正文与大纲差异
```

#### 大纲核查判定

| 核查结果 | 判定 | 后续动作 |
|---------|------|---------|
| 章节级详细大纲存在且可执行 | 完整 | 进入人物状态校验和正文三稿 |
| 只有卷级细纲或章节设计粗略 | 部分完整 | 由 `plot-architect` 补章节卡 |
| 只有总大纲核心事件 | 基础 | 由 `plot-architect` 生成章节级详细大纲 |
| 总大纲也缺少该章事件 | 缺失 | 暂停正文写作，回到阶段三补大纲 |

#### 章节卡最低字段

| 字段 | 要求 |
|------|------|
| 章节编号与标题 | 标题需暗示核心事件，不应过度剧透 |
| 核心事件 | 用一句话说明本章不可替代的推进作用 |
| 场景划分 | 标明每个场景的功能、冲突、字数和承接关系 |
| 出场人物 | 标明人物状态、动机、关系变化和能力边界 |
| 伏笔与回收 | 标明伏笔 ID、出现位置、后续影响 |
| 章末钩子 | 必须指向下一章的明确问题、危机或期待 |
| 质量标准 | 明确本章的追读、节奏、幽默、情绪或爽点重点 |

#### 差异审计规则

终稿完成后，不直接用正文覆盖大纲。必须先做差异审计：

| 偏差类型 | 处理方式 |
|---------|---------|
| 标题、场景顺序、字数分配等低风险偏差 | 可同步到章节级大纲，并记录依据 |
| 对话、幽默点、环境描写等表达层偏差 | 可同步到章节级大纲或创作报告 |
| 伏笔增减、人物行为变化、案件逻辑变化 | 必须经 `quality-evaluator` 判断影响 |
| 与总大纲核心事件、人物底层设定冲突 | 不自动同步，交由 `problem-solver` 分诊并记录待决策项 |

差异记录至少包含：偏差项、正文版本、大纲版本、影响级别、处理动作、决策依据。

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
     plot-architect.check_or_build_chapter_card()
     → character-designer.check_character_state()
     → content-writer.write_chapter()
     → quality-evaluator.evaluate_chapter()
     → plagiarism-checker.check_originality()
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
// 1. 核查并补齐章节卡
const chapterCard = await plot-architect.check_or_build_chapter_card({
  chapter_number: 50,
  sources: {
    chapter_outline: "novel-project/第50章详细大纲.md",
    volume_outline: "novel-project/第二卷详细细纲.md",
    master_outline: "novel-project/大纲.md"
  }
});

// 2. 校验人物状态
const characterState = await character-designer.check_character_state({
  chapter_number: 50,
  characters: chapterCard.characters,
  previous_context_range: { chapters: 2 }
});

// 3. 写单章
const chapter = await content-writer.write_chapter({
  chapter_number: 50,
  chapter_title: "第五十章 突破",
  word_count_target: 3000,
  outline_data: chapterCard,
  character_state: characterState
});

// 4. 质量检查
const quality = await quality-evaluator.evaluate_chapter({
  chapter_number: 50,
  quality_check_level: "strict"
});

// 5. 原创性风险审查
const originality = await plagiarism-checker.check_originality({
  chapter_number: 50,
  content_type: "content"
});

// 6. 差异审计与进度记录
await progress-tracker.update_progress({
  current_chapter: 50,
  words_written: chapter.word_count,
  quality_result: quality,
  originality_result: originality,
  outline_diff: chapter.diff_with_outline
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
5. **原创性风险结论**
6. **正文与大纲差异记录**
7. **进度记录**

---

## 🚀 进入下一阶段

**[阶段五：系统整合与优化](./phase-5-integration.md)**

**前置条件检查**：
- [ ] 完成黄金三章
- [ ] 建立稳定创作节奏
- [ ] 能够独立解决创作问题
- [ ] 能够保持质量稳定
- [ ] 建立单章生产闭环
- [ ] 正文、大纲、伏笔和进度记录保持可追溯

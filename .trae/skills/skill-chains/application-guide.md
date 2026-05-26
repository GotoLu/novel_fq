# 技能应用指南

## 📖 指南概述

本指南详细说明每个skill链在小说创作过程中的具体使用方法、适用场景和预期效果。

---

## 🎯 阶段一应用指南：市场洞察与创意孵化

### 适用场景

| 场景 | 说明 | 使用时机 |
|------|------|---------|
| 新项目启动 | 开始新的小说项目 | 项目初期 |
| 定位调整 | 根据市场变化调整定位 | 市场环境变化时 |
| 创意枯竭 | 需要新的创意灵感 | 创作瓶颈时 |
| 竞品研究 | 学习成功作品经验 | 项目准备期 |

### 使用方法

#### 场景一：新项目完整流程

```javascript
// 步骤1: 平台分析
const platforms = await market-analyzer.analyze_platform({
  platforms: ["起点", "晋江", "番茄", "纵横", "飞卢"],
  analysis_depth: "comprehensive"
});

// 预期效果：获得各平台的用户画像、题材分布、收益模式

// 步骤2: 题材分析
const genre = await market-analyzer.analyze_genre({
  genre: "玄幻",
  platforms: platforms.recommended
});

// 预期效果：了解题材市场容量、竞争强度、发展趋势

// 步骤3: 竞品分析
const competitors = await market-analyzer.analyze_competitors({
  competitor_works: ["《诡秘之主》", "《大奉打更人》", "《道诡异仙》"],
  analysis_focus: ["核心卖点", "成功要素", "读者反馈"]
});

// 预期效果：提炼成功作品的核心要素和可借鉴经验

// 步骤4: 定位建议
const positioning = await market-analyzer.generate_positioning({
  genre: genre,
  competitors: competitors,
  target_readers: {
    age_range: "18-35",
    gender: "male",
    preferences: ["爽文", "升级流", "热血"]
  }
});

// 预期效果：获得明确的平台选择、题材定位和差异化策略

// 步骤5: 创意生成
const ideas = await idea-generator.generate_ideas({
  genre: positioning.recommended_genre,
  technique: "combination",
  idea_count: 15
});

// 预期效果：获得15个初步创意

// 步骤6: 创意筛选
const filtered = await idea-generator.filter_ideas({
  ideas: ideas,
  criteria: {
    novelty_threshold: 7,
    extensibility_threshold: 8,
    market_match_threshold: 70
  }
});

// 预期效果：筛选出3-5个优质创意

// 步骤7: 创意验证
const validated = await idea-generator.validate_idea({
  target_idea: filtered.top_idea
});

// 预期效果：验证创意可行性，识别风险

// 步骤8: 高概念创建
const highConcept = await idea-generator.create_high_concept({
  validated_idea: validated.idea
});

// 预期效果：获得简洁有力的高概念
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 平台选择准确度 | ≥85% | 选择最适合的平台 |
| 题材定位精准度 | ≥80% | 定位符合市场需求 |
| 创意新颖度 | ≥7分 | 创意有足够新意 |
| 创意延展性 | ≥8分 | 创意可支撑长篇 |
| 高概念清晰度 | 一句话能说清 | 概念简洁易懂 |

---

## 🎯 阶段二应用指南：人物体系构建

### 适用场景

| 场景 | 说明 | 使用时机 |
|------|------|---------|
| 主角设计 | 设计核心主角 | 创意确定后 |
| 配角设计 | 设计功能性配角 | 主角设计后 |
| 反派设计 | 设计主要反派 | 主角设计后 |
| 关系构建 | 建立人物关系网络 | 主要人物设计后 |
| 一致性检查 | 检查人物行为一致性 | 创作过程中 |

### 使用方法

#### 场景一：完整人物体系构建

```javascript
// 步骤1: 主角设计
const protagonist = await character-designer.design_protagonist({
  character_data: {
    name: "林风",
    age: 18,
    gender: "male",
    personality_traits: ["勇敢", "聪明", "重情义", "有些固执"],
    background: "小家族庶子，母亲早亡，受尽冷眼"
  }
});

// 补充设计
protagonist.abilities = {
  initial: "普通修为",
  golden_finger: "吞噬星空的能力",
  growth_path: "觉醒→成长→质变"
};

protagonist.motivation = {
  external_goal: "成为强者，保护在乎的人",
  internal_need: "证明自己，获得认可",
  core_fear: "失去在乎的人"
};

protagonist.arc = {
  start_state: "受尽冷眼的庶子",
  growth_trajectory: "获得能力→遭遇挫折→成长蜕变",
  end_state: "成为强者"
};

// 预期效果：获得完整的主角档案

// 步骤2: 配角设计
const mentor = await character-designer.design_supporting({
  character_data: { name: "玄老", role: "mentor", ... }
});

const ally = await character-designer.design_supporting({
  character_data: { name: "苏晴", role: "ally", ... }
});

const rival = await character-designer.design_supporting({
  character_data: { name: "赵天", role: "rival", ... }
});

// 预期效果：获得功能性配角档案

// 步骤3: 反派设计
const antagonist = await character-designer.design_antagonist({
  character_data: {
    name: "魔尊",
    motivation: { surface: "统治世界", deep: "向世界复仇" },
    abilities: { power_level: "极高", weakness: "内心执念" }
  }
});

// 预期效果：获得有深度的反派档案

// 步骤4: 关系网络构建
const network = await character-designer.build_relationships({
  characters: [protagonist, mentor, ally, rival, antagonist],
  relationships: [
    { from: "林风", to: "玄老", type: "mentor", strength: 9 },
    { from: "林风", to: "苏晴", type: "ally", strength: 7 },
    { from: "林风", to: "魔尊", type: "enemy", strength: 10 }
  ]
});

// 预期效果：获得完整的人物关系网络

// 步骤5: 质量评估
const quality = await quality-evaluator.evaluate_dimension({
  dimension: "character_depth",
  characters: [protagonist, mentor, ally, rival, antagonist]
});

// 预期效果：获得人物质量评估报告
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 主角代入感 | ≥8分 | 读者能代入主角 |
| 人物深度 | ≥7分 | 人物立体有深度 |
| 关系张力 | ≥7分 | 关系网络有戏剧张力 |
| 一致性 | ≥90% | 人物行为前后一致 |

---

## 🎯 阶段三应用指南：情节架构设计

### 适用场景

| 场景 | 说明 | 使用时机 |
|------|------|---------|
| 结构设计 | 设计故事整体结构 | 人物设计后 |
| 世界观构建 | 构建完整世界观 | 结构设计后 |
| 大纲创建 | 创建分卷/分章大纲 | 世界观构建后 |
| 伏笔设计 | 设计伏笔体系 | 大纲创建后 |
| 逻辑检查 | 检查情节逻辑 | 大纲创建后/创作中 |

### 使用方法

```javascript
// 步骤1: 结构设计
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

// 预期效果：获得完整的故事结构设计

// 步骤2: 世界观构建
const world = await plot-architect.build_world({
  type: "fantasy",
  core_settings: {
    power_system: { levels: [...], advancement: "..." },
    rules: [...],
    forces: [...]
  }
});

// 预期效果：获得完整的世界观设定

// 步骤3: 大纲创建
const outline = await plot-architect.create_outline({
  outline_level: "chapter",
  structure: structure,
  world: world
});

// 预期效果：获得分卷和分章大纲

// 步骤4: 伏笔设计
const foreshadowing = await plot-architect.design_foreshadowing({
  outline: outline,
  major_plots: ["身世之谜", "金手指来源", "最终敌人"]
});

// 预期效果：获得伏笔体系

// 步骤5: 逻辑检查
const logic = await plot-architect.check_plot_logic({
  outline: outline,
  world: world
});

// 预期效果：识别逻辑问题
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 结构完整性 | ≥90% | 结构完整合理 |
| 世界观自洽性 | ≥90% | 设定前后一致 |
| 大纲详细度 | 分章级别 | 大纲足够详细 |
| 伏笔覆盖率 | 主要情节都有 | 重要情节有伏笔 |
| 逻辑一致性 | ≥95% | 情节逻辑通顺 |

---

## 🎯 阶段四应用指南：内容创作执行

### 适用场景

| 场景 | 说明 | 使用时机 |
|------|------|---------|
| 开篇创作 | 写黄金三章 | 大纲完成后 |
| 日常写作 | 写日常章节 | 持续进行 |
| 高潮创作 | 写关键段落 | 到达高潮节点 |
| 问题解决 | 解决创作问题 | 遇到问题时 |
| 质量检查 | 检查内容质量 | 每章完成后 |

### 使用方法

#### 场景一：开篇创作（黄金三章）

```javascript
// 黄金三章创作
const opening = await content-writer.write_opening({
  word_count_target: 10000,
  outline_data: {
    chapter1: {
      title: "第一章 觉醒",
      core_event: "主角出场，展示现状",
      empathy_points: ["受欺压", "有志气"],
      cliffhanger: "意外发生"
    },
    chapter2: {
      title: "第二章 机缘",
      core_event: "获得金手指",
      cliffhanger: "能力初显"
    },
    chapter3: {
      title: "第三章 初战",
      core_event: "首次使用能力",
      cliffhanger: "强悬念"
    }
  }
});

// 质量检查
const quality = await quality-evaluator.evaluate_chapter({
  chapter_range: { start: 1, end: 3 },
  focus: "opening_impact"
});

// 如果质量不达标，进行优化
if (quality.score < 8) {
  const diagnosis = await problem-solver.diagnose_problem({
    problem_type: "opening_fail",
    context: { chapters: opening }
  });
  
  const solution = await problem-solver.solve_problem({
    diagnosis_result: diagnosis
  });
  
  // 实施优化
}

// 预期效果：获得高质量的黄金三章
```

#### 场景二：日常创作流程

```javascript
// 每日创作循环
async function dailyWriting() {
  // 1. 获取进度
  const progress = await progress-tracker.get_statistics();
  
  // 2. 确定今日目标
  const todayTarget = {
    chapters: 2,
    words_per_chapter: 3000
  };
  
  // 3. 创作循环
  for (let i = 0; i < todayTarget.chapters; i++) {
    // 写章节
    const chapter = await content-writer.write_chapter({
      chapter_number: progress.current_chapter + i + 1,
      word_count_target: todayTarget.words_per_chapter,
      outline_data: getOutlineData(progress.current_chapter + i + 1)
    });
    
    // 质量检查
    const quality = await content-writer.check_quality({
      chapter_number: chapter.number,
      quality_check_level: "standard"
    });
    
    // 如果有问题，解决
    if (quality.issues.length > 0) {
      const solution = await problem-solver.solve_problem({
        problem_type: quality.issues[0].type,
        problem_description: quality.issues[0].description
      });
      // 实施解决方案
    }
    
    // 更新进度
    await progress-tracker.update_progress({
      current_chapter: chapter.number,
      words_written: chapter.word_count
    });
  }
  
  // 4. 生成日报
  const report = await progress-tracker.generate_report({
    report_type: "daily"
  });
  
  return report;
}
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 开篇代入感 | ≥8分 | 前三章建立强代入感 |
| 章节质量稳定性 | ≥7分 | 质量稳定不波动 |
| 日均产出 | ≥5000字 | 保持稳定产出 |
| 问题解决率 | ≥90% | 问题能及时解决 |

---

## 🎯 阶段五应用指南：系统整合与优化

### 适用场景

| 场景 | 说明 | 使用时机 |
|------|------|---------|
| 全流程整合 | 整合所有技能 | 项目全流程 |
| 阶段评估 | 阶段性质量评估 | 每10-20章 |
| 最终审查 | 完稿前最终检查 | 完稿前 |
| 发布准备 | 准备发布材料 | 完稿后 |

### 使用方法

#### 场景一：阶段性评估优化

```javascript
// 每20章进行一次全面评估
async function stageEvaluation(chapterEnd) {
  // 1. 全面质量评估
  const evaluation = await quality-evaluator.evaluate_full({
    chapter_range: { start: chapterEnd - 19, end: chapterEnd },
    evaluation_level: "comprehensive"
  });
  
  // 2. 识别问题
  const issues = evaluation.weaknesses;
  
  // 3. 制定优化计划
  for (const issue of issues) {
    const solution = await problem-solver.solve_problem({
      problem_type: issue.type,
      problem_description: issue.description,
      solution_preference: "moderate"
    });
    
    // 实施解决方案
    await implementSolution(solution);
  }
  
  // 4. 重新评估
  const reEvaluation = await quality-evaluator.evaluate_full({
    chapter_range: { start: chapterEnd - 19, end: chapterEnd }
  });
  
  // 5. 记录改进
  await progress-tracker.update_progress({
    quality_improvement: reEvaluation.score - evaluation.score
  });
}
```

#### 场景二：完稿流程

```javascript
// 完稿最终流程
async function completionFlow() {
  // 1. 最终全面评估
  const finalEval = await quality-evaluator.evaluate_full({
    evaluation_level: "comprehensive"
  });
  
  // 2. 检查伏笔回收
  const foreshadowingCheck = await plot-architect.check_foreshadowing();
  
  // 3. 检查人物一致性
  const consistencyCheck = await character-designer.check_consistency({
    start_chapter: 1,
    end_chapter: totalChapters
  });
  
  // 4. 检查情节逻辑
  const logicCheck = await plot-architect.check_plot_logic({
    start_chapter: 1,
    end_chapter: totalChapters
  });
  
  // 5. 汇总所有问题
  const allIssues = [
    ...finalEval.weaknesses,
    ...foreshadowingCheck.issues,
    ...consistencyCheck.issues,
    ...logicCheck.issues
  ];
  
  // 6. 解决所有问题
  for (const issue of allIssues) {
    await problem-solver.solve_problem({
      problem_type: issue.type,
      problem_description: issue.description
    });
  }
  
  // 7. 生成最终报告
  const report = await quality-evaluator.generate_report({
    report_type: "full"
  });
  
  // 8. 标记完成
  await progress-tracker.check_node("node_013", "node_014", "node_015");
  
  return report;
}
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 整体质量 | ≥80分 | 作品整体质量达标 |
| 伏笔回收率 | 100% | 所有伏笔都回收 |
| 一致性 | ≥95% | 人物行为一致 |
| 逻辑性 | ≥95% | 情节逻辑通顺 |

---

## 📋 最佳实践总结

### 1. 循序渐进
- 按阶段顺序学习应用
- 每个阶段充分掌握后再进入下一阶段

### 2. 实践结合
- 理论学习与实际创作结合
- 每个技能都要在实际项目中练习

### 3. 持续评估
- 定期使用quality-evaluator评估
- 根据评估结果持续优化

### 4. 问题导向
- 遇到问题及时使用problem-solver
- 不拖延问题，及时解决

### 5. 进度管控
- 使用progress-tracker全程跟踪
- 确保关键节点质量达标

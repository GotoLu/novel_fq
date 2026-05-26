# 技能应用指南（含查重校验）

## 📖 指南概述

本指南详细说明每个skill链在小说创作过程中的具体使用方法、适用场景和预期效果。

**重要更新**：每个技能环节执行后，现在会自动进行**查重校验**，确保输出内容的原创性。

---

## 🔍 查重校验流程

### 执行流程图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Skill执行流程（含查重校验）                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. 执行Skill → 生成输出内容                                                 │
│      ↓                                                                      │
│  2. 查重校验 → 计算重复度分数（0-100分）                                      │
│      ↓                                                                      │
│  3. 阈值判断 → 分数 ≤ 阈值？                                                 │
│      │                                                                      │
│      ├─→ 是 → 通过校验 → 进入下一环节                                        │
│      │                                                                      │
│      └─→ 否 → 触发回炉重造                                                  │
│              ↓                                                              │
│         4. 记录当前结果                                                      │
│              ↓                                                              │
│         5. 生成重造指令                                                      │
│              ↓                                                              │
│         6. 重新执行Skill                                                    │
│              ↓                                                              │
│         7. 再次查重校验                                                      │
│              ↓                                                              │
│         8. 循环直至达标或达到最大重试次数                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 查重校验参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| max_attempts | 3 | 最大重试次数 |
| threshold | 30 | 默认重复度阈值 |
| algorithm_weights | 见配置 | 算法权重配置 |

### 阈值配置

| 内容类型 | 阈值 | 说明 |
|---------|------|------|
| idea | 40 | 创意方案 |
| character | 35 | 人物设计 |
| plot | 30 | 情节架构 |
| content | 25 | 正文内容 |
| dialogue | 45 | 对话内容 |

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

```python
from plagiarism_checker import create_checker

# 初始化查重校验器
checker = create_checker(max_attempts=3, log_dir='./logs/plagiarism/')

# 步骤1: 平台分析
platforms = await market_analyzer.analyze_platform({
    "platforms": ["起点", "晋江", "番茄", "纵横", "飞卢"],
    "analysis_depth": "comprehensive"
})

# 步骤2: 题材分析
genre = await market_analyzer.analyze_genre({
    "genre": "玄幻",
    "platforms": platforms.recommended
})

# 步骤3: 竞品分析
competitors = await market_analyzer.analyze_competitors({
    "competitor_works": ["《诡秘之主》", "《大奉打更人》"],
    "analysis_focus": ["核心卖点", "成功要素", "读者反馈"]
})

# 步骤4: 定位建议
positioning = await market_analyzer.generate_positioning({
    "genre": genre,
    "competitors": competitors,
    "target_readers": {
        "age_range": "18-35",
        "gender": "male",
        "preferences": ["爽文", "升级流", "热血"]
    }
})

# 步骤5: 创意生成（带查重校验）
def generate_ideas_with_check(input_data):
    ideas = idea_generator.generate_ideas(input_data)
    
    # 查重校验
    result = checker.check(
        content=str(ideas),
        comparison_library=existing_ideas_library,
        content_type='idea'
    )
    
    if not result['passed']:
        print(f"创意重复度超标: {result['score']}分 (阈值: {result['threshold']}分)")
        print(f"相似来源: {result['similar_sources']}")
    
    return ideas, result

ideas, check_result = generate_ideas_with_check({
    "genre": positioning.recommended_genre,
    "technique": "combination",
    "idea_count": 15
})

# 步骤6: 创意筛选
filtered = await idea_generator.filter_ideas({
    "ideas": ideas,
    "criteria": {
        "novelty_threshold": 7,
        "extensibility_threshold": 8,
        "market_match_threshold": 70
    }
})

# 步骤7: 创意验证
validated = await idea_generator.validate_idea({
    "target_idea": filtered.top_idea
})

# 步骤8: 高概念创建（带查重校验）
high_concept = idea_generator.create_high_concept({
    "validated_idea": validated.idea
})

# 查重校验
concept_check = checker.check(
    content=high_concept.description,
    comparison_library=existing_concepts_library,
    content_type='idea'
)

print(f"高概念查重结果: {concept_check['score']}分 - {concept_check['level_label']}")
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 平台选择准确度 | ≥85% | 选择最适合的平台 |
| 题材定位精准度 | ≥80% | 定位符合市场需求 |
| 创意新颖度 | ≥7分 | 创意有足够新意 |
| 创意延展性 | ≥8分 | 创意可支撑长篇 |
| 高概念清晰度 | 一句话能说清 | 概念简洁易懂 |
| **创意重复度** | **≤40分** | **创意足够原创** |

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

```python
# 步骤1: 主角设计（带查重校验）
def design_protagonist_with_check(input_data):
    protagonist = character_designer.design_protagonist(input_data)
    
    # 查重校验
    result = checker.check(
        content=protagonist.description + protagonist.background,
        comparison_library=existing_characters_library,
        content_type='character'
    )
    
    if not result['passed']:
        print(f"人物设计重复度超标: {result['score']}分")
        print(f"建议: {result['action']}")
    
    return protagonist, result

protagonist, check_result = design_protagonist_with_check({
    "character_data": {
        "name": "林风",
        "age": 18,
        "gender": "male",
        "personality_traits": ["勇敢", "聪明", "重情义", "有些固执"],
        "background": "小家族庶子，母亲早亡，受尽冷眼"
    }
})

# 补充设计
protagonist.abilities = {
    "initial": "普通修为",
    "golden_finger": "吞噬星空的能力",
    "growth_path": "觉醒→成长→质变"
}

protagonist.motivation = {
    "external_goal": "成为强者，保护在乎的人",
    "internal_need": "证明自己，获得认可",
    "core_fear": "失去在乎的人"
}

protagonist.arc = {
    "start_state": "受尽冷眼的庶子",
    "growth_trajectory": "获得能力→遭遇挫折→成长蜕变",
    "end_state": "成为强者"
}

# 步骤2: 配角设计
mentor = await character_designer.design_supporting({
    "character_data": {"name": "玄老", "role": "mentor"}
})

ally = await character_designer.design_supporting({
    "character_data": {"name": "苏晴", "role": "ally"}
})

rival = await character_designer.design_supporting({
    "character_data": {"name": "赵天", "role": "rival"}
})

# 步骤3: 反派设计（带查重校验）
antagonist = character_designer.design_antagonist({
    "character_data": {
        "name": "魔尊",
        "motivation": {"surface": "统治世界", "deep": "向世界复仇"},
        "abilities": {"power_level": "极高", "weakness": "内心执念"}
    }
})

# 查重校验
antagonist_check = checker.check(
    content=antagonist.description,
    comparison_library=existing_villains_library,
    content_type='character'
)

# 步骤4: 关系网络构建
network = await character_designer.build_relationships({
    "characters": [protagonist, mentor, ally, rival, antagonist],
    "relationships": [
        {"from": "林风", "to": "玄老", "type": "mentor", "strength": 9},
        {"from": "林风", "to": "苏晴", "type": "ally", "strength": 7},
        {"from": "林风", "to": "魔尊", "type": "enemy", "strength": 10}
    ]
})

# 步骤5: 质量评估
quality = await quality_evaluator.evaluate_dimension({
    "dimension": "character_depth",
    "characters": [protagonist, mentor, ally, rival, antagonist]
})
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 主角代入感 | ≥8分 | 读者能代入主角 |
| 人物深度 | ≥7分 | 人物立体有深度 |
| 关系张力 | ≥7分 | 关系网络有戏剧张力 |
| 一致性 | ≥90% | 人物行为前后一致 |
| **人物重复度** | **≤35分** | **人物设计原创** |

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

```python
# 步骤1: 结构设计
structure = await plot_architect.design_structure({
    "structure_type": "three_act",
    "total_words": 1000000,
    "climax_distribution": {
        "first_act_climax": {"chapter": 25, "intensity": 7},
        "midpoint": {"chapter": 50, "intensity": 8},
        "second_act_climax": {"chapter": 75, "intensity": 9},
        "final_climax": {"chapter": 100, "intensity": 10}
    }
})

# 步骤2: 世界观构建（带查重校验）
world = plot_architect.build_world({
    "type": "fantasy",
    "core_settings": {
        "power_system": {"levels": [...], "advancement": "..."},
        "rules": [...],
        "forces": [...]
    }
})

# 查重校验
world_check = checker.check(
    content=str(world.settings),
    comparison_library=existing_worlds_library,
    content_type='world_building'
)

# 步骤3: 大纲创建（带查重校验）
outline = plot_architect.create_outline({
    "outline_level": "chapter",
    "structure": structure,
    "world": world
})

# 查重校验每个章节大纲
for chapter in outline.chapters:
    chapter_check = checker.check(
        content=chapter.summary,
        comparison_library=existing_outlines_library,
        content_type='plot'
    )
    
    if not chapter_check['passed']:
        print(f"章节{chapter.number}大纲重复度: {chapter_check['score']}分")

# 步骤4: 伏笔设计
foreshadowing = await plot_architect.design_foreshadowing({
    "outline": outline,
    "major_plots": ["身世之谜", "金手指来源", "最终敌人"]
})

# 步骤5: 逻辑检查
logic = await plot_architect.check_plot_logic({
    "outline": outline,
    "world": world
})
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 结构完整性 | ≥90% | 结构完整合理 |
| 世界观自洽性 | ≥90% | 设定前后一致 |
| 大纲详细度 | 分章级别 | 大纲足够详细 |
| 伏笔覆盖率 | 主要情节都有 | 重要情节有伏笔 |
| 逻辑一致性 | ≥95% | 情节逻辑通顺 |
| **情节重复度** | **≤30分** | **情节原创** |

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

#### 场景一：带查重校验的章节创作

```python
from plagiarism_checker import SkillChainExecutor

# 创建带查重校验的执行器
executor = SkillChainExecutor(max_attempts=3)

def write_chapter_with_plagiarism_check(chapter_number, outline_data, comparison_library):
    """带查重校验的章节创作"""
    
    # 定义创作函数
    def create_chapter(input_data):
        return content_writer.write_chapter(input_data)
    
    # 执行带查重校验的创作
    result = executor.execute_skill(
        skill=create_chapter,
        input_data={
            "chapter_number": chapter_number,
            "word_count_target": 3000,
            "outline_data": outline_data
        },
        content_type='content',
        comparison_library=comparison_library
    )
    
    # 输出结果
    if result['status'] == 'success':
        print(f"✅ 章节{chapter_number}创作成功")
        print(f"   重复度分数: {result['plagiarism_score']}分")
        print(f"   尝试次数: {result['attempts']}")
    else:
        print(f"⚠️ 章节{chapter_number}达到最大重试次数")
        print(f"   最终分数: {result['plagiarism_score']}分")
        print(f"   需要人工审核: {result.get('needs_manual_review', False)}")
    
    return result

# 使用示例
chapter_result = write_chapter_with_plagiarism_check(
    chapter_number=1,
    outline_data={
        "title": "第一章 觉醒",
        "core_event": "主角出场，展示现状",
        "empathy_points": ["受欺压", "有志气"],
        "cliffhanger": "意外发生"
    },
    comparison_library=existing_chapters_library
)
```

#### 场景二：日常创作流程（含查重校验）

```python
async def dailyWritingWithCheck():
    """每日创作循环（含查重校验）"""
    
    # 1. 获取进度
    progress = await progress_tracker.get_statistics()
    
    # 2. 确定今日目标
    today_target = {
        "chapters": 2,
        "words_per_chapter": 3000
    }
    
    # 3. 创作循环
    for i in range(today_target["chapters"]):
        chapter_num = progress.current_chapter + i + 1
        
        # 写章节（带查重校验）
        result = executor.execute_skill(
            skill=lambda data: content_writer.write_chapter(data),
            input_data={
                "chapter_number": chapter_num,
                "word_count_target": today_target["words_per_chapter"],
                "outline_data": getOutlineData(chapter_num)
            },
            content_type='content',
            comparison_library=existing_chapters_library
        )
        
        # 处理结果
        if result['status'] == 'success':
            chapter = result['output']
            
            # 质量检查
            quality = await content_writer.check_quality({
                "chapter_number": chapter.number,
                "quality_check_level": "standard"
            })
            
            # 如果有问题，解决
            if quality.issues:
                solution = await problem_solver.solve_problem({
                    "problem_type": quality.issues[0].type,
                    "problem_description": quality.issues[0].description
                })
            
            # 更新进度
            await progress_tracker.update_progress({
                "current_chapter": chapter.number,
                "words_written": chapter.word_count
            })
        else:
            # 记录失败
            await progress_tracker.log_issue({
                "chapter": chapter_num,
                "issue": "plagiarism_check_failed",
                "score": result['plagiarism_score']
            })
    
    # 4. 生成日报
    report = await progress_tracker.generate_report({
        "report_type": "daily"
    })
    
    # 5. 导出查重日志
    log_path = checker.export_logs()
    print(f"查重日志已导出: {log_path}")
    
    return report
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 开篇代入感 | ≥8分 | 前三章建立强代入感 |
| 章节质量稳定性 | ≥7分 | 质量稳定不波动 |
| 日均产出 | ≥5000字 | 保持稳定产出 |
| 问题解决率 | ≥90% | 问题能及时解决 |
| **正文重复度** | **≤25分** | **正文高度原创** |
| **查重通过率** | **≥95%** | **一次通过率** |

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

#### 场景一：完整Skill链执行（含查重校验）

```python
from plagiarism_checker import SkillChainExecutor, create_checker

# 创建执行器和查重校验器
checker = create_checker(max_attempts=3, log_dir='./logs/plagiarism/')
executor = SkillChainExecutor(checker=checker)

# 定义技能列表
skills = [
    idea_generator,
    character_designer,
    plot_architect,
    content_writer,
    quality_evaluator
]

# 定义内容类型
content_types = ['idea', 'character', 'plot', 'content', 'content']

# 执行技能链
result = executor.execute_chain(
    skills=skills,
    input_data={
        "genre": "玄幻",
        "target_words": 1000000
    },
    comparison_library=existing_content_library,
    content_types=content_types
)

# 查看结果
if result['status'] == 'success':
    print("✅ Skill链执行成功")
    
    # 查看日志摘要
    summary = result['log_summary']
    print(f"\n查重校验摘要:")
    print(f"  总检查次数: {summary['total_checks']}")
    print(f"  通过次数: {summary['passed_checks']}")
    print(f"  通过率: {summary['pass_rate']:.1%}")
    print(f"  平均分数: {summary['average_score']:.1f}")
    print(f"  重试次数: {summary['total_retries']}")
else:
    print(f"❌ Skill链执行失败，在第{result['failed_at']}个技能")
```

#### 场景二：阶段性评估优化

```python
async def stageEvaluationWithCheck(chapter_end):
    """阶段性评估（含查重校验）"""
    
    # 1. 全面质量评估
    evaluation = await quality_evaluator.evaluate_full({
        "chapter_range": {"start": chapter_end - 19, "end": chapter_end},
        "evaluation_level": "comprehensive"
    })
    
    # 2. 批量查重校验
    plagiarism_results = []
    for chapter_num in range(chapter_end - 19, chapter_end + 1):
        chapter_content = get_chapter_content(chapter_num)
        
        check_result = checker.check(
            content=chapter_content,
            comparison_library=all_existing_content,
            content_type='chapter'
        )
        
        plagiarism_results.append({
            "chapter": chapter_num,
            "score": check_result['score'],
            "passed": check_result['passed']
        })
    
    # 3. 汇总问题
    issues = evaluation.weaknesses
    plagiarism_issues = [r for r in plagiarism_results if not r['passed']]
    
    # 4. 解决问题
    for issue in issues:
        solution = await problem_solver.solve_problem({
            "problem_type": issue.type,
            "problem_description": issue.description
        })
    
    # 5. 处理查重问题
    for pi in plagiarism_issues:
        print(f"⚠️ 章节{pi['chapter']}重复度超标: {pi['score']}分")
        # 触发重写流程
    
    # 6. 生成报告
    report = {
        "quality_score": evaluation.score,
        "plagiarism_summary": {
            "total": len(plagiarism_results),
            "passed": len([r for r in plagiarism_results if r['passed']]),
            "failed": len(plagiarism_issues)
        }
    }
    
    return report
```

### 预期效果

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 整体质量 | ≥80分 | 作品整体质量达标 |
| 伏笔回收率 | 100% | 所有伏笔都回收 |
| 一致性 | ≥95% | 人物行为一致 |
| 逻辑性 | ≥95% | 情节逻辑通顺 |
| **整体重复度** | **≤25分** | **作品整体原创** |
| **查重通过率** | **≥98%** | **几乎全部通过** |

---

## 📊 查重校验日志查看

### 查看日志摘要

```python
# 获取日志摘要
summary = checker.get_log_summary()

print("=== 查重校验日志摘要 ===")
print(f"会话ID: {summary['session_id']}")
print(f"总检查次数: {summary['total_checks']}")
print(f"通过次数: {summary['passed_checks']}")
print(f"失败次数: {summary['failed_checks']}")
print(f"通过率: {summary['pass_rate']:.1%}")
print(f"平均分数: {summary['average_score']:.1f}")
print(f"最低分数: {summary['min_score']:.1f}")
print(f"最高分数: {summary['max_score']:.1f}")
print(f"重试次数: {summary['total_retries']}")
```

### 查看特定技能统计

```python
# 获取特定技能的统计
skill_stats = checker.log.get_skill_stats('content-writer')

print(f"\n=== content-writer 查重统计 ===")
print(f"总检查次数: {skill_stats['total_checks']}")
print(f"重试次数: {skill_stats['total_retries']}")
print(f"平均分数: {skill_stats['average_score']:.1f}")
print(f"最佳分数: {skill_stats['best_score']:.1f}")
print(f"最差分数: {skill_stats['worst_score']:.1f}")
```

### 导出日志

```python
# 导出日志到文件
log_path = checker.export_logs('./logs/plagiarism/session_001.json')
print(f"日志已导出: {log_path}")
```

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

### 6. 查重校验（新增）
- **每个技能环节执行后立即查重**
- **重复度超标自动触发重造**
- **记录完整查重日志**
- **定期查看查重统计**

---

## 🔧 配置建议

### 阈值调整建议

| 场景 | 建议阈值 | 说明 |
|------|---------|------|
| 初创阶段 | 30-35 | 适度宽松，鼓励创作 |
| 稳定创作 | 25-30 | 标准要求 |
| 完稿阶段 | 20-25 | 更严格，确保质量 |
| 对话内容 | 40-50 | 对话可适当参考 |

### 重试次数建议

| 场景 | 建议次数 | 说明 |
|------|---------|------|
| 创意生成 | 3-5次 | 创意需要多样性 |
| 人物设计 | 2-3次 | 人物需要独特性 |
| 正文创作 | 2-3次 | 平衡效率和质量 |

---

**文档更新时间**：2026-05-26  
**新增功能**：查重校验系统

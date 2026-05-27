---
name: "quality-evaluator"
description: "Evaluates novel quality using quantitative metrics across multiple dimensions. Invoke when assessing work quality, identifying strengths/weaknesses, or generating quality reports for improvement decisions."
---

# Quality Evaluator Skill

## 功能定义

质量评估技能，专注于小说质量的量化评估，提供客观的质量评分和改进建议。

**单一职责**：仅负责质量评估，不涉及内容创作、问题解决等其他环节。

---

## 输入参数

```json
{
  "action": "evaluate_full | evaluate_dimension | evaluate_chapter | generate_report | compare_versions",
  "params": {
    "work_id": "xxx",
    "chapter_range": {
      "start": 1,
      "end": 100
    },
    "dimensions": [
      "market_match",
      "idea_appeal",
      "character_depth",
      "plot_quality",
      "emotional_impact",
      "language_quality",
      "completeness"
    ],
    "evaluation_level": "quick | standard | comprehensive",
    "comparison_data": {
      "baseline_version": "v1.0",
      "current_version": "v2.0"
    }
  }
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 执行动作类型 |
| params.work_id | string | 否 | 作品ID |
| params.chapter_range | object | 否 | 章节范围 |
| params.dimensions | array | 否 | 评估维度 |
| params.evaluation_level | string | 否 | 评估级别 |
| params.comparison_data | object | 否 | 对比数据 |

---

## 输出结果

```json
{
  "status": "success | error",
  "data": {
    "overall_score": 82.5,
    "rating": "良好",
    "dimension_scores": {
      "market_match": {
        "score": 85,
        "weight": 15,
        "weighted_score": 12.75,
        "details": {
          "target_reader_match": 88,
          "genre_heat": 82,
          "differentiation": 85
        }
      },
      "idea_appeal": {
        "score": 80,
        "weight": 20,
        "weighted_score": 16.0,
        "details": {
          "novelty": 82,
          "conflict_strength": 78,
          "concept_spread": 85,
          "extensibility": 75
        }
      },
      "character_depth": {
        "score": 85,
        "weight": 20,
        "weighted_score": 17.0,
        "details": {
          "protagonist_empathy": 88,
          "character_depth": 82,
          "arc_completeness": 85,
          "relationship_tension": 85
        }
      },
      "plot_quality": {
        "score": 80,
        "weight": 20,
        "weighted_score": 16.0,
        "details": {
          "attraction": 82,
          "turn_density": 78,
          "logic": 80,
          "pacing": 82,
          "foreshadowing": 78
        }
      },
      "emotional_impact": {
        "score": 82,
        "weight": 10,
        "weighted_score": 8.2,
        "details": {
          "resonance": 85,
          "richness": 80,
          "memory_points": 81
        }
      },
      "language_quality": {
        "score": 85,
        "weight": 10,
        "weighted_score": 8.5,
        "details": {
          "fluency": 88,
          "description": 82,
          "dialogue": 85,
          "style": 85
        }
      },
      "completeness": {
        "score": 80,
        "weight": 5,
        "weighted_score": 4.0,
        "details": {
          "structure": 82,
          "detail": 80,
          "consistency": 78
        }
      }
    },
    "strengths": [
      "代入感强，主角魅力突出",
      "语言流畅，阅读体验佳",
      "市场定位精准"
    ],
    "weaknesses": [
      "情节转折密度不足",
      "伏笔体系需完善",
      "设定前后有小矛盾"
    ],
    "improvement_suggestions": [
      {
        "priority": "high",
        "dimension": "plot_quality",
        "suggestion": "增加情节转折，每5章设置一次中转折",
        "expected_improvement": "+3分"
      },
      {
        "priority": "medium",
        "dimension": "completeness",
        "suggestion": "完善伏笔体系，确保主要伏笔回收",
        "expected_improvement": "+2分"
      }
    ],
    "comparison_result": {
      "version_improvement": "+5.5分",
      "dimension_changes": {
        "character_depth": "+3分",
        "plot_quality": "+2分"
      }
    }
  },
  "errors": []
}
```

---

## 执行逻辑

### 1. 全面评估 (evaluate_full)

**执行步骤**：
```
1. 收集作品数据
    - 内容数据
    - 人物数据
    - 情节数据
    - 市场数据
    ↓
2. 逐维度评估
    - 市场匹配度
    - 创意吸引力
    - 人物塑造力
    - 情节构建力
    - 情感感染力
    - 语言表现力
    - 整体完成度
    ↓
3. 计算加权得分
    ↓
4. 识别优势和劣势
    ↓
5. 生成改进建议
    ↓
6. 返回评估结果
```

---

### 2. 维度评估 (evaluate_dimension)

**执行步骤**：
```
1. 确定评估维度
    ↓
2. 收集维度相关数据
    ↓
3. 逐指标评估
    ↓
4. 计算维度得分
    ↓
5. 生成维度分析
    ↓
6. 返回评估结果
```

---

### 3. 章节评估 (evaluate_chapter)

**执行步骤**：
```
1. 确定章节范围
    ↓
2. 逐章评估
    - 情节推进
    - 人物表现
    - 语言质量
    - 节奏控制
    ↓
3. 识别问题章节
    ↓
4. 生成章节报告
    ↓
5. 返回评估结果
```

---

### 4. 报告生成 (generate_report)

**执行步骤**：
```
1. 整合评估数据
    ↓
2. 生成可视化图表
    - 雷达图
    - 趋势图
    - 对比图
    ↓
3. 编写分析报告
    - 总体评估
    - 维度分析
    - 优劣势分析
    - 改进建议
    ↓
4. 生成报告文档
    ↓
5. 返回报告
```

---

### 5. 版本对比 (compare_versions)

**执行步骤**：
```
1. 获取对比版本数据
    ↓
2. 逐维度对比
    ↓
3. 计算变化幅度
    ↓
4. 分析变化原因
    ↓
5. 生成对比报告
    ↓
6. 返回对比结果
```

---

## 评估维度详解

### 维度1：市场匹配度（15%）

**指标**：
- 目标读者匹配度
- 题材热度指数
- 差异化竞争力

**评估方法**：
- 读者画像对比
- 市场数据分析
- 竞品对比分析

---

### 维度2：创意吸引力（20%）

**指标**：
- 核心创意新颖度
- 核心冲突强度
- 概念传播力
- 创意延展性

**评估方法**：
- 同类创意对比
- 冲突强度分析
- 传播便利性测试

---

### 维度3：人物塑造力（20%）

**指标**：
- 主角代入感强度
- 人物立体度
- 人物弧光完整性
- 人物关系张力

**评估方法**：
- 代入感测试
- 性格维度分析
- 成长轨迹分析

---

### 维度4：情节构建力（20%）

**指标**：
- 情节吸引力
- 情节转折密度
- 情节逻辑性
- 节奏控制力
- 伏笔体系完整度

**评估方法**：
- 追读动力评估
- 转折密度计算
- 逻辑检查
- 节奏分析

---

### 维度5：情感感染力（10%）

**指标**：
- 情感共鸣指数
- 情感层次丰富度
- 记忆点强度

**评估方法**：
- 情感点识别
- 共鸣强度测试
- 记忆点分析

---

### 维度6：语言表现力（10%）

**指标**：
- 语言流畅度
- 描写表现力
- 对话自然度
- 风格独特性

**评估方法**：
- 语言质量检查
- 描写效果评估
- 对话自然度分析

---

### 维度7：整体完成度（5%）

**指标**：
- 结构完整性
- 细节完善度
- 设定一致性

**评估方法**：
- 结构检查
- 细节检查
- 一致性检查

---

## 错误处理机制

### 错误类型

| 错误码 | 错误描述 | 处理方式 |
|--------|---------|---------|
| INVALID_ACTION | 无效的动作类型 | 返回错误，提示有效动作 |
| WORK_NOT_FOUND | 作品未找到 | 提示需要提供作品数据 |
| INSUFFICIENT_DATA | 数据不足 | 返回部分结果，标注缺失 |
| DIMENSION_NOT_SUPPORTED | 不支持的维度 | 返回错误，提示支持维度 |
| COMPARISON_FAILED | 对比失败 | 返回错误原因 |

---

## 调用接口规范

### 被调用接口

本skill可被以下skill调用：
- `problem-solver`：提供评估数据用于问题诊断
- `progress-tracker`：提供质量数据用于进度管理

### 调用其他skill

本skill可调用以下skill获取评估所需数据：
- `character-designer`：获取人物数据
- `plot-architect`：获取情节数据
- `content-writer`：获取内容数据

---

## 使用示例

### 示例1：全面评估

```json
输入：
{
  "action": "evaluate_full",
  "params": {
    "work_id": "novel_001",
    "evaluation_level": "comprehensive"
  }
}

输出：
{
  "status": "success",
  "data": {
    "overall_score": 82.5,
    "rating": "良好",
    "dimension_scores": {...}
  }
}
```

---

## 核心原则（必须遵循）

### 1. 客观中立原则

**定义：** 基于事实和合理分析提供内容，避免主观臆断和过度迎合。

**执行要求：**
- 所有分析和建议必须基于事实依据
- 避免无根据的主观推测
- 不因用户偏好而扭曲客观事实
- 提供多角度分析，呈现完整图景
- 明确区分事实陈述和观点表达

**应用场景：**
- 质量评估报告
- 问题识别和分析
- 评分依据说明
- 改进建议生成

---

### 2. 最优决策原则

**定义：** 面对多种方案时，经多维度评估后直接提供最优解，并说明核心依据。

**执行要求：**
- 面对多方案时，必须进行多维度评估
- 直接提供最优方案，不列出所有选项让用户选择
- 必须说明选择该方案的核心依据
- 评估维度包括：可行性、效果、成本、风险、一致性、扩展性
- 最优方案必须经得起推敲和验证

**评估维度：**
1. **可行性：** 方案是否可执行
2. **效果：** 预期效果是否最优
3. **成本：** 时间、资源成本是否合理
4. **风险：** 潜在风险是否可控
5. **一致性：** 是否与现有设定一致
6. **扩展性：** 是否为后续发展留有空间

**决策流程：**
```
识别问题 → 生成方案 → 多维度评估 → 选择最优 → 说明依据 → 执行实施
```

**应用场景：**
- 质量问题修复方案
- 评估标准调整
- 改进建议选择
- 评分权重设置

---

## 注意事项

1. **客观性**：评估应基于数据和标准，避免主观
2. **全面性**：评估要全面，不遗漏维度
3. **可操作性**：建议要具体可执行
4. **动态性**：评估标准可根据类型调整
5. **核心原则优先**：客观中立原则 > 最优决策原则 > 其他注意事项

---

## 依赖资源

- 评估指标体系
- 评分标准库
- 评估工具（评分卡、计算工具）
- 历史评估数据

---

## 性能指标

- 全面评估时间：< 5分钟
- 维度评估时间：< 1分钟/维度
- 章节评估时间：< 30秒/章
- 报告生成时间：< 2分钟
- 版本对比时间：< 1分钟

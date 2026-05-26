---
name: "idea-generator"
description: "Generates and validates novel ideas using creative techniques. Invoke when developing core concepts, creating high-concept statements, or validating idea feasibility for a new novel."
---

# Idea Generator Skill

## 功能定义

创意生成技能，专注于小说核心创意的激发、筛选和验证，确保创意的新颖性和可行性。

**单一职责**：仅负责创意的生成和验证，不涉及市场分析、人物设计、情节架构等其他环节。

---

## 输入参数

```json
{
  "action": "generate_ideas | filter_ideas | validate_idea | create_high_concept",
  "params": {
    "genre": "玄幻",
    "technique": "what_if | combination | inversion | cross_over",
    "idea_count": 10,
    "target_idea": {
      "core_concept": "xxx",
      "core_conflict": "xxx",
      "emotional_core": "xxx"
    },
    "validation_criteria": {
      "novelty_threshold": 7,
      "extensibility_threshold": 8,
      "market_match_threshold": 70
    }
  }
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 执行动作类型 |
| params.genre | string | 否 | 题材类型 |
| params.technique | string | 否 | 创意激发方法 |
| params.idea_count | number | 否 | 生成创意数量 |
| params.target_idea | object | 否 | 待验证的创意 |
| params.validation_criteria | object | 否 | 验证标准 |

---

## 输出结果

```json
{
  "status": "success | error",
  "data": {
    "ideas": [
      {
        "id": "idea_001",
        "core_concept": "xxx",
        "technique_used": "what_if",
        "novelty_score": 8.5,
        "extensibility_score": 9.0,
        "market_match_score": 75
      }
    ],
    "filtered_ideas": [
      {
        "id": "idea_001",
        "rank": 1,
        "reason": "新颖度高，延展性强"
      }
    ],
    "validation_result": {
      "is_valid": true,
      "scores": {
        "novelty": 8.5,
        "extensibility": 9.0,
        "market_match": 75,
        "conflict_strength": 8.0
      },
      "issues": [],
      "suggestions": []
    },
    "high_concept": {
      "one_sentence": "xxx",
      "core_conflict": "xxx",
      "emotional_core": "xxx",
      "memory_points": ["xxx", "xxx"]
    }
  },
  "errors": []
}
```

---

## 执行逻辑

### 1. 创意生成 (generate_ideas)

**执行步骤**：
```
1. 验证输入参数
    ↓
2. 选择创意激发方法
    - What-if假设法
    - 组合创新法
    - 反转颠覆法
    - 跨界融合法
    ↓
3. 批量生成创意
    ↓
4. 初步评分
    - 新颖度
    - 延展性
    - 市场匹配度
    ↓
5. 返回创意列表
```

**创意激发方法详解**：

**What-if假设法**：
- 提出假设性问题："如果...会怎样？"
- 探索假设的后果和可能性
- 示例："如果修仙者可以吞噬星空会怎样？"

**组合创新法**：
- 选择两个不同元素进行组合
- 探索组合后的新可能
- 示例："系统流 + 修仙 = 修仙系统"

**反转颠覆法**：
- 识别传统设定
- 设计反转版本
- 示例："反派才是救世主"

**跨界融合法**：
- 选择不同类型的元素
- 进行跨类型融合
- 示例："科幻 + 玄幻 = 星际修仙"

---

### 2. 创意筛选 (filter_ideas)

**执行步骤**：
```
1. 验证创意列表
    ↓
2. 多维度评分
    - 新颖度评分（0-10）
    - 延展性评分（0-10）
    - 市场匹配度评分（0-100）
    - 冲突强度评分（0-10）
    ↓
3. 计算综合得分
    综合得分 = (新颖度×0.3) + (延展性×0.3) + (市场匹配度×0.2) + (冲突强度×0.2)
    ↓
4. 排序筛选
    ↓
5. 返回筛选结果
```

---

### 3. 创意验证 (validate_idea)

**执行步骤**：
```
1. 验证创意完整性
    - 是否有核心概念
    - 是否有核心冲突
    - 是否有情感内核
    ↓
2. 多维度验证
    - 新颖性验证
    - 延展性验证
    - 市场匹配验证
    - 冲突强度验证
    ↓
3. 识别潜在问题
    ↓
4. 生成优化建议
    ↓
5. 返回验证结果
```

**验证标准**：
- 新颖度 ≥ 7分
- 延展性 ≥ 8分
- 市场匹配度 ≥ 70分
- 冲突强度 ≥ 7分

---

### 4. 高概念创建 (create_high_concept)

**执行步骤**：
```
1. 提炼一句话概念
    - 简洁有力
    - 易于理解
    - 有吸引力
    ↓
2. 明确核心冲突
    - 冲突本质
    - 冲突双方
    - 冲突强度
    ↓
3. 确定情感内核
    - 主情感线
    - 情感变化
    ↓
4. 设计记忆点
    - 核心金句
    - 独特设定
    - 人物特质
    ↓
5. 返回高概念
```

---

## 错误处理机制

### 错误类型

| 错误码 | 错误描述 | 处理方式 |
|--------|---------|---------|
| INVALID_ACTION | 无效的动作类型 | 返回错误，提示有效动作 |
| INSUFFICIENT_IDEAS | 创意数量不足 | 降低标准或增加生成 |
| VALIDATION_FAILED | 验证不通过 | 返回问题列表和改进建议 |
| IDEA_TOO_SIMILAR | 创意过于相似 | 提示差异化方向 |
| MISSING_CORE_ELEMENTS | 缺少核心要素 | 返回错误，提示缺少的要素 |

### 错误响应格式

```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "创意验证不通过",
    "details": {
      "failed_criteria": ["novelty", "conflict_strength"],
      "current_scores": {
        "novelty": 6.5,
        "conflict_strength": 6.0
      },
      "threshold": {
        "novelty": 7,
        "conflict_strength": 7
      }
    }
  }
}
```

---

## 调用接口规范

### 被调用接口

本skill可被以下skill调用：
- `character-designer`：提供核心创意信息
- `plot-architect`：提供核心冲突和设定
- `progress-tracker`：提交创意开发阶段完成

### 调用其他skill

本skill可调用以下skill获取辅助信息：
- `market-analyzer`：获取市场定位和题材信息

**调用示例**：
```json
{
  "call": "market-analyzer",
  "action": "analyze_genre",
  "params": {
    "genre": "玄幻"
  }
}
```

---

## 使用示例

### 示例1：生成创意

```json
输入：
{
  "action": "generate_ideas",
  "params": {
    "genre": "玄幻",
    "technique": "combination",
    "idea_count": 10
  }
}

输出：
{
  "status": "success",
  "data": {
    "ideas": [
      {
        "id": "idea_001",
        "core_concept": "修仙者获得吞噬星空的能力",
        "technique_used": "combination",
        "novelty_score": 8.5,
        "extensibility_score": 9.0
      }
    ]
  }
}
```

### 示例2：验证创意

```json
输入：
{
  "action": "validate_idea",
  "params": {
    "target_idea": {
      "core_concept": "修仙者获得吞噬星空的能力",
      "core_conflict": "主角vs宇宙意志",
      "emotional_core": "逆天改命的热血"
    }
  }
}

输出：
{
  "status": "success",
  "data": {
    "validation_result": {
      "is_valid": true,
      "scores": {
        "novelty": 8.5,
        "extensibility": 9.0,
        "conflict_strength": 8.0
      }
    }
  }
}
```

---

## 注意事项

1. **创意数量**：先生成足够数量，再筛选质量
2. **延迟评判**：生成阶段不评判，避免扼杀创意
3. **多角度思考**：尝试多种激发方法
4. **可行性验证**：创意要能落地执行

---

## 依赖资源

- 创意激发方法库
- 同类创意数据库（用于对比）
- 市场分析结果（来自market-analyzer）
- 创意评分模型

---

## 性能指标

- 创意生成速度：10个创意/分钟
- 创意筛选速度：20个创意/分钟
- 创意验证时间：< 3秒/创意
- 高概念创建时间：< 5秒

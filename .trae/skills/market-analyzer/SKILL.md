---
name: "market-analyzer"
description: "Analyzes market trends, platform data, and competitor works to guide novel positioning. Invoke when starting a new novel project or when market research is needed for positioning decisions."
---

# Market Analyzer Skill

## 功能定义

市场分析技能，专注于小说创作的市场调研和定位分析，为创作决策提供数据支撑。

**单一职责**：仅负责市场数据的收集、分析和定位建议，不涉及创意开发、人物设计等其他环节。

---

## 输入参数

```json
{
  "action": "analyze_platform | analyze_genre | analyze_competitors | generate_positioning",
  "params": {
    "platforms": ["起点", "晋江", "番茄"],
    "genre": "玄幻",
    "competitor_works": ["作品1", "作品2"],
    "target_readers": {
      "age_range": "18-35",
      "gender": "male",
      "preferences": ["爽文", "升级流"]
    }
  }
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 执行动作类型 |
| params.platforms | array | 否 | 待分析平台列表 |
| params.genre | string | 否 | 题材类型 |
| params.competitor_works | array | 否 | 竞品作品列表 |
| params.target_readers | object | 否 | 目标读者画像 |

---

## 输出结果

```json
{
  "status": "success | error",
  "data": {
    "platform_analysis": {
      "platform": "起点",
      "user_scale": "日活500万",
      "genre_distribution": {},
      "revenue_model": "付费阅读",
      "recommendation": "推荐指数：8.5/10"
    },
    "genre_analysis": {
      "genre": "玄幻",
      "market_capacity": "大",
      "competition_level": "高",
      "trend": "上升",
      "opportunity_score": 7.5
    },
    "competitor_analysis": {
      "work_name": "xxx",
      "core_selling_points": [],
      "differentiation_opportunities": []
    },
    "positioning_suggestion": {
      "recommended_platform": "起点",
      "recommended_genre": "东方玄幻",
      "differentiation_strategy": "xxx",
      "risk_warning": "xxx"
    }
  },
  "errors": []
}
```

---

## 执行逻辑

### 1. 平台分析 (analyze_platform)

**执行步骤**：
```
1. 验证输入参数
    ↓
2. 收集平台数据
    - 用户规模和画像
    - 题材分布
    - 收益模式
    - 规则要求
    ↓
3. 分析平台特点
    - 优势劣势
    - 适合的作品类型
    - 推荐机制
    ↓
4. 生成平台评估报告
    ↓
5. 返回分析结果
```

**数据来源**：
- 平台公开数据
- 第三方数据平台
- 行业报告
- 历史数据

---

### 2. 题材分析 (analyze_genre)

**执行步骤**：
```
1. 验证题材类型
    ↓
2. 收集题材数据
    - 市场容量
    - 作品数量
    - 读者规模
    - 增长趋势
    ↓
3. 计算机会指数
    机会指数 = (市场容量×0.3) + ((10-竞争强度)×0.3) + (增长趋势×0.2) + (个人匹配度×0.2)
    ↓
4. 生成题材分析报告
    ↓
5. 返回分析结果
```

---

### 3. 竞品分析 (analyze_competitors)

**执行步骤**：
```
1. 验证竞品列表
    ↓
2. 逐个分析竞品
    - 基础信息
    - 核心设定
    - 成功要素
    - 读者反馈
    ↓
3. 提取成功模式
    ↓
4. 识别差异化机会
    ↓
5. 生成竞品分析报告
    ↓
6. 返回分析结果
```

---

### 4. 定位建议生成 (generate_positioning)

**执行步骤**：
```
1. 综合平台分析结果
    ↓
2. 综合题材分析结果
    ↓
3. 综合竞品分析结果
    ↓
4. 生成定位建议
    - 平台选择
    - 题材选择
    - 差异化策略
    - 风险提示
    ↓
5. 返回定位建议
```

---

## 错误处理机制

### 错误类型

| 错误码 | 错误描述 | 处理方式 |
|--------|---------|---------|
| INVALID_ACTION | 无效的动作类型 | 返回错误，提示有效动作 |
| MISSING_PARAMS | 缺少必要参数 | 返回错误，提示缺少的参数 |
| DATA_NOT_FOUND | 数据未找到 | 返回部分结果，标注缺失部分 |
| ANALYSIS_FAILED | 分析失败 | 记录错误日志，返回错误信息 |
| INVALID_PLATFORM | 无效的平台名称 | 返回错误，提示有效平台 |

### 错误响应格式

```json
{
  "status": "error",
  "error": {
    "code": "MISSING_PARAMS",
    "message": "缺少必要参数：genre",
    "details": "题材分析需要指定题材类型"
  },
  "data": null
}
```

---

## 调用接口规范

### 被调用接口

本skill可被以下skill调用：
- `idea-generator`：获取市场定位信息
- `progress-tracker`：提交市场分析阶段完成

### 调用其他skill

本skill不调用其他skill，保持单一职责。

---

## 使用示例

### 示例1：分析平台

```json
输入：
{
  "action": "analyze_platform",
  "params": {
    "platforms": ["起点", "番茄"]
  }
}

输出：
{
  "status": "success",
  "data": {
    "platform_analysis": [
      {
        "platform": "起点",
        "user_scale": "日活500万",
        "recommendation": "推荐指数：8.5/10"
      },
      {
        "platform": "番茄",
        "user_scale": "日活800万",
        "recommendation": "推荐指数：7.5/10"
      }
    ]
  }
}
```

### 示例2：生成定位建议

```json
输入：
{
  "action": "generate_positioning",
  "params": {
    "genre": "玄幻",
    "target_readers": {
      "age_range": "18-35",
      "gender": "male"
    }
  }
}

输出：
{
  "status": "success",
  "data": {
    "positioning_suggestion": {
      "recommended_platform": "起点",
      "recommended_genre": "东方玄幻",
      "differentiation_strategy": "结合系统流与修仙设定",
      "risk_warning": "竞争激烈，需强差异化"
    }
  }
}
```

---

## 注意事项

1. **数据时效性**：市场数据有时效性，建议定期更新
2. **客观性**：分析应基于数据，避免主观臆断
3. **全面性**：分析要全面，不遗漏重要维度
4. **可操作性**：建议要具体可执行，不空泛

---

## 依赖资源

- 市场数据源（平台公开数据、第三方数据）
- 竞品数据库
- 行业报告库
- 历史分析记录

---

## 性能指标

- 平台分析响应时间：< 5秒
- 题材分析响应时间：< 3秒
- 竞品分析响应时间：< 10秒/作品
- 定位建议生成时间：< 5秒

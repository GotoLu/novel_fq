---
name: "progress-tracker"
description: "Tracks writing progress, manages milestones, and monitors key node completion. Invoke when updating progress, checking milestone status, or generating progress reports for project management."
---

# Progress Tracker Skill

## 功能定义

进度跟踪技能，专注于创作进度的管理和关键节点的检验，确保创作按计划推进。

**单一职责**：仅负责进度管理和节点检验，不涉及内容创作、质量评估等其他环节。

---

## 输入参数

```json
{
  "action": "init_project | update_progress | check_node | generate_report | adjust_plan | get_statistics",
  "params": {
    "project_id": "xxx",
    "project_data": {
      "name": "xxx",
      "target_words": 1000000,
      "target_duration": 120,
      "start_date": "2026-05-26"
    },
    "progress_data": {
      "current_stage": "content_writing",
      "current_chapter": 50,
      "words_written": 150000,
      "time_spent": 30
    },
    "node_data": {
      "node_id": "node_005",
      "node_name": "黄金三章完成",
      "completion_status": "completed",
      "completion_date": "2026-06-01"
    },
    "report_type": "daily | weekly | stage | full",
    "adjustment_reason": "xxx"
  }
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 执行动作类型 |
| params.project_id | string | 否 | 项目ID |
| params.project_data | object | 否 | 项目数据 |
| params.progress_data | object | 否 | 进度数据 |
| params.node_data | object | 否 | 节点数据 |
| params.report_type | string | 否 | 报告类型 |
| params.adjustment_reason | string | 否 | 调整原因 |

---

## 输出结果

```json
{
  "status": "success | error",
  "data": {
    "project_info": {
      "project_id": "proj_001",
      "name": "xxx",
      "status": "in_progress",
      "start_date": "2026-05-26",
      "target_completion": "2026-09-23",
      "current_stage": "content_writing"
    },
    "progress_status": {
      "current_stage": "content_writing",
      "stage_progress": 15,
      "overall_progress": 45,
      "words_written": 150000,
      "words_target": 1000000,
      "words_progress": 15,
      "chapters_completed": 50,
      "days_elapsed": 30,
      "days_remaining": 90,
      "on_schedule": true
    },
    "node_status": [
      {
        "node_id": "node_001",
        "node_name": "平台选择决策",
        "stage": "market_analysis",
        "status": "completed",
        "completion_date": "2026-05-28",
        "score": 85
      },
      {
        "node_id": "node_005",
        "node_name": "黄金三章完成",
        "stage": "content_writing",
        "status": "completed",
        "completion_date": "2026-06-01",
        "score": 88
      },
      {
        "node_id": "node_006",
        "node_name": "第一卷完成",
        "stage": "content_writing",
        "status": "in_progress",
        "target_date": "2026-06-15"
      }
    ],
    "statistics": {
      "daily_average_words": 5000,
      "weekly_average_words": 35000,
      "efficiency_trend": "stable",
      "quality_trend": "improving",
      "estimated_completion": "2026-09-20"
    },
    "milestones": [
      {
        "milestone": "市场分析完成",
        "target_date": "2026-05-30",
        "actual_date": "2026-05-29",
        "status": "completed",
        "on_time": true
      },
      {
        "milestone": "大纲设计完成",
        "target_date": "2026-06-15",
        "actual_date": null,
        "status": "in_progress",
        "on_time": null
      }
    ],
    "alerts": [
      {
        "type": "info",
        "message": "进度正常，按计划推进",
        "suggestion": null
      }
    ],
    "report": {
      "report_type": "daily",
      "summary": "今日完成5000字，进度正常",
      "details": {...}
    }
  },
  "errors": []
}
```

---

## 执行逻辑

### 1. 项目初始化 (init_project)

**执行步骤**：
```
1. 创建项目记录
    ↓
2. 设定项目目标
    - 字数目标
    - 时间目标
    - 质量目标
    ↓
3. 创建阶段计划
    - 7个阶段
    - 各阶段时间分配
    ↓
4. 创建关键节点清单
    - 15个关键节点
    - 各节点检验标准
    ↓
5. 初始化进度记录
    ↓
6. 返回项目信息
```

---

### 2. 进度更新 (update_progress)

**执行步骤**：
```
1. 验证进度数据
    ↓
2. 更新进度记录
    - 当前阶段
    - 已写字数
    - 已完成章节
    - 已用时间
    ↓
3. 计算进度指标
    - 阶段进度
    - 整体进度
    - 日均效率
    ↓
4. 对比计划进度
    ↓
5. 生成进度预警
    ↓
6. 返回进度状态
```

---

### 3. 节点检验 (check_node)

**执行步骤**：
```
1. 获取节点信息
    ↓
2. 检验节点完成条件
    - 交付物检查
    - 质量标准检查
    ↓
3. 评估节点得分
    ↓
4. 判断是否通过
    ↓
5. 更新节点状态
    ↓
6. 生成节点报告
    ↓
7. 返回检验结果
```

---

### 4. 报告生成 (generate_report)

**执行步骤**：
```
1. 确定报告类型
    - 日报
    - 周报
    - 阶段报告
    - 完整报告
    ↓
2. 收集报告数据
    ↓
3. 分析进度情况
    ↓
4. 生成报告内容
    - 进度摘要
    - 详细数据
    - 分析结论
    - 建议措施
    ↓
5. 返回报告
```

---

### 5. 计划调整 (adjust_plan)

**执行步骤**：
```
1. 分析调整原因
    ↓
2. 评估调整影响
    ↓
3. 设计调整方案
    ↓
4. 更新项目计划
    ↓
5. 通知相关方
    ↓
6. 返回调整结果
```

---

### 6. 统计数据 (get_statistics)

**执行步骤**：
```
1. 收集历史数据
    ↓
2. 计算统计指标
    - 日均字数
    - 周均字数
    - 效率趋势
    - 质量趋势
    ↓
3. 预测完成时间
    ↓
4. 返回统计数据
```

---

## 关键节点清单

### 阶段1：市场分析与定位
- node_001：平台选择决策
- node_002：题材定位确认

### 阶段2：核心创意开发
- node_003：核心创意确定
- node_004：差异化优势确认

### 阶段3：人物体系塑造
- node_005：主角设定完成
- node_006：人物关系网络完成

### 阶段4：情节架构设计
- node_007：世界观构建完成
- node_008：大纲体系完成
- node_009：开篇三章设计完成

### 阶段5：正文创作执行
- node_010：黄金三章完成
- node_011：第一卷完成
- node_012：中期质量检查
- node_013：全书完稿

### 阶段6：打磨优化完善
- node_014：整体审查完成
- node_015：最终定稿

---

## 错误处理机制

### 错误类型

| 错误码 | 错误描述 | 处理方式 |
|--------|---------|---------|
| INVALID_ACTION | 无效的动作类型 | 返回错误，提示有效动作 |
| PROJECT_NOT_FOUND | 项目未找到 | 提示需要先初始化项目 |
| NODE_NOT_FOUND | 节点未找到 | 返回有效节点列表 |
| INVALID_PROGRESS_DATA | 无效的进度数据 | 提示有效数据格式 |
| NODE_NOT_PASSED | 节点检验未通过 | 返回未通过原因 |

---

## 调用接口规范

### 被调用接口

本skill可被所有其他skill调用，用于：
- 提交阶段完成状态
- 记录进度数据
- 检验关键节点

### 调用其他skill

本skill可调用以下skill获取辅助信息：
- `quality-evaluator`：获取质量评估数据用于节点检验

---

## 使用示例

### 示例1：初始化项目

```json
输入：
{
  "action": "init_project",
  "params": {
    "project_data": {
      "name": "玄幻小说项目",
      "target_words": 1000000,
      "target_duration": 120,
      "start_date": "2026-05-26"
    }
  }
}

输出：
{
  "status": "success",
  "data": {
    "project_info": {
      "project_id": "proj_001",
      "name": "玄幻小说项目",
      "status": "initialized"
    }
  }
}
```

### 示例2：更新进度

```json
输入：
{
  "action": "update_progress",
  "params": {
    "project_id": "proj_001",
    "progress_data": {
      "current_stage": "content_writing",
      "current_chapter": 50,
      "words_written": 150000
    }
  }
}

输出：
{
  "status": "success",
  "data": {
    "progress_status": {
      "overall_progress": 45,
      "on_schedule": true
    }
  }
}
```

---

## 注意事项

1. **及时更新**：进度要及时更新，保持数据准确
2. **节点严格**：关键节点要严格检验，不达标不通过
3. **预警及时**：进度异常要及时预警
4. **灵活调整**：计划可根据实际情况调整

---

## 依赖资源

- 项目数据库
- 进度记录系统
- 节点检验标准
- 统计分析工具

---

## 性能指标

- 项目初始化时间：< 5秒
- 进度更新时间：< 1秒
- 节点检验时间：< 3秒
- 报告生成时间：< 5秒
- 统计计算时间：< 2秒

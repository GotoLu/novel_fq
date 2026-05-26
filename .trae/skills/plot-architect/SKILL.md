---
name: "plot-architect"
description: "Architects plot structure, world-building, and foreshadowing systems for novels. Invoke when designing story structure, creating chapter outlines, or planning plot progression and foreshadowing."
---

# Plot Architect Skill

## 功能定义

情节架构技能，专注于小说情节结构设计、世界观构建和伏笔体系规划。

**单一职责**：仅负责情节架构设计，不涉及人物设计、内容写作等其他环节。

---

## 输入参数

```json
{
  "action": "design_structure | build_world | create_outline | design_foreshadowing | check_plot_logic",
  "params": {
    "structure_type": "three_act | four_act | multi_volume",
    "total_words": 1000000,
    "world_data": {
      "type": "fantasy | urban | sci-fi",
      "core_settings": {},
      "power_system": {},
      "social_structure": {}
    },
    "outline_level": "volume | chapter | scene",
    "foreshadowing_data": {
      "content": "xxx",
      "plant_chapter": 5,
      "reveal_chapter": 50,
      "importance": "high | medium | low"
    },
    "logic_check_range": {
      "start_chapter": 1,
      "end_chapter": 100
    }
  }
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 执行动作类型 |
| params.structure_type | string | 否 | 结构类型 |
| params.total_words | number | 否 | 总字数 |
| params.world_data | object | 否 | 世界观数据 |
| params.outline_level | string | 否 | 大纲层级 |
| params.foreshadowing_data | object | 否 | 伏笔数据 |
| params.logic_check_range | object | 否 | 逻辑检查范围 |

---

## 输出结果

```json
{
  "status": "success | error",
  "data": {
    "structure_design": {
      "type": "three_act",
      "acts": [
        {
          "name": "第一幕：建置",
          "percentage": 25,
          "word_count": 250000,
          "purpose": "建立人物、设定、冲突"
        }
      ],
      "climax_distribution": [],
      "turning_points": []
    },
    "world_building": {
      "type": "fantasy",
      "core_settings": {
        "time_space": "xxx",
        "power_system": "xxx",
        "rules": "xxx"
      },
      "social_structure": {
        "forces": [],
        "hierarchy": "xxx"
      },
      "environment": {
        "geography": "xxx",
        "important_locations": []
      }
    },
    "outline": {
      "volumes": [
        {
          "volume_id": 1,
          "name": "xxx",
          "theme": "xxx",
          "word_count": 200000,
          "chapters": 50,
          "core_events": [],
          "character_growth": "xxx"
        }
      ],
      "chapters": [
        {
          "chapter_id": 1,
          "title": "xxx",
          "word_count": 3000,
          "core_event": "xxx",
          "conflict": "xxx",
          "foreshadowing": [],
          "cliffhanger": "xxx"
        }
      ]
    },
    "foreshadowing_system": {
      "foreshadowings": [
        {
          "id": "fs_001",
          "content": "xxx",
          "plant_chapter": 5,
          "hints": [15, 30],
          "reveal_chapter": 50,
          "importance": "high",
          "status": "planted | hinted | revealed"
        }
      ],
      "statistics": {
        "total": 20,
        "planted": 15,
        "revealed": 5,
        "completion_rate": 25
      }
    },
    "logic_check_result": {
      "is_logical": true,
      "issues": [],
      "suggestions": []
    }
  },
  "errors": []
}
```

---

## 执行逻辑

### 1. 结构设计 (design_structure)

**执行步骤**：
```
1. 确定结构类型
    - 三幕式
    - 四幕式
    - 多卷结构
    ↓
2. 计算各部分占比
    ↓
3. 规划高潮分布
    - 高潮数量
    - 高潮间隔
    - 高潮强度递增
    ↓
4. 设计转折节点
    - 大转折
    - 中转折
    - 小转折
    ↓
5. 规划节奏分布
    - 张弛比例
    - 信息密度
    ↓
6. 生成结构设计
    ↓
7. 返回设计结果
```

---

### 2. 世界观构建 (build_world)

**执行步骤**：
```
1. 确定世界类型
    ↓
2. 设计核心设定
    - 时空背景
    - 力量体系
    - 核心规则
    ↓
3. 设计社会结构
    - 势力组织
    - 阶层划分
    - 权力结构
    ↓
4. 设计环境设定
    - 地理环境
    - 重要地点
    - 环境特色
    ↓
5. 设计其他设定
    - 经济体系
    - 文化习俗
    - 历史背景
    ↓
6. 验证设定自洽性
    ↓
7. 生成世界观文档
    ↓
8. 返回构建结果
```

---

### 3. 大纲创建 (create_outline)

**执行步骤**：
```
1. 确定大纲层级
    - 分卷大纲
    - 分章大纲
    - 场景大纲
    ↓
2. 创建分卷大纲
    - 卷名主题
    - 核心事件
    - 人物成长
    - 字数规划
    ↓
3. 创建分章大纲
    - 章节标题
    - 核心事件
    - 冲突设置
    - 推进目标
    - 字数规划
    ↓
4. 标注关键节点
    - 高潮点
    - 转折点
    - 伏笔点
    ↓
5. 生成大纲文档
    ↓
6. 返回大纲结果
```

---

### 4. 伏笔体系设计 (design_foreshadowing)

**执行步骤**：
```
1. 识别需要伏笔的情节
    ↓
2. 设计伏笔内容
    ↓
3. 规划埋设位置
    ↓
4. 规划暗示次数和位置
    ↓
5. 规划揭示位置和方式
    ↓
6. 评估伏笔重要性
    ↓
7. 建立伏笔清单
    ↓
8. 返回伏笔体系
```

---

### 5. 情节逻辑检查 (check_plot_logic)

**执行步骤**：
```
1. 确定检查范围
    ↓
2. 检查情节连贯性
    - 因果关系
    - 时间顺序
    - 空间逻辑
    ↓
3. 检查设定一致性
    - 前后设定对比
    - 规则一致性
    ↓
4. 检查人物行为合理性
    ↓
5. 识别逻辑问题
    ↓
6. 生成问题报告
    ↓
7. 提出修正建议
    ↓
8. 返回检查结果
```

---

## 错误处理机制

### 错误类型

| 错误码 | 错误描述 | 处理方式 |
|--------|---------|---------|
| INVALID_ACTION | 无效的动作类型 | 返回错误，提示有效动作 |
| STRUCTURE_INCOMPATIBLE | 结构与字数不匹配 | 调整结构或字数 |
| WORLD_INCONSISTENT | 世界观不自洽 | 返回矛盾点 |
| OUTLINE_INCOMPLETE | 大纲不完整 | 提示缺失部分 |
| FORESHADOWING_CONFLICT | 伏笔冲突 | 返回冲突详情 |
| LOGIC_ERROR | 逻辑错误 | 返回错误位置和修正建议 |

---

## 调用接口规范

### 被调用接口

本skill可被以下skill调用：
- `content-writer`：提供情节大纲和世界观
- `quality-evaluator`：提供情节数据用于评估
- `progress-tracker`：提交情节设计阶段完成

### 调用其他skill

本skill可调用以下skill获取辅助信息：
- `idea-generator`：获取核心创意和冲突
- `character-designer`：获取人物信息和关系

---

## 使用示例

### 示例1：设计结构

```json
输入：
{
  "action": "design_structure",
  "params": {
    "structure_type": "three_act",
    "total_words": 1000000
  }
}

输出：
{
  "status": "success",
  "data": {
    "structure_design": {
      "type": "three_act",
      "acts": [
        {
          "name": "第一幕：建置",
          "percentage": 25,
          "word_count": 250000
        }
      ]
    }
  }
}
```

---

## 注意事项

1. **结构服务冲突**：结构要服务于核心冲突
2. **节奏张弛有度**：高潮低谷分布合理
3. **伏笔系统规划**：埋设和回收要系统规划
4. **逻辑自洽**：设定和情节要前后一致
5. **大纲弹性**：大纲要有一定弹性，允许调整

---

## 依赖资源

- 结构模板库
- 世界观设定模板
- 大纲模板
- 伏笔管理工具
- 逻辑检查规则

---

## 性能指标

- 结构设计时间：< 5分钟
- 世界观构建时间：< 30分钟
- 分卷大纲创建时间：< 20分钟
- 分章大纲创建时间：< 2分钟/章
- 伏笔体系设计时间：< 10分钟
- 逻辑检查时间：< 1分钟/章节

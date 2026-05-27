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
- 情节逻辑分析
- 设定一致性检查
- 伏笔合理性评估
- 大纲逻辑检查

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
- 大纲修改方案选择
- 章节标题优化
- 伏笔埋设位置确定
- 案件难度设定
- 人物成长轨迹设计

---

## 注意事项

1. **结构服务冲突**：结构要服务于核心冲突
2. **节奏张弛有度**：高潮低谷分布合理
3. **伏笔系统规划**：埋设和回收要系统规划
4. **逻辑自洽**：设定和情节要前后一致
5. **大纲弹性**：大纲要有一定弹性，允许调整
6. **核心原则优先**：客观中立原则 > 最优决策原则 > 其他注意事项

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

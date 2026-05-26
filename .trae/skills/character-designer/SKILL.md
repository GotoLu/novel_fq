---
name: "character-designer"
description: "Designs and develops novel characters including protagonist, supporting characters, and antagonists. Invoke when creating character profiles, defining character arcs, or establishing character relationships."
---

# Character Designer Skill

## 功能定义

人物设计技能，专注于小说人物的塑造和关系设计，确保人物的立体性和一致性。

**单一职责**：仅负责人物的设计和关系构建，不涉及情节设计、内容创作等其他环节。

---

## 输入参数

```json
{
  "action": "design_protagonist | design_supporting | design_antagonist | build_relationships | check_consistency",
  "params": {
    "character_type": "protagonist | supporting | antagonist",
    "character_data": {
      "name": "xxx",
      "age": 25,
      "gender": "male",
      "personality_traits": ["勇敢", "聪明", "固执"],
      "background": "xxx",
      "abilities": "xxx",
      "goals": {
        "external": "xxx",
        "internal": "xxx"
      },
      "fears": "xxx",
      "arc": {
        "start_state": "xxx",
        "growth_path": "xxx",
        "end_state": "xxx"
      }
    },
    "relationship_type": "ally | enemy | mentor | rival",
    "consistency_check_range": {
      "start_chapter": 1,
      "end_chapter": 50
    }
  }
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 执行动作类型 |
| params.character_type | string | 否 | 人物类型 |
| params.character_data | object | 否 | 人物数据 |
| params.relationship_type | string | 否 | 关系类型 |
| params.consistency_check_range | object | 否 | 一致性检查范围 |

---

## 输出结果

```json
{
  "status": "success | error",
  "data": {
    "character_profile": {
      "id": "char_001",
      "name": "xxx",
      "type": "protagonist",
      "basic_info": {
        "age": 25,
        "gender": "male",
        "appearance": "xxx"
      },
      "personality": {
        "core_traits": ["勇敢", "聪明", "固执"],
        "strengths": ["xxx"],
        "weaknesses": ["xxx"],
        "contradictions": ["xxx"]
      },
      "background_story": "xxx",
      "abilities": {
        "initial": "xxx",
        "golden_finger": "xxx",
        "growth_path": "xxx"
      },
      "motivation": {
        "external_goal": "xxx",
        "internal_need": "xxx",
        "core_fear": "xxx",
        "values": "xxx"
      },
      "arc": {
        "start_state": "xxx",
        "growth_trajectory": "xxx",
        "key_turning_points": [],
        "end_state": "xxx"
      },
      "empathy_design": {
        "empathy_points": [],
        "care_points": [],
        "expectation_points": []
      }
    },
    "relationship_network": {
      "characters": [],
      "relationships": [
        {
          "from": "char_001",
          "to": "char_002",
          "type": "ally",
          "strength": 8,
          "development": "xxx"
        }
      ]
    },
    "consistency_report": {
      "is_consistent": true,
      "issues": [],
      "suggestions": []
    }
  },
  "errors": []
}
```

---

## 执行逻辑

### 1. 主角设计 (design_protagonist)

**执行步骤**：
```
1. 验证输入数据
    ↓
2. 设计基础信息
    - 姓名、年龄、性别、外貌
    - 身份背景
    ↓
3. 设计性格体系
    - 核心特质（3-5个）
    - 优点缺点
    - 矛盾点
    ↓
4. 设计背景故事
    - 成长经历
    - 关键事件
    - 心理创伤
    ↓
5. 设计能力体系
    - 初始能力
    - 金手指
    - 成长路径
    ↓
6. 设计动机体系
    - 外在目标
    - 内在需求
    - 核心恐惧
    - 价值观
    ↓
7. 设计人物弧光
    - 起点状态
    - 成长轨迹
    - 关键转折点
    - 终点状态
    ↓
8. 设计代入感
    - 共情点
    - 认同点
    - 关心点
    ↓
9. 生成人物档案
    ↓
10. 返回设计结果
```

---

### 2. 配角设计 (design_supporting)

**执行步骤**：
```
1. 验证输入数据
    ↓
2. 确定角色功能
    - 导师型
    - 盟友型
    - 对手型
    - 功能型
    ↓
3. 设计基础信息
    ↓
4. 设计性格特点
    ↓
5. 设计与主角关系
    - 关系类型
    - 关系发展
    - 互动模式
    ↓
6. 设计出场规划
    - 首次出场
    - 活跃期
    - 退场/转化
    ↓
7. 设计人物发展
    - 是否有成长
    - 命运走向
    ↓
8. 生成人物档案
    ↓
9. 返回设计结果
```

---

### 3. 反派设计 (design_antagonist)

**执行步骤**：
```
1. 验证输入数据
    ↓
2. 设计基础信息
    ↓
3. 设计动机体系
    - 表面动机
    - 深层动机
    - 价值观
    - 动机合理性
    ↓
4. 设计能力体系
    - 能力水平
    - 与主角对比
    - 威胁程度
    - 弱点
    ↓
5. 设计与主角冲突
    - 冲突本质
    - 冲突层次
    - 冲突升级
    ↓
6. 设计反派层次
    - 人物复杂度
    - 转化可能
    - 人性展现
    ↓
7. 设计行动轨迹
    - 阶段性目标
    - 行动计划
    - 冲突节点
    ↓
8. 生成人物档案
    ↓
9. 返回设计结果
```

---

### 4. 关系网络构建 (build_relationships)

**执行步骤**：
```
1. 收集所有人物
    ↓
2. 识别关系类型
    - 盟友关系
    - 敌对关系
    - 恋爱关系
    - 师徒关系
    - 竞争关系
    ↓
3. 设计关系强度
    ↓
4. 设计关系发展
    - 初始关系
    - 关系变化
    - 最终关系
    ↓
5. 设计互动模式
    ↓
6. 生成关系网络图
    ↓
7. 返回关系网络
```

---

### 5. 一致性检查 (check_consistency)

**执行步骤**：
```
1. 确定检查范围
    ↓
2. 逐章检查
    - 性格一致性
    - 行为逻辑性
    - 能力一致性
    - 关系发展合理性
    ↓
3. 识别不一致问题
    ↓
4. 生成问题报告
    ↓
5. 提出修正建议
    ↓
6. 返回检查结果
```

---

## 错误处理机制

### 错误类型

| 错误码 | 错误描述 | 处理方式 |
|--------|---------|---------|
| INVALID_ACTION | 无效的动作类型 | 返回错误，提示有效动作 |
| MISSING_REQUIRED_FIELDS | 缺少必要字段 | 返回错误，提示缺少的字段 |
| INCONSISTENT_CHARACTER | 人物不一致 | 返回问题列表和修正建议 |
| INVALID_RELATIONSHIP | 无效的关系定义 | 返回错误，提示有效关系类型 |
| ARC_NOT_COMPLETE | 人物弧光不完整 | 返回错误，提示缺失部分 |

---

## 调用接口规范

### 被调用接口

本skill可被以下skill调用：
- `plot-architect`：提供人物信息用于情节设计
- `content-writer`：提供人物设定用于写作
- `quality-evaluator`：提供人物数据用于评估
- `progress-tracker`：提交人物设计阶段完成

### 调用其他skill

本skill可调用以下skill获取辅助信息：
- `idea-generator`：获取核心创意和冲突信息

---

## 使用示例

### 示例1：设计主角

```json
输入：
{
  "action": "design_protagonist",
  "params": {
    "character_data": {
      "name": "林风",
      "age": 18,
      "gender": "male",
      "personality_traits": ["勇敢", "聪明", "重情义"],
      "background": "小家族庶子，受尽冷眼"
    }
  }
}

输出：
{
  "status": "success",
  "data": {
    "character_profile": {
      "id": "char_001",
      "name": "林风",
      "type": "protagonist",
      "personality": {
        "core_traits": ["勇敢", "聪明", "重情义"]
      }
    }
  }
}
```

---

## 注意事项

1. **主角优先**：主角设计最详细，是代入感核心
2. **功能明确**：每个配角都有明确功能，避免冗余
3. **关系张力**：人物关系要有冲突和张力
4. **一致性**：定期检查人物一致性
5. **成长空间**：主要人物要有成长弧线

---

## 依赖资源

- 人物设定模板
- 人物关系模型
- 一致性检查规则
- 人物数据库

---

## 性能指标

- 主角设计时间：< 10分钟
- 配角设计时间：< 5分钟/角色
- 反派设计时间：< 8分钟
- 关系网络构建时间：< 5分钟
- 一致性检查时间：< 1分钟/章节

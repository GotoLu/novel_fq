---
name: "problem-solver"
description: "Diagnoses and resolves common writing problems like plot blocks, character issues, or pacing problems. Invoke when encountering creative blocks, quality issues, or when specific writing problems need systematic solutions."
---

# Problem Solver Skill

## 功能定义

问题解决技能，专注于创作过程中常见问题的诊断和解决，提供系统化的问题处理方案。

**单一职责**：仅负责问题的诊断和解决，不涉及内容创作、质量评估等其他环节。

---

## 输入参数

```json
{
  "action": "diagnose_problem | solve_problem | prevent_problem | get_solution_library",
  "params": {
    "problem_type": "idea_block | character_flat | plot_stuck | pacing_issue | logic_error | language_issue | opening_fail | middle_collapse | ending_fail",
    "problem_description": "xxx",
    "context": {
      "current_chapter": 50,
      "problem_location": "第50章",
      "related_content": "xxx"
    },
    "diagnosis_depth": "quick | standard | deep",
    "solution_preference": "conservative | moderate | aggressive"
  }
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 执行动作类型 |
| params.problem_type | string | 否 | 问题类型 |
| params.problem_description | string | 否 | 问题描述 |
| params.context | object | 否 | 问题上下文 |
| params.diagnosis_depth | string | 否 | 诊断深度 |
| params.solution_preference | string | 否 | 解决方案偏好 |

---

## 输出结果

```json
{
  "status": "success | error",
  "data": {
    "diagnosis": {
      "problem_type": "plot_stuck",
      "problem_name": "情节卡顿",
      "severity": "medium",
      "root_causes": [
        {
          "cause": "大纲不够详细",
          "probability": 0.8,
          "impact": "high"
        },
        {
          "cause": "冲突设置不足",
          "probability": 0.7,
          "impact": "medium"
        }
      ],
      "symptoms": [
        "写不下去，不知道怎么推进",
        "情节停滞不前"
      ]
    },
    "solutions": [
      {
        "id": "sol_001",
        "name": "细化大纲",
        "description": "回到大纲，明确推进目标，设计多个推进路径",
        "steps": [
          "回顾大纲设计",
          "明确当前推进目标",
          "设计3个可能的推进路径",
          "选择最优路径"
        ],
        "effectiveness": 0.85,
        "difficulty": "easy",
        "time_cost": "10分钟",
        "risk": "low"
      },
      {
        "id": "sol_002",
        "name": "增加冲突",
        "description": "设置新的冲突或升级现有冲突",
        "steps": [
          "识别当前冲突状态",
          "设计新冲突或升级现有冲突",
          "确保冲突推动情节"
        ],
        "effectiveness": 0.80,
        "difficulty": "medium",
        "time_cost": "15分钟",
        "risk": "low"
      }
    ],
    "recommended_solution": {
      "solution_id": "sol_001",
      "reason": "效果最好，难度最低，风险最小",
      "implementation_guide": "详细实施步骤..."
    },
    "prevention_measures": [
      "创作前确保大纲足够详细",
      "定期回顾大纲，及时调整",
      "保持冲突的持续性"
    ]
  },
  "errors": []
}
```

---

## 执行逻辑

### 1. 问题诊断 (diagnose_problem)

**执行步骤**：
```
1. 识别问题类型
    ↓
2. 收集问题上下文
    ↓
3. 分析问题表现
    ↓
4. 识别根本原因
    - 多原因分析
    - 概率评估
    - 影响评估
    ↓
5. 评估问题严重性
    ↓
6. 生成诊断报告
    ↓
7. 返回诊断结果
```

---

### 2. 问题解决 (solve_problem)

**执行步骤**：
```
1. 获取诊断结果
    ↓
2. 检索解决方案库
    ↓
3. 匹配适用方案
    ↓
4. 评估方案效果
    - 有效性
    - 难度
    - 时间成本
    - 风险
    ↓
5. 推荐最优方案
    ↓
6. 生成实施指南
    ↓
7. 返回解决方案
```

---

### 3. 问题预防 (prevent_problem)

**执行步骤**：
```
1. 识别潜在问题
    ↓
2. 分析问题成因
    ↓
3. 设计预防措施
    ↓
4. 生成预防清单
    ↓
5. 返回预防方案
```

---

### 4. 获取解决方案库 (get_solution_library)

**执行步骤**：
```
1. 确定问题类型
    ↓
2. 检索解决方案库
    ↓
3. 返回相关方案
```

---

## 常见问题类型

### 1. 创意阶段问题

#### 创意枯竭 (idea_block)
**表现**：想不出好的创意，灵感枯竭  
**原因**：输入不足、方法不当、心理障碍  
**解决方案**：
- 扩大输入（大量阅读、跨领域学习）
- 使用创意激发方法（What-if、组合、反转、跨界）
- 降低心理门槛，先求数量再求质量

#### 创意平庸 (idea_mediocre)
**表现**：创意缺乏新意，套路化严重  
**原因**：输入同质化、思维定势  
**解决方案**：
- 跨类型学习借鉴
- 打破思维定势
- 增加创新维度

---

### 2. 人物塑造问题

#### 人物扁平 (character_flat)
**表现**：人物性格单一，脸谱化  
**原因**：性格维度不足、缺乏矛盾性  
**解决方案**：
- 增加3-5个核心性格特质
- 设计性格矛盾点
- 完善背景故事
- 设计人物弧光

#### 代入感弱 (empathy_weak)
**表现**：读者难以代入主角  
**原因**：主角魅力不足、缺乏共情点  
**解决方案**：
- 强化主角魅力
- 建立共情点
- 优化开篇代入建立
- 调整主角行为

---

### 3. 情节构建问题

#### 情节卡顿 (plot_stuck)
**表现**：写不下去，不知道怎么推进  
**原因**：大纲不够详细、冲突不足  
**解决方案**：
- 细化大纲，明确推进目标
- 增加冲突或升级现有冲突
- 调整方向，寻找新路径

#### 节奏失衡 (pacing_issue)
**表现**：节奏过快或过慢，张弛混乱  
**原因**：缺乏节奏规划、情节推进不当  
**解决方案**：
- 重新规划节奏曲线
- 调整推进速度
- 优化信息密度
- 调整冲突设置

#### 逻辑混乱 (logic_error)
**表现**：情节前后矛盾，因果关系不清  
**原因**：大纲逻辑问题、忘记设定  
**解决方案**：
- 梳理情节逻辑链
- 建立设定文档
- 逻辑修正
- 简化设定

---

### 4. 语言表达问题

#### 语言生涩 (language_issue)
**表现**：语言不流畅，阅读有阻滞感  
**原因**：文字功底不足、缺乏打磨  
**解决方案**：
- 提升文字功底
- 多次修改润色
- 多样化表达
- 追求自然流畅

---

### 5. 整体问题

#### 开篇失败 (opening_fail)
**表现**：开篇劝退读者，代入感建立失败  
**原因**：节奏不当、信息密度失衡  
**解决方案**：
- 优化开篇节奏
- 调整信息密度
- 强化代入感
- 设置悬念

#### 中期崩盘 (middle_collapse)
**表现**：中期质量下滑，读者流失  
**原因**：大纲执行不力、创作疲劳  
**解决方案**：
- 回归大纲
- 克服疲劳
- 坚守核心创意
- 及时修正问题

#### 结尾烂尾 (ending_fail)
**表现**：结尾仓促，伏笔未回收  
**原因**：创作疲劳、规划不当  
**解决方案**：
- 充分准备结尾
- 系统检查完整性
- 精心打磨
- 从读者角度审视

---

## 错误处理机制

### 错误类型

| 错误码 | 错误描述 | 处理方式 |
|--------|---------|---------|
| INVALID_ACTION | 无效的动作类型 | 返回错误，提示有效动作 |
| UNKNOWN_PROBLEM | 未知问题类型 | 提供问题类型列表 |
| INSUFFICIENT_CONTEXT | 上下文不足 | 提示需要的信息 |
| NO_SOLUTION_FOUND | 未找到解决方案 | 提供通用建议 |
| SOLUTION_FAILED | 解决方案失败 | 提供备选方案 |

---

## 调用接口规范

### 被调用接口

本skill可被以下skill调用：
- `content-writer`：解决写作过程中的问题
- `progress-tracker`：记录问题解决情况

### 调用其他skill

本skill可调用以下skill获取辅助信息：
- `quality-evaluator`：获取质量评估数据
- `plot-architect`：获取大纲数据
- `character-designer`：获取人物设定

---

## 使用示例

### 示例1：诊断问题

```json
输入：
{
  "action": "diagnose_problem",
  "params": {
    "problem_type": "plot_stuck",
    "problem_description": "写到第50章，不知道怎么继续推进了",
    "context": {
      "current_chapter": 50
    }
  }
}

输出：
{
  "status": "success",
  "data": {
    "diagnosis": {
      "problem_type": "plot_stuck",
      "root_causes": [...]
    },
    "solutions": [...]
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
- 问题诊断和分析
- 根本原因识别
- 解决方案评估
- 预防措施设计

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
- 解决方案选择
- 问题修复方案
- 预防措施选择
- 优先级排序

---

## 注意事项

1. **及时诊断**：问题发现后立即诊断，不拖延
2. **根本原因**：找到根本原因，不治标不治本
3. **最优方案**：直接提供最优解决方案，并说明依据
4. **预防为主**：重视问题预防，减少问题发生
5. **核心原则优先**：客观中立原则 > 最优决策原则 > 其他注意事项

---

## 依赖资源

- 问题诊断规则库
- 解决方案库
- 问题案例库
- 预防措施清单

---

## 性能指标

- 问题诊断时间：< 1分钟
- 解决方案生成时间：< 30秒
- 预防方案生成时间：< 30秒
- 方案库检索时间：< 5秒

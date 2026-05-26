---
name: "content-writer"
description: "Writes novel content including opening chapters, regular chapters, and climactic scenes. Invoke when writing actual novel text, controlling pacing, or crafting specific scenes and chapters."
---

# Content Writer Skill

## 功能定义

内容创作技能，专注于小说正文的写作，包括开篇、日常章节、高潮段落等。

**单一职责**：仅负责正文内容的创作，不涉及情节设计、质量评估等其他环节。

---

## 输入参数

```json
{
  "action": "write_opening | write_chapter | write_climax | control_pacing | check_quality",
  "params": {
    "chapter_number": 1,
    "chapter_title": "xxx",
    "word_count_target": 3000,
    "content_type": "opening | regular | climax | transition",
    "outline_data": {
      "core_event": "xxx",
      "conflict": "xxx",
      "characters": [],
      "foreshadowing": [],
      "cliffhanger": "xxx"
    },
    "pacing_type": "fast | medium | slow",
    "quality_check_level": "basic | standard | strict"
  }
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | 执行动作类型 |
| params.chapter_number | number | 否 | 章节编号 |
| params.chapter_title | string | 否 | 章节标题 |
| params.word_count_target | number | 否 | 目标字数 |
| params.content_type | string | 否 | 内容类型 |
| params.outline_data | object | 否 | 大纲数据 |
| params.pacing_type | string | 否 | 节奏类型 |
| params.quality_check_level | string | 否 | 质量检查级别 |

---

## 输出结果

```json
{
  "status": "success | error",
  "data": {
    "chapter_content": {
      "chapter_number": 1,
      "title": "xxx",
      "content": "正文内容...",
      "word_count": 3200,
      "content_type": "opening"
    },
    "pacing_analysis": {
      "tension_level": 7.5,
      "information_density": 8.0,
      "conflict_intensity": 6.5,
      "suggestion": "节奏适中，可适当加快"
    },
    "quality_check": {
      "overall_score": 8.5,
      "dimensions": {
        "language_fluency": 9.0,
        "character_consistency": 8.5,
        "plot_progression": 8.0,
        "emotional_impact": 8.5
      },
      "issues": [],
      "suggestions": []
    },
    "writing_statistics": {
      "actual_word_count": 3200,
      "target_word_count": 3000,
      "completion_rate": 106.7,
      "writing_time": "15分钟"
    }
  },
  "errors": []
}
```

---

## 执行逻辑

### 1. 开篇写作 (write_opening)

**执行步骤**：
```
1. 获取开篇大纲
    ↓
2. 设计开篇策略
    - 快速建立代入感
    - 展示主角魅力
    - 设置核心悬念
    ↓
3. 撰写第一章
    - 主角出场（前500字）
    - 建立代入点
    - 设置留钩
    ↓
4. 撰写第二章
    - 展示核心设定
    - 推进情节
    - 强化代入感
    ↓
5. 撰写第三章
    - 设置核心悬念
    - 强力留钩
    - 建立追读动力
    ↓
6. 质量检查
    - 代入感强度
    - 信息密度
    - 节奏控制
    ↓
7. 返回开篇内容
```

**开篇要点**：
- **第一章**：快速建立代入感，主角魅力展现
- **第二章**：展示核心设定，推进情节
- **第三章**：设置核心悬念，强力留钩

---

### 2. 章节写作 (write_chapter)

**执行步骤**：
```
1. 获取章节大纲
    ↓
2. 回顾前文
    - 前一章内容
    - 人物状态
    - 情节进展
    ↓
3. 确定写作要点
    - 核心事件
    - 冲突设置
    - 人物出场
    - 伏笔处理
    ↓
4. 撰写章节内容
    - 开头承接
    - 事件展开
    - 冲突发展
    - 结尾留钩
    ↓
5. 控制节奏
    - 信息密度
    - 张弛节奏
    - 情感强度
    ↓
6. 质量检查
    - 语言流畅度
    - 人物一致性
    - 情节推进
    ↓
7. 返回章节内容
```

---

### 3. 高潮写作 (write_climax)

**执行步骤**：
```
1. 获取高潮大纲
    ↓
2. 铺垫准备
    - 积累张力
    - 建立期待
    ↓
3. 设计高潮结构
    - 铺垫阶段
    - 爆发阶段
    - 延续阶段
    ↓
4. 撰写高潮内容
    - 冲突升级
    - 高潮爆发
    - 情感释放
    ↓
5. 控制节奏
    - 加快节奏
    - 提升张力
    - 强化情感
    ↓
6. 质量检查
    - 高潮强度
    - 情感冲击
    - 读者满意度
    ↓
7. 返回高潮内容
```

---

### 4. 节奏控制 (control_pacing)

**执行步骤**：
```
1. 分析当前节奏
    - 紧张度
    - 信息密度
    - 冲突强度
    ↓
2. 识别节奏问题
    - 过快/过慢
    - 过密/过稀
    - 张弛失衡
    ↓
3. 设计调整方案
    - 加快/放慢
    - 增加/减少信息
    - 调整张弛
    ↓
4. 实施调整
    ↓
5. 验证效果
    ↓
6. 返回调整结果
```

---

### 5. 质量检查 (check_quality)

**执行步骤**：
```
1. 确定检查级别
    - 基础检查
    - 标准检查
    - 严格检查
    ↓
2. 语言质量检查
    - 流畅度
    - 表达准确性
    - 句式多样性
    ↓
3. 内容质量检查
    - 人物一致性
    - 情节推进
    - 设定准确
    ↓
4. 效果检查
    - 吸引力
    - 情感冲击
    - 留钩效果
    ↓
5. 生成检查报告
    ↓
6. 返回检查结果
```

---

## 错误处理机制

### 错误类型

| 错误码 | 错误描述 | 处理方式 |
|--------|---------|---------|
| INVALID_ACTION | 无效的动作类型 | 返回错误，提示有效动作 |
| OUTLINE_NOT_FOUND | 大纲未找到 | 提示需要先创建大纲 |
| WORD_COUNT_MISMATCH | 字数不匹配 | 调整内容或目标字数 |
| PACING_ISSUE | 节奏问题 | 返回问题分析和调整建议 |
| QUALITY_BELOW_STANDARD | 质量不达标 | 返回问题和改进建议 |
| CHARACTER_INCONSISTENT | 人物不一致 | 返回不一致详情 |

---

## 调用接口规范

### 被调用接口

本skill可被以下skill调用：
- `quality-evaluator`：提供内容用于评估
- `problem-solver`：提供内容用于问题诊断
- `progress-tracker`：提交创作进度

### 调用其他skill

本skill可调用以下skill获取辅助信息：
- `plot-architect`：获取大纲和世界观
- `character-designer`：获取人物设定

---

## 使用示例

### 示例1：写作开篇

```json
输入：
{
  "action": "write_opening",
  "params": {
    "word_count_target": 10000,
    "outline_data": {
      "core_event": "主角获得金手指",
      "conflict": "主角vs家族压迫"
    }
  }
}

输出：
{
  "status": "success",
  "data": {
    "chapter_content": {
      "chapter_number": 1,
      "title": "第一章 觉醒",
      "content": "正文内容...",
      "word_count": 3200
    }
  }
}
```

---

## 注意事项

1. **黄金三章**：前三章务必精彩，决定作品生死
2. **保持连贯**：不断更、不烂尾
3. **质量稳定**：不因赶进度牺牲质量
4. **节奏控制**：张弛有度，信息密度适中
5. **人物一致**：保持人物性格和行为一致

---

## 依赖资源

- 大纲数据（来自plot-architect）
- 人物设定（来自character-designer）
- 写作技巧库
- 质量检查规则
- 语言模型（可选）

---

## 性能指标

- 开篇写作时间：30-60分钟（三章）
- 章节写作时间：15-30分钟/章
- 高潮写作时间：30-45分钟
- 节奏调整时间：< 5分钟
- 质量检查时间：< 3分钟/章

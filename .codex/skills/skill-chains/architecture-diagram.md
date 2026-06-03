# 全技能链架构图

## 一、总体架构

```text
用户任务
  |
  v
skill-chains 总控
  |
  +-- 判断阶段、交付物、前置资料、质量闸门
  |
  v
生产技能层
  |
  +-- market-analyzer      市场、平台、竞品、发布适配
  +-- idea-generator       创意、高概念、不可替代性
  +-- character-designer   人物、关系、群像轮转
  +-- plot-architect       结构、大纲、世界观、长篇资产
  +-- content-writer       正文、开篇、章节、高潮、风格
  |
  v
验收与修复层
  |
  +-- quality-evaluator    质量评分、硬性淘汰、版本对比
  +-- plagiarism-checker   原创性、相似度、风险定位
  +-- problem-solver       分诊、修复、保护项
  |
  v
记忆与周期层
  |
  +-- progress-tracker     节点、进度、反馈、资源账本记录
  |
  v
下一阶段 / 回退重做 / 发布完结
```

## 二、五阶段流向

```text
阶段一：市场与创意
progress-tracker
  -> market-analyzer
  -> idea-generator
  -> plagiarism-checker
  -> quality-evaluator
  -> progress-tracker

阶段二：人物与群像
idea-generator
  -> character-designer
  -> plot-architect 局部反查
  -> quality-evaluator
  -> progress-tracker

阶段三：结构与资产
character-designer
  -> plot-architect
  -> plagiarism-checker
  -> quality-evaluator
  -> problem-solver 必要修复
  -> progress-tracker

阶段四：正文生产
plot-architect
  -> character-designer
  -> content-writer
  -> quality-evaluator
  -> problem-solver 必要修复
  -> plagiarism-checker
  -> progress-tracker

阶段五：连载、发布与完结
progress-tracker
  -> quality-evaluator
  -> problem-solver
  -> 按问题回调生产技能
  -> plagiarism-checker
  -> market-analyzer 发布适配
  -> progress-tracker 归档
```

## 三、回退架构

```text
质量或原创性未通过
  |
  v
quality-evaluator / plagiarism-checker 定位问题
  |
  v
problem-solver 分诊
  |
  +-- 市场错位       -> market-analyzer
  +-- 创意平庸       -> idea-generator
  +-- 人物失真       -> character-designer
  +-- 情节塌陷       -> plot-architect
  +-- 正文不追读     -> content-writer
  +-- 相似风险       -> 对应生产技能重构
  +-- 长篇失控       -> progress-tracker + plot-architect
  |
  v
复评、复查重、记录版本
```

## 四、数据依赖

| 技能 | 依赖 | 输出给 |
|------|------|--------|
| `market-analyzer` | 用户需求、平台目标、竞品 | `idea-generator`、`content-writer`、发布链 |
| `idea-generator` | 市场定位、题材方向 | `character-designer`、`plot-architect`、`plagiarism-checker` |
| `character-designer` | 高概念、核心冲突 | `plot-architect`、`content-writer`、`quality-evaluator` |
| `plot-architect` | 创意、人物、市场节奏 | `content-writer`、`progress-tracker`、`quality-evaluator` |
| `content-writer` | 章节卡、人物状态、风格声明 | `quality-evaluator`、`plagiarism-checker`、`progress-tracker` |
| `quality-evaluator` | 任意产出 | `problem-solver`、`progress-tracker` |
| `problem-solver` | 质量报告、用户反馈 | 对应生产技能、`progress-tracker` |
| `plagiarism-checker` | 创意、设定、场景、文本 | 对应生产技能、`quality-evaluator` |
| `progress-tracker` | 全部阶段产出 | 下一阶段和周期复盘 |

## 五、核心闭环

```text
产出
  -> 质量验收
  -> 原创性验收
  -> 问题分诊
  -> 回退重做
  -> 进度记录
  -> 下一次产出
```

没有经过这个闭环的产出，只能算草稿，不能算技能链完成。

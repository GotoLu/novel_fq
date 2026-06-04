# 阶段一：市场与创意

本阶段目标是确定小说写给谁看、凭什么被点开、为什么不能被同类作品轻易替代。

## 调用链

`progress-tracker` → `market-analyzer` → `idea-generator` → `plagiarism-checker` → `quality-evaluator` → `progress-tracker`

## 技能分工

| 技能 | 职责 |
|------|------|
| `progress-tracker` | 初始化项目，记录平台、题材、读者、版本和决策依据 |
| `market-analyzer` | 分析平台、题材、竞品、读者预期和发布适配 |
| `idea-generator` | 生成创意池，筛选高概念，做不可替代性测试 |
| `plagiarism-checker` | 检查高概念、核心设定、卖点和桥段原创性风险 |
| `quality-evaluator` | 验收 P3、P11、P17 和原创性风险 |

## 必须交付

- 项目初始化记录。
- 目标平台和目标读者。
- 题材机会和竞品风险。
- 发布适配表。
- 创意候选池。
- 一句话高概念。
- 不可替代性测试结论。
- 原创性检查结论。

## 通过标准

- 高概念一句话能说清，且包含人物、冲突、差异化卖点。
- 平台读者明确，不是泛泛地说“喜欢爽文的人”。
- 竞品拆解能指出可借鉴点和必须避开的相似点。
- 创意通过替换主角、替换设定、替换冲突和同类替代测试。
- 原创性风险可控，或已完成重构方案。

## 回退规则

| 问题 | 回退 |
|------|------|
| 平台不清 | `market-analyzer` 重做平台和读者定位 |
| 卖点平庸 | `idea-generator` 重做高概念 |
| 创意像竞品 | `idea-generator` 和 `plagiarism-checker` 联合重构 |
| 发布方向不匹配 | `market-analyzer` 重做发布适配 |

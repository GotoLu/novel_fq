# 查重校验系统配置

## 📋 系统参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `max_attempts` | 3 | 最大重试次数 |
| `default_threshold` | 30 | 默认重复度阈值 |
| `similarity_precision` | 4 | 相似度精度（小数位） |
| `log_enabled` | true | 是否启用日志 |
| `log_filepath` | ./logs/plagiarism/ | 日志文件路径 |

---

## ⚖️ 阈值配置

### 默认阈值

| 内容类型 | 阈值 | 说明 |
|---------|------|------|
| idea | 40 | 创意方案需要新颖性，允许适度参考 |
| character | 35 | 人物设计需要独特性，避免雷同 |
| plot | 30 | 情节架构需要原创性，核心情节不能重复 |
| content | 25 | 正文内容需要高度原创，严格控制重复 |
| dialogue | 45 | 对话内容可适当参考常见表达 |
| description | 30 | 描写内容需要原创，避免照搬 |
| world_building | 35 | 世界观设定需要独特性 |
| chapter | 25 | 章节内容需要高度原创 |
| scene | 30 | 场景描写需要原创性 |

### 阈值调整规则

| 条件 | 调整幅度 | 说明 |
|------|---------|------|
| 内容长度 < 500字 | +5 | 短内容允许稍高重复 |
| 内容长度 < 1000字 | +2 | 中等内容微调 |
| 重试次数 > 0 | +2/次 | 每次重试放宽2分 |
| 内容类型 = dialogue | +10 | 对话内容更宽松 |
| 内容类型 = description | +5 | 描写内容适度宽松 |
| 重要性 = high | -5 | 重要内容更严格 |
| 重要性 = low | +5 | 次要内容更宽松 |

---

## 🔍 算法权重配置

### 默认权重

| 算法 | 权重 | 说明 |
|------|------|------|
| 余弦相似度 | 0.30 | 基于TF-IDF向量 |
| Jaccard相似度 | 0.25 | 基于集合交集 |
| 编辑距离 | 0.25 | 基于字符编辑 |
| N-gram相似度 | 0.20 | 基于连续字符 |

### 权重可调范围

| 算法 | 最小值 | 最大值 |
|------|--------|--------|
| 余弦相似度 | 0.20 | 0.40 |
| Jaccard相似度 | 0.15 | 0.35 |
| 编辑距离 | 0.15 | 0.35 |
| N-gram相似度 | 0.10 | 0.30 |

---

## 📊 分数等级定义

| 等级 | 分数范围 | 标签 | 颜色 | 操作 |
|------|---------|------|------|------|
| original | 0-10 | 完全原创 | 绿色 | 通过 |
| low | 11-30 | 低重复度 | 蓝色 | 通过 |
| medium | 31-50 | 中重复度 | 黄色 | 关注 |
| high | 51-70 | 高重复度 | 橙色 | 需修改 |
| critical | 71-100 | 严重重复 | 红色 | 必须修改 |

---

## 🔄 重造流程配置

### 重造触发条件

```
if (重复度分数 > 阈值) and (当前尝试次数 < 最大重试次数):
    触发重造
```

### 重造参数

| 参数 | 计算方式 | 说明 |
|------|---------|------|
| creativity_boost | attempt × 0.1 | 每次重试增加创造性 |
| target_score | threshold - 5 | 目标分数比阈值低5分 |
| creativity_level | 0.5 + attempt × 0.15 | 创造性级别 |

### 重造建议

| 分数范围 | 建议 |
|---------|------|
| > 60 | 需要大幅修改内容结构和表达方式；尝试从不同角度重新构思 |
| 40-60 | 需要调整部分内容和表达；增加原创性描述 |
| < 40 | 需要微调个别表述；替换相似词汇 |

---

## 📝 日志配置

### 日志类型

| 类型 | 说明 |
|------|------|
| check | 查重校验记录 |
| retry | 重试记录 |
| success | 成功记录 |
| failure | 失败记录 |

### 日志字段

#### check类型

| 字段 | 类型 | 说明 |
|------|------|------|
| timestamp | string | 时间戳 |
| session_id | string | 会话ID |
| skill_name | string | 技能名称 |
| content_type | string | 内容类型 |
| content_length | int | 内容长度 |
| content_hash | string | 内容哈希 |
| score | float | 重复度分数 |
| threshold | int | 阈值 |
| passed | bool | 是否通过 |
| max_similarity | float | 最大相似度 |
| similar_sources | array | 相似来源 |
| algorithm_scores | object | 各算法分数 |

#### retry类型

| 字段 | 类型 | 说明 |
|------|------|------|
| timestamp | string | 时间戳 |
| session_id | string | 会话ID |
| skill_name | string | 技能名称 |
| attempt | int | 尝试次数 |
| previous_score | float | 上次分数 |
| threshold | int | 阈值 |
| issues | array | 问题列表 |
| suggestions | array | 建议列表 |
| retry_params | object | 重试参数 |

---

## 🚀 使用配置示例

### 基本配置

```python
from plagiarism_checker import create_checker

checker = create_checker(
    max_attempts=3,
    log_dir='./logs/plagiarism/'
)
```

### 自定义阈值

```python
custom_thresholds = {
    'content': 20,  # 更严格
    'dialogue': 50,  # 更宽松
    'chapter': 22
}

checker = create_checker(
    max_attempts=5,
    custom_thresholds=custom_thresholds
)
```

### 动态调整阈值

```python
context = {
    'content_length': 3000,
    'retry_count': 1,
    'content_type': 'content',
    'importance': 'high'
}

adjusted_threshold = PlagiarismThreshold.adjust_threshold(
    base_threshold=30,
    context=context
)
```

---

## 📈 性能配置

### 算法优化

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| use_optimized_levenshtein | true | 使用优化的编辑距离算法 |
| ngram_size | 3 | N-gram大小 |
| max_similar_sources | 5 | 最大相似来源数量 |
| similarity_threshold | 0.3 | 记录相似来源的阈值 |

### 内存配置

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| max_cache_size | 1000 | 最大缓存条目 |
| enable_cache | true | 是否启用缓存 |

---

## ✅ 配置验证

- ✅ 阈值范围：0-100
- ✅ 权重总和：1.0
- ✅ 最大重试次数：≥ 1
- ✅ 日志目录：可写
- ✅ 算法参数：有效

---

**配置文档更新时间**：2026-05-26

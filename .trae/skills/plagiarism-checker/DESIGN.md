# 查重校验系统设计文档

## 📋 系统概述

本系统为skill链执行流程提供实时查重校验功能，确保每个技能环节输出的内容具有足够的原创性。

---

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        查重校验系统架构                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Skill执行 → 内容输出 → 查重校验 → 分数计算 → 阈值判断                       │
│      │           │           │           │           │                      │
│      │           │           │           │           ├─→ 通过 → 进入下一环节 │
│      │           │           │           │           │                      │
│      │           │           │           │           └─→ 不通过 → 回炉重造  │
│      │           │           │           │                   │              │
│      │           │           │           │                   ↓              │
│      │           │           │           │              重新执行Skill       │
│      │           │           │           │                   │              │
│      │           │           │           │                   ↓              │
│      │           │           │           │              再次查重校验        │
│      │           │           │           │                   │              │
│      │           │           │           │                   ↓              │
│      │           │           │           │              (循环直至达标)      │
│      │           │           │           │                                  │
│      └───────────┴───────────┴───────────┴──────────────────────────────────┤
│                              查重校验日志系统                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 文本相似度算法

### 算法选择

本系统采用多算法融合策略：

| 算法 | 权重 | 适用场景 | 说明 |
|------|------|---------|------|
| **余弦相似度** | 30% | 整体文本 | 基于TF-IDF向量的余弦相似度 |
| **Jaccard相似度** | 25% | 词汇层面 | 集合交集/并集 |
| **编辑距离** | 25% | 字符层面 | Levenshtein距离 |
| **N-gram相似度** | 20% | 局部匹配 | 连续N个字符的匹配度 |

### 算法实现

#### 1. 余弦相似度算法

```python
def cosine_similarity(text1, text2):
    """
    基于TF-IDF的余弦相似度计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
    
    Returns:
        float: 相似度分数 (0-1)
    """
    # 1. 文本预处理
    words1 = preprocess(text1)
    words2 = preprocess(text2)
    
    # 2. 构建词频向量
    all_words = set(words1) | set(words2)
    vector1 = [words1.count(word) for word in all_words]
    vector2 = [words2.count(word) for word in all_words]
    
    # 3. 计算余弦相似度
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = sum(a ** 2 for a in vector1) ** 0.5
    magnitude2 = sum(b ** 2 for b in vector2) ** 0.5
    
    if magnitude1 * magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)
```

#### 2. Jaccard相似度算法

```python
def jaccard_similarity(text1, text2):
    """
    Jaccard相似度计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
    
    Returns:
        float: 相似度分数 (0-1)
    """
    # 1. 分词
    words1 = set(preprocess(text1))
    words2 = set(preprocess(text2))
    
    # 2. 计算交集和并集
    intersection = words1 & words2
    union = words1 | words2
    
    # 3. 计算Jaccard相似度
    if len(union) == 0:
        return 0.0
    
    return len(intersection) / len(union)
```

#### 3. 编辑距离算法

```python
def levenshtein_distance(text1, text2):
    """
    Levenshtein编辑距离计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
    
    Returns:
        int: 编辑距离
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    return dp[m][n]

def levenshtein_similarity(text1, text2):
    """
    基于编辑距离的相似度计算
    
    Returns:
        float: 相似度分数 (0-1)
    """
    distance = levenshtein_distance(text1, text2)
    max_len = max(len(text1), len(text2))
    
    if max_len == 0:
        return 1.0
    
    return 1 - (distance / max_len)
```

#### 4. N-gram相似度算法

```python
def ngram_similarity(text1, text2, n=3):
    """
    N-gram相似度计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
        n: gram大小，默认3
    
    Returns:
        float: 相似度分数 (0-1)
    """
    # 1. 生成n-gram
    def get_ngrams(text, n):
        return set(text[i:i+n] for i in range(len(text) - n + 1))
    
    ngrams1 = get_ngrams(text1, n)
    ngrams2 = get_ngrams(text2, n)
    
    # 2. 计算交集和并集
    intersection = ngrams1 & ngrams2
    union = ngrams1 | ngrams2
    
    # 3. 计算相似度
    if len(union) == 0:
        return 0.0
    
    return len(intersection) / len(union)
```

### 综合相似度计算

```python
def calculate_similarity(text1, text2):
    """
    综合相似度计算（多算法融合）
    
    Args:
        text1: 待检测文本
        text2: 对比文本
    
    Returns:
        float: 综合相似度分数 (0-1)
    """
    # 各算法权重
    weights = {
        'cosine': 0.30,
        'jaccard': 0.25,
        'levenshtein': 0.25,
        'ngram': 0.20
    }
    
    # 计算各算法相似度
    scores = {
        'cosine': cosine_similarity(text1, text2),
        'jaccard': jaccard_similarity(text1, text2),
        'levenshtein': levenshtein_similarity(text1, text2),
        'ngram': ngram_similarity(text1, text2, n=3)
    }
    
    # 加权平均
    total_score = sum(weights[k] * scores[k] for k in weights)
    
    return total_score
```

---

## 📊 重复度分数生成

### 分数定义

| 分数范围 | 含义 | 说明 |
|---------|------|------|
| 0分 | 完全原创 | 与对比库无任何相似 |
| 1-30分 | 低重复度 | 存在少量相似，属于正常引用 |
| 31-60分 | 中重复度 | 存在较多相似，需要关注 |
| 61-90分 | 高重复度 | 大量相似，需要修改 |
| 91-100分 | 几乎重复 | 与已有内容高度重复 |

### 分数计算公式

```
重复度分数 = 综合相似度 × 100

其中：
- 综合相似度 = Σ(算法权重 × 算法相似度)
- 算法权重：余弦30% + Jaccard25% + 编辑距离25% + N-gram20%
```

### 分数生成实现

```python
def generate_plagiarism_score(content, comparison_library):
    """
    生成重复度分数
    
    Args:
        content: 待检测内容
        comparison_library: 对比库（已有内容集合）
    
    Returns:
        dict: {
            'score': 重复度分数 (0-100),
            'max_similarity': 最大相似度,
            'similar_sources': 相似来源列表,
            'algorithm_scores': 各算法分数
        }
    """
    max_similarity = 0
    similar_sources = []
    algorithm_scores = {
        'cosine': [],
        'jaccard': [],
        'levenshtein': [],
        'ngram': []
    }
    
    # 与对比库中每个内容计算相似度
    for source_id, source_content in comparison_library.items():
        similarity = calculate_similarity(content, source_content)
        
        if similarity > max_similarity:
            max_similarity = similarity
        
        if similarity > 0.3:  # 记录相似度超过30%的来源
            similar_sources.append({
                'source_id': source_id,
                'similarity': similarity
            })
        
        # 记录各算法分数
        algorithm_scores['cosine'].append(
            cosine_similarity(content, source_content)
        )
        algorithm_scores['jaccard'].append(
            jaccard_similarity(content, source_content)
        )
        algorithm_scores['levenshtein'].append(
            levenshtein_similarity(content, source_content)
        )
        algorithm_scores['ngram'].append(
            ngram_similarity(content, source_content, n=3)
        )
    
    # 计算重复度分数
    score = max_similarity * 100
    
    return {
        'score': round(score, 2),
        'max_similarity': round(max_similarity, 4),
        'similar_sources': sorted(similar_sources, 
                                  key=lambda x: x['similarity'], 
                                  reverse=True)[:5],
        'algorithm_scores': {
            k: round(max(v), 4) if v else 0 
            for k, v in algorithm_scores.items()
        }
    }
```

---

## ⚖️ 阈值标准设定

### 默认阈值配置

| 内容类型 | 阈值 | 说明 |
|---------|------|------|
| 创意方案 | 40分 | 创意需要新颖性 |
| 人物设计 | 35分 | 人物需要独特性 |
| 情节架构 | 30分 | 情节需要原创性 |
| 正文内容 | 25分 | 正文需要高度原创 |
| 对话内容 | 45分 | 对话可适当参考 |

### 阈值配置实现

```python
class PlagiarismThreshold:
    """重复度阈值配置"""
    
    DEFAULT_THRESHOLDS = {
        'idea': 40,           # 创意方案
        'character': 35,      # 人物设计
        'plot': 30,           # 情节架构
        'content': 25,        # 正文内容
        'dialogue': 45,       # 对话内容
        'description': 30,    # 描写内容
        'world_building': 35  # 世界观设定
    }
    
    @classmethod
    def get_threshold(cls, content_type):
        """获取指定内容类型的阈值"""
        return cls.DEFAULT_THRESHOLDS.get(content_type, 30)
    
    @classmethod
    def set_threshold(cls, content_type, threshold):
        """设置指定内容类型的阈值"""
        if 0 <= threshold <= 100:
            cls.DEFAULT_THRESHOLDS[content_type] = threshold
        else:
            raise ValueError("阈值必须在0-100之间")
```

### 动态阈值调整

```python
def adjust_threshold(base_threshold, context):
    """
    根据上下文动态调整阈值
    
    Args:
        base_threshold: 基础阈值
        context: 上下文信息
    
    Returns:
        int: 调整后的阈值
    """
    adjusted = base_threshold
    
    # 1. 根据内容长度调整
    if context.get('content_length', 0) < 500:
        adjusted += 5  # 短内容允许稍高重复
    
    # 2. 根据重试次数调整
    retry_count = context.get('retry_count', 0)
    if retry_count > 0:
        adjusted += retry_count * 2  # 每次重试放宽2分
    
    # 3. 根据内容类型调整
    if context.get('content_type') == 'dialogue':
        adjusted += 10  # 对话内容更宽松
    
    # 确保不超过上限
    return min(adjusted, 70)
```

---

## 🔄 回炉重造流程

### 流程设计

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          回炉重造流程                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. 检测到重复度超标                                                         │
│      ↓                                                                      │
│  2. 记录当前结果和分数                                                       │
│      ↓                                                                      │
│  3. 判断是否达到最大重试次数                                                 │
│      │                                                                      │
│      ├─→ 是 → 使用当前最佳结果 + 人工标记                                   │
│      │                                                                      │
│      └─→ 否 → 继续重造                                                      │
│              ↓                                                              │
│         4. 生成重造指令                                                      │
│              ↓                                                              │
│         5. 重新执行Skill                                                    │
│              ↓                                                              │
│         6. 再次查重校验                                                      │
│              ↓                                                              │
│         7. 循环直至达标或达到最大次数                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 重造指令生成

```python
def generate_retry_instruction(original_output, plagiarism_result, attempt):
    """
    生成重造指令
    
    Args:
        original_output: 原始输出
        plagiarism_result: 查重结果
        attempt: 当前尝试次数
    
    Returns:
        dict: 重造指令
    """
    instruction = {
        'action': 'retry',
        'attempt': attempt,
        'issues': [],
        'suggestions': []
    }
    
    # 1. 分析重复来源
    for source in plagiarism_result['similar_sources']:
        instruction['issues'].append(
            f"与来源 {source['source_id']} 相似度 {source['similarity']*100:.1f}%"
        )
    
    # 2. 生成修改建议
    if plagiarism_result['score'] > 60:
        instruction['suggestions'].append("需要大幅修改内容结构和表达方式")
    elif plagiarism_result['score'] > 40:
        instruction['suggestions'].append("需要调整部分内容和表达")
    else:
        instruction['suggestions'].append("需要微调个别表述")
    
    # 3. 添加重造参数
    instruction['retry_params'] = {
        'avoid_sources': [s['source_id'] for s in plagiarism_result['similar_sources']],
        'target_score': plagiarism_result['threshold'] - 5,  # 目标分数比阈值低5分
        'creativity_boost': attempt * 0.1  # 每次重试增加创造性
    }
    
    return instruction
```

### 重造流程实现

```python
class RetryMechanism:
    """回炉重造机制"""
    
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts
        self.attempt_history = []
    
    def execute_with_retry(self, skill, input_data, content_type, comparison_library):
        """
        带重试的执行
        
        Args:
            skill: 技能实例
            input_data: 输入数据
            content_type: 内容类型
            comparison_library: 对比库
        
        Returns:
            dict: 最终结果
        """
        attempt = 0
        best_result = None
        best_score = 100
        
        threshold = PlagiarismThreshold.get_threshold(content_type)
        
        while attempt < self.max_attempts:
            attempt += 1
            
            # 1. 执行技能
            if attempt == 1:
                output = skill.execute(input_data)
            else:
                # 重造时添加创造性参数
                retry_input = self._prepare_retry_input(
                    input_data, 
                    best_result, 
                    attempt
                )
                output = skill.execute(retry_input)
            
            # 2. 查重校验
            plagiarism_result = generate_plagiarism_score(
                output['content'],
                comparison_library
            )
            plagiarism_result['threshold'] = threshold
            plagiarism_result['attempt'] = attempt
            
            # 3. 记录历史
            self.attempt_history.append({
                'attempt': attempt,
                'output': output,
                'plagiarism_result': plagiarism_result
            })
            
            # 4. 判断是否达标
            if plagiarism_result['score'] <= threshold:
                return {
                    'status': 'success',
                    'output': output,
                    'plagiarism_score': plagiarism_result['score'],
                    'attempts': attempt
                }
            
            # 5. 记录最佳结果
            if plagiarism_result['score'] < best_score:
                best_score = plagiarism_result['score']
                best_result = output
            
            # 6. 生成重造指令
            retry_instruction = generate_retry_instruction(
                output,
                plagiarism_result,
                attempt
            )
            
            # 7. 日志记录
            log_retry_attempt(
                skill.__class__.__name__,
                attempt,
                plagiarism_result,
                retry_instruction
            )
        
        # 达到最大重试次数，返回最佳结果
        return {
            'status': 'max_attempts_reached',
            'output': best_result,
            'plagiarism_score': best_score,
            'attempts': self.max_attempts,
            'needs_manual_review': True
        }
    
    def _prepare_retry_input(self, original_input, previous_output, attempt):
        """准备重试输入"""
        retry_input = original_input.copy()
        
        # 添加重试参数
        retry_input['retry'] = {
            'attempt': attempt,
            'previous_output': previous_output,
            'creativity_boost': attempt * 0.1,
            'avoid_patterns': self._extract_patterns(previous_output)
        }
        
        return retry_input
    
    def _extract_patterns(self, output):
        """提取需要避免的模式"""
        # 提取高频词汇、句式等
        patterns = []
        content = output.get('content', '')
        
        # 简单实现：提取重复出现的短语
        words = content.split()
        for i in range(len(words) - 2):
            phrase = ' '.join(words[i:i+3])
            if content.count(phrase) > 1:
                patterns.append(phrase)
        
        return list(set(patterns))[:10]  # 最多10个模式
```

---

## 📝 查重校验日志系统

### 日志数据结构

```python
class PlagiarismLog:
    """查重校验日志"""
    
    def __init__(self):
        self.logs = []
        self.session_id = generate_session_id()
    
    def log_check(self, skill_name, content_type, content, result):
        """
        记录查重校验
        
        Args:
            skill_name: 技能名称
            content_type: 内容类型
            content: 内容
            result: 查重结果
        """
        log_entry = {
            'timestamp': get_timestamp(),
            'session_id': self.session_id,
            'skill_name': skill_name,
            'content_type': content_type,
            'content_length': len(content),
            'content_hash': hash_content(content),
            'score': result['score'],
            'threshold': result.get('threshold', 30),
            'passed': result['score'] <= result.get('threshold', 30),
            'max_similarity': result['max_similarity'],
            'similar_sources': result['similar_sources'],
            'algorithm_scores': result['algorithm_scores']
        }
        
        self.logs.append(log_entry)
        return log_entry
    
    def log_retry(self, skill_name, attempt, previous_result, retry_instruction):
        """
        记录重试
        
        Args:
            skill_name: 技能名称
            attempt: 尝试次数
            previous_result: 上次结果
            retry_instruction: 重试指令
        """
        log_entry = {
            'timestamp': get_timestamp(),
            'session_id': self.session_id,
            'type': 'retry',
            'skill_name': skill_name,
            'attempt': attempt,
            'previous_score': previous_result['score'],
            'threshold': previous_result.get('threshold', 30),
            'issues': retry_instruction['issues'],
            'suggestions': retry_instruction['suggestions']
        }
        
        self.logs.append(log_entry)
        return log_entry
    
    def get_summary(self):
        """获取日志摘要"""
        total_checks = len([l for l in self.logs if l.get('type') != 'retry'])
        total_retries = len([l for l in self.logs if l.get('type') == 'retry'])
        passed_checks = len([l for l in self.logs 
                           if l.get('type') != 'retry' and l.get('passed', False)])
        
        return {
            'session_id': self.session_id,
            'total_checks': total_checks,
            'passed_checks': passed_checks,
            'failed_checks': total_checks - passed_checks,
            'total_retries': total_retries,
            'pass_rate': passed_checks / total_checks if total_checks > 0 else 0
        }
    
    def export_logs(self, filepath):
        """导出日志"""
        import json
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.logs, f, ensure_ascii=False, indent=2)
```

### 日志格式示例

```json
{
  "timestamp": "2026-05-26T10:30:00Z",
  "session_id": "session_20260526_001",
  "skill_name": "content-writer",
  "content_type": "content",
  "content_length": 3500,
  "content_hash": "a1b2c3d4e5f6...",
  "score": 35.6,
  "threshold": 25,
  "passed": false,
  "max_similarity": 0.356,
  "similar_sources": [
    {
      "source_id": "chapter_001",
      "similarity": 0.356
    },
    {
      "source_id": "chapter_002",
      "similarity": 0.289
    }
  ],
  "algorithm_scores": {
    "cosine": 0.342,
    "jaccard": 0.312,
    "levenshtein": 0.398,
    "ngram": 0.356
  }
}
```

---

## 🔧 集成到Skill链

### Skill执行流程更新

```python
class SkillChainExecutor:
    """Skill链执行器（带查重校验）"""
    
    def __init__(self, plagiarism_checker=None):
        self.plagiarism_checker = plagiarism_checker or PlagiarismChecker()
        self.log = PlagiarismLog()
    
    def execute_skill(self, skill, input_data, content_type, comparison_library):
        """
        执行单个技能（带查重校验）
        
        Args:
            skill: 技能实例
            input_data: 输入数据
            content_type: 内容类型
            comparison_library: 对比库
        
        Returns:
            dict: 执行结果
        """
        # 1. 执行技能
        output = skill.execute(input_data)
        
        # 2. 查重校验
        plagiarism_result = generate_plagiarism_score(
            output['content'],
            comparison_library
        )
        
        # 3. 获取阈值
        threshold = PlagiarismThreshold.get_threshold(content_type)
        plagiarism_result['threshold'] = threshold
        
        # 4. 记录日志
        self.log.log_check(
            skill.__class__.__name__,
            content_type,
            output['content'],
            plagiarism_result
        )
        
        # 5. 判断是否需要重造
        if plagiarism_result['score'] > threshold:
            # 触发回炉重造
            retry_mechanism = RetryMechanism(max_attempts=3)
            result = retry_mechanism.execute_with_retry(
                skill,
                input_data,
                content_type,
                comparison_library
            )
            
            # 记录重试日志
            for attempt in range(1, result['attempts'] + 1):
                if attempt > 1:
                    self.log.log_retry(
                        skill.__class__.__name__,
                        attempt,
                        plagiarism_result,
                        {}
                    )
            
            return result
        else:
            return {
                'status': 'success',
                'output': output,
                'plagiarism_score': plagiarism_result['score'],
                'attempts': 1
            }
    
    def execute_chain(self, skills, input_data, comparison_library):
        """
        执行技能链
        
        Args:
            skills: 技能列表
            input_data: 输入数据
            comparison_library: 对比库
        
        Returns:
            dict: 执行结果
        """
        results = []
        current_data = input_data
        
        for i, skill in enumerate(skills):
            content_type = self._get_content_type(skill, i)
            
            result = self.execute_skill(
                skill,
                current_data,
                content_type,
                comparison_library
            )
            
            results.append(result)
            
            if result['status'] not in ['success', 'max_attempts_reached']:
                return {
                    'status': 'failed',
                    'failed_at': i,
                    'results': results
                }
            
            # 更新下一个技能的输入
            current_data = result['output']
        
        return {
            'status': 'success',
            'results': results,
            'log_summary': self.log.get_summary()
        }
    
    def _get_content_type(self, skill, index):
        """根据技能类型确定内容类型"""
        skill_name = skill.__class__.__name__
        
        type_mapping = {
            'IdeaGenerator': 'idea',
            'CharacterDesigner': 'character',
            'PlotArchitect': 'plot',
            'ContentWriter': 'content',
            'QualityEvaluator': 'content'
        }
        
        return type_mapping.get(skill_name, 'content')
```

---

## 📊 配置参数

### 系统配置

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `max_attempts` | 3 | 最大重试次数 |
| `default_threshold` | 30 | 默认重复度阈值 |
| `similarity_precision` | 4 | 相似度精度（小数位） |
| `log_enabled` | True | 是否启用日志 |
| `log_filepath` | ./logs/plagiarism/ | 日志文件路径 |

### 算法权重配置

| 算法 | 默认权重 | 可调范围 |
|------|---------|---------|
| 余弦相似度 | 0.30 | 0.20-0.40 |
| Jaccard相似度 | 0.25 | 0.15-0.35 |
| 编辑距离 | 0.25 | 0.15-0.35 |
| N-gram相似度 | 0.20 | 0.10-0.30 |

---

## 📝 使用示例

### 基本使用

```python
# 1. 初始化执行器
executor = SkillChainExecutor()

# 2. 准备数据
input_data = {
    'theme': '推理悬疑',
    'style': '幽默喜剧'
}

comparison_library = {
    'existing_chapter_1': '已有章节内容...',
    'existing_chapter_2': '已有章节内容...'
}

# 3. 执行技能
result = executor.execute_skill(
    skill=ContentWriter(),
    input_data=input_data,
    content_type='content',
    comparison_library=comparison_library
)

# 4. 查看结果
print(f"状态: {result['status']}")
print(f"重复度分数: {result['plagiarism_score']}")
print(f"尝试次数: {result['attempts']}")
```

### 查看日志摘要

```python
summary = executor.log.get_summary()
print(f"总检查次数: {summary['total_checks']}")
print(f"通过次数: {summary['passed_checks']}")
print(f"通过率: {summary['pass_rate']:.2%}")
```

---

## ✅ 系统验证

- ✅ 文本相似度算法实现（多算法融合）
- ✅ 重复度分数生成（0-100分）
- ✅ 阈值标准设定（可配置）
- ✅ 回炉重造流程（自动触发）
- ✅ 查重校验日志系统（完整记录）
- ✅ Skill链集成（无缝对接）

---

**文档创建时间**：2026-05-26  
**系统状态**：设计完成，待实现  
**下一步**：实现查重校验系统代码

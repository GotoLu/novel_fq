"""
查重校验系统 - 文本相似度算法实现

提供多种文本相似度计算算法，用于检测内容重复度。
"""

import re
from typing import Dict, List, Set, Tuple
from collections import Counter
from datetime import datetime
import hashlib
import json


def preprocess(text: str) -> List[str]:
    """
    文本预处理
    
    Args:
        text: 原始文本
    
    Returns:
        分词后的词列表
    """
    if not text:
        return []
    
    text = text.lower()
    text = re.sub(r'[^\w\s\u4e00-\u9fff]', '', text)
    
    if re.search(r'[\u4e00-\u9fff]', text):
        words = list(text)
    else:
        words = text.split()
    
    words = [w for w in words if len(w) > 0]
    
    return words


def cosine_similarity(text1: str, text2: str) -> float:
    """
    基于TF-IDF的余弦相似度计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
    
    Returns:
        相似度分数 (0-1)
    """
    words1 = preprocess(text1)
    words2 = preprocess(text2)
    
    if not words1 or not words2:
        return 0.0
    
    all_words = set(words1) | set(words2)
    
    if not all_words:
        return 0.0
    
    counter1 = Counter(words1)
    counter2 = Counter(words2)
    
    vector1 = [counter1.get(word, 0) for word in all_words]
    vector2 = [counter2.get(word, 0) for word in all_words]
    
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = sum(a ** 2 for a in vector1) ** 0.5
    magnitude2 = sum(b ** 2 for b in vector2) ** 0.5
    
    if magnitude1 * magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)


def jaccard_similarity(text1: str, text2: str) -> float:
    """
    Jaccard相似度计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
    
    Returns:
        相似度分数 (0-1)
    """
    words1 = set(preprocess(text1))
    words2 = set(preprocess(text2))
    
    if not words1 or not words2:
        return 0.0
    
    intersection = words1 & words2
    union = words1 | words2
    
    if len(union) == 0:
        return 0.0
    
    return len(intersection) / len(union)


def levenshtein_distance(text1: str, text2: str) -> int:
    """
    Levenshtein编辑距离计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
    
    Returns:
        编辑距离
    """
    m, n = len(text1), len(text2)
    
    if m == 0:
        return n
    if n == 0:
        return m
    
    prev_row = list(range(n + 1))
    
    for i in range(1, m + 1):
        curr_row = [i] + [0] * n
        
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                curr_row[j] = prev_row[j-1]
            else:
                curr_row[j] = min(prev_row[j], curr_row[j-1], prev_row[j-1]) + 1
        
        prev_row = curr_row
    
    return prev_row[n]


def levenshtein_similarity(text1: str, text2: str) -> float:
    """
    基于编辑距离的相似度计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
    
    Returns:
        相似度分数 (0-1)
    """
    if not text1 and not text2:
        return 1.0
    
    distance = levenshtein_distance(text1, text2)
    max_len = max(len(text1), len(text2))
    
    if max_len == 0:
        return 1.0
    
    return 1 - (distance / max_len)


def ngram_similarity(text1: str, text2: str, n: int = 3) -> float:
    """
    N-gram相似度计算
    
    Args:
        text1: 待检测文本
        text2: 对比文本
        n: gram大小，默认3
    
    Returns:
        相似度分数 (0-1)
    """
    def get_ngrams(text: str, n: int) -> Set[str]:
        if len(text) < n:
            return set()
        return set(text[i:i+n] for i in range(len(text) - n + 1))
    
    ngrams1 = get_ngrams(text1, n)
    ngrams2 = get_ngrams(text2, n)
    
    if not ngrams1 or not ngrams2:
        return 0.0
    
    intersection = ngrams1 & ngrams2
    union = ngrams1 | ngrams2
    
    if len(union) == 0:
        return 0.0
    
    return len(intersection) / len(union)


def calculate_similarity(text1: str, text2: str, 
                        weights: Dict[str, float] = None) -> float:
    """
    综合相似度计算（多算法融合）
    
    Args:
        text1: 待检测文本
        text2: 对比文本
        weights: 各算法权重
    
    Returns:
        综合相似度分数 (0-1)
    """
    if weights is None:
        weights = {
            'cosine': 0.30,
            'jaccard': 0.25,
            'levenshtein': 0.25,
            'ngram': 0.20
        }
    
    scores = {
        'cosine': cosine_similarity(text1, text2),
        'jaccard': jaccard_similarity(text1, text2),
        'levenshtein': levenshtein_similarity(text1, text2),
        'ngram': ngram_similarity(text1, text2, n=3)
    }
    
    total_score = sum(weights.get(k, 0) * v for k, v in scores.items())
    
    return total_score


def generate_plagiarism_score(content: str, 
                             comparison_library: Dict[str, str],
                             weights: Dict[str, float] = None) -> Dict:
    """
    生成重复度分数
    
    Args:
        content: 待检测内容
        comparison_library: 对比库（已有内容集合）
        weights: 算法权重
    
    Returns:
        包含重复度分数和相关信息的字典
    """
    if not content or not comparison_library:
        return {
            'score': 0.0,
            'max_similarity': 0.0,
            'similar_sources': [],
            'algorithm_scores': {}
        }
    
    max_similarity = 0.0
    similar_sources = []
    algorithm_scores = {
        'cosine': [],
        'jaccard': [],
        'levenshtein': [],
        'ngram': []
    }
    
    for source_id, source_content in comparison_library.items():
        if not source_content:
            continue
        
        similarity = calculate_similarity(content, source_content, weights)
        
        if similarity > max_similarity:
            max_similarity = similarity
        
        if similarity > 0.3:
            similar_sources.append({
                'source_id': source_id,
                'similarity': round(similarity, 4)
            })
        
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
    
    score = max_similarity * 100
    
    similar_sources = sorted(similar_sources, 
                            key=lambda x: x['similarity'], 
                            reverse=True)[:5]
    
    return {
        'score': round(score, 2),
        'max_similarity': round(max_similarity, 4),
        'similar_sources': similar_sources,
        'algorithm_scores': {
            k: round(max(v), 4) if v else 0.0
            for k, v in algorithm_scores.items()
        }
    }


def hash_content(content: str) -> str:
    """
    生成内容哈希值
    
    Args:
        content: 内容文本
    
    Returns:
        哈希值字符串
    """
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def get_timestamp() -> str:
    """
    获取当前时间戳
    
    Returns:
        ISO格式时间戳
    """
    return datetime.now().isoformat()


def generate_session_id() -> str:
    """
    生成会话ID
    
    Returns:
        会话ID字符串
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_suffix = hashlib.md5(str(datetime.now().timestamp()).encode()).hexdigest()[:6]
    return f"session_{timestamp}_{random_suffix}"


if __name__ == '__main__':
    text1 = "李大嘴是一个逻辑混乱的侦探，但他的错误推理总能歪打正着。"
    text2 = "李大嘴是个推理混乱的侦探，但他的歪理总能意外找到真相。"
    
    print("=== 文本相似度测试 ===")
    print(f"余弦相似度: {cosine_similarity(text1, text2):.4f}")
    print(f"Jaccard相似度: {jaccard_similarity(text1, text2):.4f}")
    print(f"编辑距离相似度: {levenshtein_similarity(text1, text2):.4f}")
    print(f"N-gram相似度: {ngram_similarity(text1, text2):.4f}")
    print(f"综合相似度: {calculate_similarity(text1, text2):.4f}")
    
    print("\n=== 重复度分数测试 ===")
    library = {
        'source1': text2,
        'source2': "这是一个完全不同的内容，没有任何相似之处。"
    }
    result = generate_plagiarism_score(text1, library)
    print(f"重复度分数: {result['score']}")
    print(f"最大相似度: {result['max_similarity']}")
    print(f"相似来源: {result['similar_sources']}")

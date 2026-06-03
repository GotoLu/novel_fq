"""
查重校验系统 - 阈值配置

定义不同内容类型的重复度阈值标准。
"""

from typing import Dict, Optional
from enum import Enum


class ContentType(Enum):
    """内容类型枚举"""
    IDEA = 'idea'
    CHARACTER = 'character'
    PLOT = 'plot'
    CONTENT = 'content'
    DIALOGUE = 'dialogue'
    DESCRIPTION = 'description'
    WORLD_BUILDING = 'world_building'
    CHAPTER = 'chapter'
    SCENE = 'scene'


class PlagiarismThreshold:
    """重复度阈值配置"""
    
    DEFAULT_THRESHOLDS: Dict[str, int] = {
        'idea': 40,
        'character': 35,
        'plot': 30,
        'content': 25,
        'dialogue': 45,
        'description': 30,
        'world_building': 35,
        'chapter': 25,
        'scene': 30
    }
    
    THRESHOLD_DESCRIPTIONS: Dict[str, str] = {
        'idea': '创意方案需要新颖性，允许适度参考',
        'character': '人物设计需要独特性，避免雷同',
        'plot': '情节架构需要原创性，核心情节不能重复',
        'content': '正文内容需要高度原创，严格控制重复',
        'dialogue': '对话内容可适当参考常见表达',
        'description': '描写内容需要原创，避免照搬',
        'world_building': '世界观设定需要独特性',
        'chapter': '章节内容需要高度原创',
        'scene': '场景描写需要原创性'
    }
    
    @classmethod
    def get_threshold(cls, content_type: str) -> int:
        """
        获取指定内容类型的阈值
        
        Args:
            content_type: 内容类型
        
        Returns:
            阈值分数
        """
        return cls.DEFAULT_THRESHOLDS.get(content_type, 30)
    
    @classmethod
    def set_threshold(cls, content_type: str, threshold: int) -> None:
        """
        设置指定内容类型的阈值
        
        Args:
            content_type: 内容类型
            threshold: 阈值分数
        
        Raises:
            ValueError: 阈值不在有效范围内
        """
        if not 0 <= threshold <= 100:
            raise ValueError("阈值必须在0-100之间")
        
        cls.DEFAULT_THRESHOLDS[content_type] = threshold
    
    @classmethod
    def get_description(cls, content_type: str) -> str:
        """
        获取内容类型的阈值说明
        
        Args:
            content_type: 内容类型
        
        Returns:
            说明文本
        """
        return cls.THRESHOLD_DESCRIPTIONS.get(
            content_type, 
            '默认内容类型，需要原创性'
        )
    
    @classmethod
    def get_all_thresholds(cls) -> Dict[str, Dict]:
        """
        获取所有阈值配置
        
        Returns:
            包含阈值和说明的字典
        """
        return {
            content_type: {
                'threshold': threshold,
                'description': cls.THRESHOLD_DESCRIPTIONS.get(content_type, '')
            }
            for content_type, threshold in cls.DEFAULT_THRESHOLDS.items()
        }
    
    @classmethod
    def adjust_threshold(cls, 
                        base_threshold: int, 
                        context: Optional[Dict] = None) -> int:
        """
        根据上下文动态调整阈值
        
        Args:
            base_threshold: 基础阈值
            context: 上下文信息
        
        Returns:
            调整后的阈值
        """
        if context is None:
            context = {}
        
        adjusted = base_threshold
        
        content_length = context.get('content_length', 0)
        if content_length < 500:
            adjusted += 5
        elif content_length < 1000:
            adjusted += 2
        
        retry_count = context.get('retry_count', 0)
        if retry_count > 0:
            adjusted += retry_count * 2
        
        content_type = context.get('content_type', '')
        if content_type == 'dialogue':
            adjusted += 10
        elif content_type == 'description':
            adjusted += 5
        
        importance = context.get('importance', 'normal')
        if importance == 'high':
            adjusted -= 5
        elif importance == 'low':
            adjusted += 5
        
        return max(0, min(adjusted, 70))
    
    @classmethod
    def validate_threshold(cls, threshold: int) -> bool:
        """
        验证阈值是否有效
        
        Args:
            threshold: 阈值分数
        
        Returns:
            是否有效
        """
        return 0 <= threshold <= 100
    
    @classmethod
    def get_threshold_level(cls, threshold: int) -> str:
        """
        获取阈值严格程度等级
        
        Args:
            threshold: 阈值分数
        
        Returns:
            等级描述
        """
        if threshold <= 20:
            return '极严格'
        elif threshold <= 30:
            return '严格'
        elif threshold <= 40:
            return '适中'
        elif threshold <= 50:
            return '宽松'
        else:
            return '极宽松'


class ScoreLevel:
    """分数等级定义"""
    
    LEVELS: Dict[str, Dict] = {
        'original': {
            'range': (0, 10),
            'label': '完全原创',
            'color': 'green',
            'action': '通过'
        },
        'low': {
            'range': (11, 30),
            'label': '低重复度',
            'color': 'blue',
            'action': '通过'
        },
        'medium': {
            'range': (31, 50),
            'label': '中重复度',
            'color': 'yellow',
            'action': '关注'
        },
        'high': {
            'range': (51, 70),
            'label': '高重复度',
            'color': 'orange',
            'action': '需修改'
        },
        'critical': {
            'range': (71, 100),
            'label': '严重重复',
            'color': 'red',
            'action': '必须修改'
        }
    }
    
    @classmethod
    def get_level(cls, score: float) -> Dict:
        """
        根据分数获取等级信息
        
        Args:
            score: 重复度分数
        
        Returns:
            等级信息字典
        """
        for level_name, level_info in cls.LEVELS.items():
            min_score, max_score = level_info['range']
            if min_score <= score <= max_score:
                return {
                    'level': level_name,
                    **level_info
                }
        
        return {
            'level': 'unknown',
            'range': (0, 100),
            'label': '未知',
            'color': 'gray',
            'action': '检查'
        }
    
    @classmethod
    def is_acceptable(cls, score: float, threshold: int) -> bool:
        """
        判断分数是否可接受
        
        Args:
            score: 重复度分数
            threshold: 阈值
        
        Returns:
            是否可接受
        """
        return score <= threshold


if __name__ == '__main__':
    print("=== 阈值配置测试 ===")
    
    print("\n默认阈值配置:")
    for content_type, info in PlagiarismThreshold.get_all_thresholds().items():
        print(f"  {content_type}: {info['threshold']}分 - {info['description']}")
    
    print("\n动态阈值调整测试:")
    contexts = [
        {'content_length': 300, 'retry_count': 0},
        {'content_length': 2000, 'retry_count': 2},
        {'content_type': 'dialogue', 'importance': 'high'}
    ]
    
    for i, ctx in enumerate(contexts, 1):
        base = 30
        adjusted = PlagiarismThreshold.adjust_threshold(base, ctx)
        print(f"  场景{i}: 基础阈值{base} -> 调整后{adjusted} (上下文: {ctx})")
    
    print("\n分数等级测试:")
    test_scores = [5, 25, 45, 65, 85]
    for score in test_scores:
        level = ScoreLevel.get_level(score)
        print(f"  分数{score}: {level['label']} ({level['action']})")

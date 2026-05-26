"""
查重校验系统 - 主入口

提供统一的查重校验接口，集成所有功能模块。
"""

from typing import Dict, List, Optional, Any, Callable
from pathlib import Path

from .similarity import (
    generate_plagiarism_score,
    calculate_similarity,
    cosine_similarity,
    jaccard_similarity,
    levenshtein_similarity,
    ngram_similarity
)
from .threshold import PlagiarismThreshold, ScoreLevel
from .retry import RetryMechanism
from .logger import PlagiarismLog


class PlagiarismChecker:
    """查重校验器"""
    
    def __init__(self,
                 max_attempts: int = 3,
                 log_dir: Optional[str] = None,
                 custom_thresholds: Optional[Dict[str, int]] = None):
        """
        初始化查重校验器
        
        Args:
            max_attempts: 最大重试次数
            log_dir: 日志目录
            custom_thresholds: 自定义阈值配置
        """
        self.max_attempts = max_attempts
        self.log = PlagiarismLog(log_dir=log_dir)
        self.retry_mechanism = RetryMechanism(max_attempts=max_attempts)
        
        if custom_thresholds:
            for content_type, threshold in custom_thresholds.items():
                PlagiarismThreshold.set_threshold(content_type, threshold)
    
    def check(self,
             content: str,
             comparison_library: Dict[str, str],
             content_type: str = 'content') -> Dict:
        """
        执行查重校验
        
        Args:
            content: 待检测内容
            comparison_library: 对比库
            content_type: 内容类型
        
        Returns:
            查重结果
        """
        result = generate_plagiarism_score(content, comparison_library)
        
        threshold = PlagiarismThreshold.get_threshold(content_type)
        result['threshold'] = threshold
        result['content_type'] = content_type
        result['passed'] = result['score'] <= threshold
        
        level_info = ScoreLevel.get_level(result['score'])
        result['level'] = level_info['level']
        result['level_label'] = level_info['label']
        result['action'] = level_info['action']
        
        return result
    
    def check_with_retry(self,
                        skill_execute: Callable,
                        input_data: Dict,
                        content_type: str,
                        comparison_library: Dict[str, str],
                        on_retry: Optional[Callable] = None) -> Dict:
        """
        带重试的查重校验
        
        Args:
            skill_execute: 技能执行函数
            input_data: 输入数据
            content_type: 内容类型
            comparison_library: 对比库
            on_retry: 重试回调
        
        Returns:
            最终结果
        """
        def wrapped_execute(data):
            output = skill_execute(data)
            content = self._extract_content(output)
            
            check_result = self.check(content, comparison_library, content_type)
            
            self.log.log_check(
                skill_name=skill_execute.__name__ if hasattr(skill_execute, '__name__') else 'skill',
                content_type=content_type,
                content=content,
                result=check_result
            )
            
            return output
        
        result = self.retry_mechanism.execute_with_retry(
            skill_execute=wrapped_execute,
            input_data=input_data,
            content_type=content_type,
            comparison_library=comparison_library,
            on_retry=on_retry
        )
        
        if result['status'] == 'success':
            self.log.log_success(
                skill_name=skill_execute.__name__ if hasattr(skill_execute, '__name__') else 'skill',
                content_type=content_type,
                final_score=result['plagiarism_score'],
                attempts=result['attempts']
            )
        else:
            self.log.log_failure(
                skill_name=skill_execute.__name__ if hasattr(skill_execute, '__name__') else 'skill',
                content_type=content_type,
                final_score=result['plagiarism_score'],
                attempts=result['attempts'],
                reason='max_attempts_reached'
            )
        
        result['log_summary'] = self.log.get_summary()
        
        return result
    
    def _extract_content(self, output: Any) -> str:
        """从输出中提取内容"""
        if output is None:
            return ''
        
        if isinstance(output, str):
            return output
        
        if isinstance(output, dict):
            for key in ['content', 'text', 'output', 'result']:
                if key in output:
                    value = output[key]
                    if isinstance(value, str):
                        return value
            return str(output)
        
        return str(output)
    
    def get_threshold(self, content_type: str) -> int:
        """获取阈值"""
        return PlagiarismThreshold.get_threshold(content_type)
    
    def set_threshold(self, content_type: str, threshold: int) -> None:
        """设置阈值"""
        PlagiarismThreshold.set_threshold(content_type, threshold)
    
    def get_all_thresholds(self) -> Dict[str, Dict]:
        """获取所有阈值配置"""
        return PlagiarismThreshold.get_all_thresholds()
    
    def get_log_summary(self) -> Dict:
        """获取日志摘要"""
        return self.log.get_summary()
    
    def export_logs(self, filepath: Optional[str] = None) -> str:
        """导出日志"""
        return self.log.export_logs(filepath)
    
    def clear_logs(self) -> None:
        """清空日志"""
        self.log.clear()


class SkillChainExecutor:
    """Skill链执行器（带查重校验）"""
    
    def __init__(self,
                 plagiarism_checker: Optional[PlagiarismChecker] = None,
                 max_attempts: int = 3):
        """
        初始化执行器
        
        Args:
            plagiarism_checker: 查重校验器
            max_attempts: 最大重试次数
        """
        self.checker = plagiarism_checker or PlagiarismChecker(max_attempts=max_attempts)
    
    def execute_skill(self,
                     skill: Any,
                     input_data: Dict,
                     content_type: str,
                     comparison_library: Dict[str, str]) -> Dict:
        """
        执行单个技能
        
        Args:
            skill: 技能实例
            input_data: 输入数据
            content_type: 内容类型
            comparison_library: 对比库
        
        Returns:
            执行结果
        """
        skill_name = skill.__class__.__name__ if hasattr(skill, '__class__') else str(skill)
        
        def skill_execute(data):
            if hasattr(skill, 'execute'):
                return skill.execute(data)
            elif callable(skill):
                return skill(data)
            else:
                raise ValueError(f"Skill {skill_name} 不可执行")
        
        return self.checker.check_with_retry(
            skill_execute=skill_execute,
            input_data=input_data,
            content_type=content_type,
            comparison_library=comparison_library
        )
    
    def execute_chain(self,
                     skills: List[Any],
                     input_data: Dict,
                     comparison_library: Dict[str, str],
                     content_types: Optional[List[str]] = None) -> Dict:
        """
        执行技能链
        
        Args:
            skills: 技能列表
            input_data: 输入数据
            comparison_library: 对比库
            content_types: 内容类型列表
        
        Returns:
            执行结果
        """
        results = []
        current_data = input_data
        
        default_types = ['idea', 'character', 'plot', 'content', 'content']
        
        for i, skill in enumerate(skills):
            content_type = (content_types[i] if content_types and i < len(content_types)
                          else default_types[i % len(default_types)])
            
            result = self.execute_skill(
                skill=skill,
                input_data=current_data,
                content_type=content_type,
                comparison_library=comparison_library
            )
            
            results.append(result)
            
            if result['status'] not in ['success', 'max_attempts_reached']:
                return {
                    'status': 'failed',
                    'failed_at': i,
                    'results': results
                }
            
            current_data = result.get('output', current_data)
        
        return {
            'status': 'success',
            'results': results,
            'log_summary': self.checker.get_log_summary()
        }


def create_checker(max_attempts: int = 3,
                   log_dir: Optional[str] = None,
                   custom_thresholds: Optional[Dict[str, int]] = None) -> PlagiarismChecker:
    """
    创建查重校验器
    
    Args:
        max_attempts: 最大重试次数
        log_dir: 日志目录
        custom_thresholds: 自定义阈值
    
    Returns:
        PlagiarismChecker实例
    """
    return PlagiarismChecker(
        max_attempts=max_attempts,
        log_dir=log_dir,
        custom_thresholds=custom_thresholds
    )


def create_executor(max_attempts: int = 3) -> SkillChainExecutor:
    """
    创建Skill链执行器
    
    Args:
        max_attempts: 最大重试次数
    
    Returns:
        SkillChainExecutor实例
    """
    return SkillChainExecutor(max_attempts=max_attempts)


__all__ = [
    'PlagiarismChecker',
    'SkillChainExecutor',
    'PlagiarismThreshold',
    'ScoreLevel',
    'RetryMechanism',
    'PlagiarismLog',
    'create_checker',
    'create_executor',
    'generate_plagiarism_score',
    'calculate_similarity',
    'cosine_similarity',
    'jaccard_similarity',
    'levenshtein_similarity',
    'ngram_similarity'
]


if __name__ == '__main__':
    print("=== 查重校验系统测试 ===")
    
    checker = create_checker(max_attempts=3)
    
    print("\n阈值配置:")
    for content_type, info in checker.get_all_thresholds().items():
        print(f"  {content_type}: {info['threshold']}分")
    
    content = "李大嘴是一个逻辑混乱的侦探，但他的错误推理总能歪打正着找到真相。"
    library = {
        'chapter1': "李大嘴是个推理混乱的侦探，但他的歪理总能意外找到真相。",
        'chapter2': "这是一个完全不同的故事内容。"
    }
    
    print("\n查重测试:")
    result = checker.check(content, library, 'content')
    print(f"  分数: {result['score']}")
    print(f"  等级: {result['level_label']}")
    print(f"  通过: {result['passed']}")
    print(f"  建议: {result['action']}")
    
    print("\n日志摘要:")
    summary = checker.get_log_summary()
    print(f"  总检查次数: {summary['total_checks']}")

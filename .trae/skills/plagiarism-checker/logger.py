"""
查重校验系统 - 日志系统

记录查重校验过程和结果，支持导出和分析。
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path
import json

from .similarity import get_timestamp, generate_session_id, hash_content


class PlagiarismLog:
    """查重校验日志"""
    
    def __init__(self, log_dir: Optional[str] = None):
        """
        初始化日志系统
        
        Args:
            log_dir: 日志目录路径
        """
        self.logs: List[Dict] = []
        self.session_id = generate_session_id()
        self.log_dir = Path(log_dir) if log_dir else None
    
    def log_check(self,
                 skill_name: str,
                 content_type: str,
                 content: str,
                 result: Dict) -> Dict:
        """
        记录查重校验
        
        Args:
            skill_name: 技能名称
            content_type: 内容类型
            content: 内容
            result: 查重结果
        
        Returns:
            日志条目
        """
        threshold = result.get('threshold', 30)
        score = result.get('score', 0)
        
        log_entry = {
            'timestamp': get_timestamp(),
            'session_id': self.session_id,
            'type': 'check',
            'skill_name': skill_name,
            'content_type': content_type,
            'content_length': len(content),
            'content_hash': hash_content(content),
            'score': score,
            'threshold': threshold,
            'passed': score <= threshold,
            'max_similarity': result.get('max_similarity', 0),
            'similar_sources': result.get('similar_sources', []),
            'algorithm_scores': result.get('algorithm_scores', {})
        }
        
        self.logs.append(log_entry)
        return log_entry
    
    def log_retry(self,
                 skill_name: str,
                 attempt: int,
                 previous_result: Dict,
                 retry_instruction: Dict) -> Dict:
        """
        记录重试
        
        Args:
            skill_name: 技能名称
            attempt: 尝试次数
            previous_result: 上次结果
            retry_instruction: 重试指令
        
        Returns:
            日志条目
        """
        log_entry = {
            'timestamp': get_timestamp(),
            'session_id': self.session_id,
            'type': 'retry',
            'skill_name': skill_name,
            'attempt': attempt,
            'previous_score': previous_result.get('score', 0),
            'threshold': previous_result.get('threshold', 30),
            'issues': retry_instruction.get('issues', []),
            'suggestions': retry_instruction.get('suggestions', []),
            'retry_params': retry_instruction.get('retry_params', {})
        }
        
        self.logs.append(log_entry)
        return log_entry
    
    def log_success(self,
                   skill_name: str,
                   content_type: str,
                   final_score: float,
                   attempts: int) -> Dict:
        """
        记录成功
        
        Args:
            skill_name: 技能名称
            content_type: 内容类型
            final_score: 最终分数
            attempts: 尝试次数
        
        Returns:
            日志条目
        """
        log_entry = {
            'timestamp': get_timestamp(),
            'session_id': self.session_id,
            'type': 'success',
            'skill_name': skill_name,
            'content_type': content_type,
            'final_score': final_score,
            'attempts': attempts
        }
        
        self.logs.append(log_entry)
        return log_entry
    
    def log_failure(self,
                   skill_name: str,
                   content_type: str,
                   final_score: float,
                   attempts: int,
                   reason: str) -> Dict:
        """
        记录失败
        
        Args:
            skill_name: 技能名称
            content_type: 内容类型
            final_score: 最终分数
            attempts: 尝试次数
            reason: 失败原因
        
        Returns:
            日志条目
        """
        log_entry = {
            'timestamp': get_timestamp(),
            'session_id': self.session_id,
            'type': 'failure',
            'skill_name': skill_name,
            'content_type': content_type,
            'final_score': final_score,
            'attempts': attempts,
            'reason': reason,
            'needs_manual_review': True
        }
        
        self.logs.append(log_entry)
        return log_entry
    
    def get_summary(self) -> Dict:
        """
        获取日志摘要
        
        Returns:
            摘要信息
        """
        checks = [l for l in self.logs if l.get('type') == 'check']
        retries = [l for l in self.logs if l.get('type') == 'retry']
        successes = [l for l in self.logs if l.get('type') == 'success']
        failures = [l for l in self.logs if l.get('type') == 'failure']
        
        passed_checks = [l for l in checks if l.get('passed', False)]
        
        scores = [l['score'] for l in checks if 'score' in l]
        
        return {
            'session_id': self.session_id,
            'total_logs': len(self.logs),
            'total_checks': len(checks),
            'passed_checks': len(passed_checks),
            'failed_checks': len(checks) - len(passed_checks),
            'total_retries': len(retries),
            'total_successes': len(successes),
            'total_failures': len(failures),
            'pass_rate': len(passed_checks) / len(checks) if checks else 0,
            'average_score': sum(scores) / len(scores) if scores else 0,
            'min_score': min(scores) if scores else 0,
            'max_score': max(scores) if scores else 0
        }
    
    def get_skill_stats(self, skill_name: str) -> Dict:
        """
        获取特定技能的统计信息
        
        Args:
            skill_name: 技能名称
        
        Returns:
            统计信息
        """
        skill_logs = [l for l in self.logs if l.get('skill_name') == skill_name]
        
        checks = [l for l in skill_logs if l.get('type') == 'check']
        retries = [l for l in skill_logs if l.get('type') == 'retry']
        
        scores = [l['score'] for l in checks if 'score' in l]
        
        return {
            'skill_name': skill_name,
            'total_checks': len(checks),
            'total_retries': len(retries),
            'average_score': sum(scores) / len(scores) if scores else 0,
            'best_score': min(scores) if scores else 0,
            'worst_score': max(scores) if scores else 0
        }
    
    def export_logs(self, filepath: Optional[str] = None) -> str:
        """
        导出日志
        
        Args:
            filepath: 导出文件路径
        
        Returns:
            导出文件路径
        """
        if filepath is None:
            if self.log_dir:
                self.log_dir.mkdir(parents=True, exist_ok=True)
                filepath = self.log_dir / f"plagiarism_log_{self.session_id}.json"
            else:
                filepath = f"plagiarism_log_{self.session_id}.json"
        
        export_data = {
            'session_id': self.session_id,
            'export_time': get_timestamp(),
            'summary': self.get_summary(),
            'logs': self.logs
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        return str(filepath)
    
    def import_logs(self, filepath: str) -> None:
        """
        导入日志
        
        Args:
            filepath: 日志文件路径
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.session_id = data.get('session_id', self.session_id)
        self.logs = data.get('logs', [])
    
    def clear(self) -> None:
        """清空日志"""
        self.logs = []
        self.session_id = generate_session_id()
    
    def get_recent_logs(self, count: int = 10) -> List[Dict]:
        """
        获取最近的日志
        
        Args:
            count: 数量
        
        Returns:
            日志列表
        """
        return self.logs[-count:] if self.logs else []
    
    def filter_by_type(self, log_type: str) -> List[Dict]:
        """
        按类型筛选日志
        
        Args:
            log_type: 日志类型
        
        Returns:
            日志列表
        """
        return [l for l in self.logs if l.get('type') == log_type]
    
    def filter_by_skill(self, skill_name: str) -> List[Dict]:
        """
        按技能筛选日志
        
        Args:
            skill_name: 技能名称
        
        Returns:
            日志列表
        """
        return [l for l in self.logs if l.get('skill_name') == skill_name]
    
    def filter_by_score_range(self, min_score: float, max_score: float) -> List[Dict]:
        """
        按分数范围筛选日志
        
        Args:
            min_score: 最小分数
            max_score: 最大分数
        
        Returns:
            日志列表
        """
        return [
            l for l in self.logs
            if 'score' in l and min_score <= l['score'] <= max_score
        ]


def create_log_system(log_dir: Optional[str] = None) -> PlagiarismLog:
    """
    创建日志系统实例
    
    Args:
        log_dir: 日志目录路径
    
    Returns:
        PlagiarismLog实例
    """
    return PlagiarismLog(log_dir=log_dir)


if __name__ == '__main__':
    print("=== 日志系统测试 ===")
    
    log = PlagiarismLog()
    
    print(f"\n会话ID: {log.session_id}")
    
    log.log_check(
        skill_name='content-writer',
        content_type='content',
        content='这是一段测试内容',
        result={
            'score': 35.6,
            'threshold': 30,
            'max_similarity': 0.356,
            'similar_sources': [{'source_id': 'test', 'similarity': 0.356}],
            'algorithm_scores': {'cosine': 0.342}
        }
    )
    
    log.log_retry(
        skill_name='content-writer',
        attempt=1,
        previous_result={'score': 35.6, 'threshold': 30},
        retry_instruction={
            'issues': ['与来源test相似度35.6%'],
            'suggestions': ['需要调整内容'],
            'retry_params': {'creativity_boost': 0.1}
        }
    )
    
    log.log_success(
        skill_name='content-writer',
        content_type='content',
        final_score=22.3,
        attempts=2
    )
    
    print("\n日志摘要:")
    summary = log.get_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    print("\n最近日志:")
    for entry in log.get_recent_logs(3):
        print(f"  [{entry['type']}] {entry['skill_name']}: {entry.get('score', 'N/A')}")

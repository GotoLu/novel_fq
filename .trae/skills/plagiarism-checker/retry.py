"""
查重校验系统 - 回炉重造机制

当内容重复度超标时，自动触发重新生成流程。
"""

from typing import Dict, List, Optional, Any, Callable
from .similarity import generate_plagiarism_score, get_timestamp
from .threshold import PlagiarismThreshold, ScoreLevel


class RetryMechanism:
    """回炉重造机制"""
    
    def __init__(self, max_attempts: int = 3):
        """
        初始化重造机制
        
        Args:
            max_attempts: 最大重试次数
        """
        self.max_attempts = max_attempts
        self.attempt_history: List[Dict] = []
    
    def execute_with_retry(self,
                          skill_execute: Callable,
                          input_data: Dict,
                          content_type: str,
                          comparison_library: Dict[str, str],
                          on_retry: Optional[Callable] = None) -> Dict:
        """
        带重试的执行
        
        Args:
            skill_execute: 技能执行函数
            input_data: 输入数据
            content_type: 内容类型
            comparison_library: 对比库
            on_retry: 重试回调函数
        
        Returns:
            最终结果
        """
        attempt = 0
        best_result = None
        best_score = 100.0
        best_output = None
        
        base_threshold = PlagiarismThreshold.get_threshold(content_type)
        
        while attempt < self.max_attempts:
            attempt += 1
            
            context = {
                'content_type': content_type,
                'retry_count': attempt - 1,
                'content_length': len(input_data.get('content', ''))
            }
            threshold = PlagiarismThreshold.adjust_threshold(base_threshold, context)
            
            if attempt == 1:
                output = skill_execute(input_data)
            else:
                retry_input = self._prepare_retry_input(
                    input_data,
                    best_output,
                    attempt
                )
                output = skill_execute(retry_input)
            
            content = self._extract_content(output)
            
            plagiarism_result = generate_plagiarism_score(
                content,
                comparison_library
            )
            plagiarism_result['threshold'] = threshold
            plagiarism_result['attempt'] = attempt
            plagiarism_result['adjusted_threshold'] = threshold
            
            self.attempt_history.append({
                'attempt': attempt,
                'output': output,
                'content': content[:200] + '...' if len(content) > 200 else content,
                'plagiarism_result': plagiarism_result,
                'timestamp': get_timestamp()
            })
            
            if plagiarism_result['score'] <= threshold:
                return {
                    'status': 'success',
                    'output': output,
                    'content': content,
                    'plagiarism_score': plagiarism_result['score'],
                    'attempts': attempt,
                    'threshold': threshold,
                    'passed': True
                }
            
            if plagiarism_result['score'] < best_score:
                best_score = plagiarism_result['score']
                best_result = plagiarism_result
                best_output = output
            
            retry_instruction = self._generate_retry_instruction(
                output,
                plagiarism_result,
                attempt
            )
            
            if on_retry:
                on_retry(attempt, plagiarism_result, retry_instruction)
        
        return {
            'status': 'max_attempts_reached',
            'output': best_output,
            'content': self._extract_content(best_output) if best_output else '',
            'plagiarism_score': best_score,
            'attempts': self.max_attempts,
            'threshold': base_threshold,
            'needs_manual_review': True,
            'passed': False,
            'attempt_history': self.attempt_history
        }
    
    def _prepare_retry_input(self, 
                            original_input: Dict,
                            previous_output: Any,
                            attempt: int) -> Dict:
        """
        准备重试输入
        
        Args:
            original_input: 原始输入
            previous_output: 上次输出
            attempt: 当前尝试次数
        
        Returns:
            重试输入
        """
        retry_input = original_input.copy()
        
        retry_input['retry'] = {
            'attempt': attempt,
            'previous_output': previous_output,
            'creativity_boost': attempt * 0.1,
            'avoid_patterns': self._extract_patterns(previous_output)
        }
        
        retry_input['creativity_level'] = min(1.0, 0.5 + attempt * 0.15)
        
        return retry_input
    
    def _extract_content(self, output: Any) -> str:
        """
        从输出中提取内容
        
        Args:
            output: 输出对象
        
        Returns:
            内容字符串
        """
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
                    elif isinstance(value, dict):
                        return self._extract_content(value)
            return str(output)
        
        return str(output)
    
    def _extract_patterns(self, output: Any) -> List[str]:
        """
        提取需要避免的模式
        
        Args:
            output: 输出对象
        
        Returns:
            模式列表
        """
        patterns = []
        content = self._extract_content(output)
        
        if not content:
            return patterns
        
        words = content.split()
        phrase_counts = {}
        
        for i in range(len(words) - 2):
            phrase = ' '.join(words[i:i+3])
            phrase_counts[phrase] = phrase_counts.get(phrase, 0) + 1
        
        patterns = [phrase for phrase, count in phrase_counts.items() if count > 1]
        
        return patterns[:10]
    
    def _generate_retry_instruction(self,
                                   output: Any,
                                   plagiarism_result: Dict,
                                   attempt: int) -> Dict:
        """
        生成重造指令
        
        Args:
            output: 当前输出
            plagiarism_result: 查重结果
            attempt: 当前尝试次数
        
        Returns:
            重造指令
        """
        instruction = {
            'action': 'retry',
            'attempt': attempt,
            'issues': [],
            'suggestions': [],
            'retry_params': {}
        }
        
        for source in plagiarism_result.get('similar_sources', []):
            instruction['issues'].append(
                f"与来源 {source['source_id']} 相似度 {source['similarity']*100:.1f}%"
            )
        
        score = plagiarism_result['score']
        if score > 60:
            instruction['suggestions'].append("需要大幅修改内容结构和表达方式")
            instruction['suggestions'].append("尝试从不同角度重新构思")
        elif score > 40:
            instruction['suggestions'].append("需要调整部分内容和表达")
            instruction['suggestions'].append("增加原创性描述")
        else:
            instruction['suggestions'].append("需要微调个别表述")
            instruction['suggestions'].append("替换相似词汇")
        
        instruction['retry_params'] = {
            'avoid_sources': [s['source_id'] for s in plagiarism_result.get('similar_sources', [])],
            'target_score': plagiarism_result['threshold'] - 5,
            'creativity_boost': attempt * 0.1
        }
        
        return instruction
    
    def get_attempt_summary(self) -> Dict:
        """
        获取尝试摘要
        
        Returns:
            摘要信息
        """
        if not self.attempt_history:
            return {
                'total_attempts': 0,
                'best_score': None,
                'final_status': 'no_attempts'
            }
        
        scores = [h['plagiarism_result']['score'] for h in self.attempt_history]
        
        return {
            'total_attempts': len(self.attempt_history),
            'best_score': min(scores),
            'worst_score': max(scores),
            'average_score': sum(scores) / len(scores),
            'score_trend': scores,
            'final_status': 'improved' if scores[-1] < scores[0] else 'not_improved'
        }


def create_retry_mechanism(max_attempts: int = 3) -> RetryMechanism:
    """
    创建重造机制实例
    
    Args:
        max_attempts: 最大重试次数
    
    Returns:
        RetryMechanism实例
    """
    return RetryMechanism(max_attempts=max_attempts)


if __name__ == '__main__':
    print("=== 回炉重造机制测试 ===")
    
    def mock_skill_execute(input_data):
        content = input_data.get('content', '')
        retry = input_data.get('retry', {})
        
        if retry:
            attempt = retry.get('attempt', 1)
            return {'content': f"第{attempt}次重试生成的内容，完全原创的新文本。"}
        
        return {'content': content or "初始生成的内容"}
    
    comparison_library = {
        'source1': "初始生成的内容",
        'source2': "一些已有的文本内容"
    }
    
    mechanism = RetryMechanism(max_attempts=3)
    
    result = mechanism.execute_with_retry(
        skill_execute=mock_skill_execute,
        input_data={'content': "初始生成的内容"},
        content_type='content',
        comparison_library=comparison_library
    )
    
    print(f"\n执行状态: {result['status']}")
    print(f"重复度分数: {result['plagiarism_score']}")
    print(f"尝试次数: {result['attempts']}")
    print(f"是否通过: {result['passed']}")
    
    print("\n尝试摘要:")
    summary = mechanism.get_attempt_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")

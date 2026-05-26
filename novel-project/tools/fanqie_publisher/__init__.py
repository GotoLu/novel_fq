"""
番茄作家助手自动提交工具
"""

from .publisher import (
    FanqiePublisher,
    FanqiePublisherConfig,
    ChapterContent,
    SubmitResult,
    SubmitStatus,
    ErrorCode,
    parse_markdown_file,
    generate_report
)

__version__ = "1.0.0"
__all__ = [
    "FanqiePublisher",
    "FanqiePublisherConfig",
    "ChapterContent",
    "SubmitResult",
    "SubmitStatus",
    "ErrorCode",
    "parse_markdown_file",
    "generate_report"
]

"""
命令行接口
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import List

from .publisher import (
    FanqiePublisher,
    FanqiePublisherConfig,
    ChapterContent,
    SubmitResult,
    SubmitStatus,
    parse_markdown_file,
    generate_report
)


def print_banner():
    """打印横幅"""
    banner = """
╔═══════════════════════════════════════════════════════════╗
║         番茄作家助手自动提交工具 v1.0.0                   ║
║         Fanqie Novel Auto Publisher                       ║
╚═══════════════════════════════════════════════════════════╝
"""
    print(banner)


def create_parser() -> argparse.ArgumentParser:
    """创建命令行解析器"""
    parser = argparse.ArgumentParser(
        description="番茄作家助手自动提交工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 提交单个文件
  python cli.py submit -f "第001章_大嘴侦探登场.md"
  
  # 批量提交目录下所有md文件
  python cli.py batch -d "./正文"
  
  # 使用配置文件
  python cli.py submit -f chapter.md -c config.yaml
  
  # 启动浏览器调试模式（需要先执行此命令启动浏览器）
  python cli.py browser --start
"""
    )
    
    subparsers = parser.add_subparsers(dest="command", help="命令")
    
    submit_parser = subparsers.add_parser("submit", help="提交单个章节")
    submit_parser.add_argument("-f", "--file", required=True, help="章节文件路径")
    submit_parser.add_argument("-t", "--title", help="章节标题（默认从文件提取）")
    submit_parser.add_argument("-c", "--config", help="配置文件路径")
    submit_parser.add_argument("--cdp-port", type=int, default=9222, help="CDP端口")
    submit_parser.add_argument("--no-screenshot", action="store_true", help="失败时不截图")
    
    batch_parser = subparsers.add_parser("batch", help="批量提交章节")
    batch_parser.add_argument("-d", "--directory", required=True, help="章节目录")
    batch_parser.add_argument("-p", "--pattern", default="*.md", help="文件匹配模式")
    batch_parser.add_argument("-o", "--output", help="报告输出路径")
    batch_parser.add_argument("-c", "--config", help="配置文件路径")
    batch_parser.add_argument("--cdp-port", type=int, default=9222, help="CDP端口")
    batch_parser.add_argument("--sort", action="store_true", help="按章节号排序")
    batch_parser.add_argument("--dry-run", action="store_true", help="仅解析不提交")
    
    browser_parser = subparsers.add_parser("browser", help="浏览器管理")
    browser_parser.add_argument("--start", action="store_true", help="启动调试模式浏览器")
    browser_parser.add_argument("--port", type=int, default=9222, help="调试端口")
    
    return parser


def load_config(config_path: str) -> FanqiePublisherConfig:
    """加载配置文件"""
    if config_path and Path(config_path).exists():
        import yaml
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)
        return FanqiePublisherConfig(**config_data)
    return FanqiePublisherConfig()


def status_callback(status: SubmitStatus, message: str):
    """状态回调"""
    icons = {
        SubmitStatus.PENDING: "⏳",
        SubmitStatus.PREPARING: "🔧",
        SubmitStatus.SUBMITTING: "📤",
        SubmitStatus.SUCCESS: "✅",
        SubmitStatus.FAILED: "❌",
        SubmitStatus.RETRYING: "🔄"
    }
    icon = icons.get(status, "📌")
    print(f"{icon} {message}")


async def submit_single(args):
    """提交单个章节"""
    print_banner()
    
    config = load_config(args.config) if hasattr(args, 'config') else FanqiePublisherConfig()
    config.cdp_port = args.cdp_port
    if args.no_screenshot:
        config.screenshot_on_error = False
    
    chapter = parse_markdown_file(args.file)
    if not chapter:
        print(f"❌ 无法解析文件: {args.file}")
        return 1
    
    if args.title:
        chapter.title = args.title
    
    print(f"📖 章节信息:")
    print(f"   标题: {chapter.title}")
    print(f"   字数: {chapter.word_count}")
    print(f"   来源: {chapter.source_file}")
    print()
    
    publisher = FanqiePublisher(config)
    publisher.set_status_callback(status_callback)
    
    try:
        if not await publisher.connect_browser():
            print("\n❌ 连接浏览器失败")
            print("请确保已启动调试模式浏览器:")
            print(f"  chrome.exe --remote-debugging-port={config.cdp_port}")
            return 1
        
        if not await publisher.navigate_to_writer():
            print("\n❌ 导航到作家后台失败")
            return 1
        
        result = await publisher.submit_to_draft(chapter)
        
        print()
        if result.is_success:
            print(f"✅ 提交成功!")
            print(f"   时间: {result.submit_time}")
            return 0
        else:
            print(f"❌ 提交失败")
            print(f"   错误: {result.error_message}")
            if result.screenshot_path:
                print(f"   截图: {result.screenshot_path}")
            return 1
            
    finally:
        await publisher.close()


async def submit_batch(args):
    """批量提交章节"""
    print_banner()
    
    config = load_config(args.config) if hasattr(args, 'config') else FanqiePublisherConfig()
    config.cdp_port = args.cdp_port
    
    directory = Path(args.directory)
    if not directory.exists():
        print(f"❌ 目录不存在: {directory}")
        return 1
    
    files = list(directory.glob(args.pattern))
    if not files:
        print(f"❌ 未找到匹配文件: {args.pattern}")
        return 1
    
    chapters: List[ChapterContent] = []
    for file_path in files:
        chapter = parse_markdown_file(str(file_path))
        if chapter:
            chapters.append(chapter)
    
    if args.sort:
        chapters.sort(key=lambda c: c.chapter_number or 999)
    
    print(f"📚 发现 {len(chapters)} 个章节:")
    for i, chapter in enumerate(chapters, 1):
        print(f"   {i}. {chapter.title} ({chapter.word_count}字)")
    print()
    
    if args.dry_run:
        print("🔍 Dry-run 模式，不实际提交")
        return 0
    
    publisher = FanqiePublisher(config)
    publisher.set_status_callback(status_callback)
    
    try:
        if not await publisher.connect_browser():
            print("\n❌ 连接浏览器失败")
            return 1
        
        if not await publisher.navigate_to_writer():
            print("\n❌ 导航到作家后台失败")
            return 1
        
        results = await publisher.submit_batch(chapters)
        
        print()
        success_count = sum(1 for r in results if r.is_success)
        print(f"📊 提交结果:")
        print(f"   成功: {success_count}/{len(results)}")
        print(f"   失败: {len(results) - success_count}/{len(results)}")
        
        if args.output:
            report = generate_report(results, args.output)
            print(f"   报告: {args.output}")
        
        return 0 if success_count == len(results) else 1
        
    finally:
        await publisher.close()


def start_browser(args):
    """启动调试模式浏览器"""
    import subprocess
    import platform
    
    print_banner()
    print(f"🚀 启动调试模式浏览器 (端口: {args.port})")
    
    system = platform.system()
    
    if system == "Windows":
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
        ]
    elif system == "Darwin":
        chrome_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ]
    else:
        chrome_paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/chromium-browser",
        ]
    
    chrome_path = None
    for path in chrome_paths:
        if Path(path).exists():
            chrome_path = path
            break
    
    if not chrome_path:
        print("❌ 未找到Chrome浏览器，请手动启动:")
        print(f"   chrome.exe --remote-debugging-port={args.port}")
        return 1
    
    cmd = [
        chrome_path,
        f"--remote-debugging-port={args.port}",
        "--user-data-dir=./chrome_debug_profile",
    ]
    
    print(f"📍 浏览器路径: {chrome_path}")
    print(f"📍 调试端口: {args.port}")
    print()
    
    try:
        subprocess.Popen(cmd)
        print("✅ 浏览器已启动!")
        print()
        print("请在浏览器中登录番茄作家助手，然后运行提交命令。")
        print(f"登录地址: https://fanqienovel.com/writer")
        return 0
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        return 1


def main():
    """主入口"""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    if args.command == "submit":
        return asyncio.run(submit_single(args))
    elif args.command == "batch":
        return asyncio.run(submit_batch(args))
    elif args.command == "browser":
        return start_browser(args)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

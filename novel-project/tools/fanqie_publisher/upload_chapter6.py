"""
上传第006章到番茄作家助手
"""

import asyncio
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from publisher import (
    FanqiePublisher,
    FanqiePublisherConfig,
    ChapterContent,
    SubmitStatus,
    parse_markdown_file
)


async def upload_chapter6():
    """上传第006章"""
    print("\n" + "="*60)
    print("上传第006章到番茄作家助手")
    print("="*60)
    
    chapter_file = Path(__file__).parent.parent.parent / "正文" / "第006章_密室失窃.md"
    
    if not chapter_file.exists():
        print(f"❌ 文件不存在: {chapter_file}")
        return False
    
    print(f"\n📄 解析文件: {chapter_file.name}")
    chapter = parse_markdown_file(str(chapter_file))
    
    if not chapter:
        print("❌ 解析文件失败")
        return False
    
    print(f"✅ 解析成功!")
    print(f"  标题: {chapter.title}")
    print(f"  章节号: {chapter.chapter_number}")
    print(f"  字数: {chapter.word_count}")
    print(f"  内容预览: {chapter.content[:100]}...")
    
    config = FanqiePublisherConfig(
        cdp_port=9222,
        headless=False,
        timeout=30000,
        max_retries=3,
        screenshot_on_error=True,
        log_level="INFO"
    )
    
    publisher = FanqiePublisher(config)
    
    def on_status(status: SubmitStatus, message: str):
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"[{timestamp}] [{status.value}] {message}")
    
    publisher.set_status_callback(on_status)
    
    try:
        print("\n🔌 连接浏览器...")
        if not await publisher.connect_browser():
            print("❌ 浏览器连接失败")
            print("\n请先启动调试模式浏览器:")
            print("  chrome.exe --remote-debugging-port=9222")
            print("\n或者在浏览器中手动登录番茄作家助手后，再运行此脚本")
            return False
        
        print("\n🌐 导航到作家后台...")
        if not await publisher.navigate_to_writer():
            print("❌ 导航失败")
            print("  可能需要先在浏览器中登录番茄作家助手")
            return False
        
        print(f"\n📤 提交章节: {chapter.title}")
        result = await publisher.submit_to_draft(chapter)
        
        print("\n" + "="*60)
        print("提交结果")
        print("="*60)
        print(f"状态: {result.status.value}")
        print(f"错误码: {result.error_code.value}")
        
        if result.error_message:
            print(f"错误信息: {result.error_message}")
        
        if result.submit_time:
            print(f"提交时间: {result.submit_time}")
        
        if result.screenshot_path:
            print(f"错误截图: {result.screenshot_path}")
        
        if result.is_success:
            print("\n✅ 上传成功！")
            print("请在番茄作家助手平台查看草稿箱")
        else:
            print("\n❌ 上传失败")
        
        return result.is_success
        
    except Exception as e:
        print(f"\n❌ 上传过程出错: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        await publisher.close()


if __name__ == "__main__":
    success = asyncio.run(upload_chapter6())
    sys.exit(0 if success else 1)

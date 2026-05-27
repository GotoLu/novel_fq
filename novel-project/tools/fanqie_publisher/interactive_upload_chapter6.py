"""
交互式上传第006章到番茄作家助手
先打开浏览器让用户登录，登录完成后再上传
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


async def interactive_upload():
    """交互式上传"""
    print("\n" + "="*60)
    print("交互式上传第006章到番茄作家助手")
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
            return False
        
        print("\n🌐 导航到作家后台...")
        await publisher.page.goto(config.fanqie_url, wait_until="networkidle")
        
        current_url = publisher.page.url
        print(f"  当前URL: {current_url}")
        
        if "login" in current_url or "passport" in current_url:
            print("\n" + "="*60)
            print("⚠️  需要登录")
            print("="*60)
            print("\n请在浏览器中完成登录操作")
            print("登录完成后，请回到此终端按回车键继续...")
            
            input("\n按回车键继续...")
            
            await asyncio.sleep(2)
            
            current_url = publisher.page.url
            print(f"\n当前URL: {current_url}")
            
            if "login" in current_url or "passport" in current_url:
                print("❌ 仍未登录，请重新登录后重试")
                return False
        
        print("\n✅ 已登录，准备上传...")
        
        await asyncio.sleep(1)
        
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
            print("\n可能的原因：")
            print("1. 页面结构已变化，需要更新选择器")
            print("2. 没有找到'新建章节'按钮")
            print("3. 其他页面元素未找到")
            print("\n建议：手动上传章节内容")
        
        return result.is_success
        
    except Exception as e:
        print(f"\n❌ 上传过程出错: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        await publisher.close()


if __name__ == "__main__":
    success = asyncio.run(interactive_upload())
    sys.exit(0 if success else 1)

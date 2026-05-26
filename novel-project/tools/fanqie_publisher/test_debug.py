"""
调试测试脚本
用于测试番茄作家助手发布工具的各项功能
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from publisher import (
    FanqiePublisher,
    FanqiePublisherConfig,
    ChapterContent,
    SubmitStatus,
    parse_markdown_file
)


async def test_browser_connection():
    """测试浏览器连接"""
    print("\n" + "="*60)
    print("测试1: 浏览器连接")
    print("="*60)
    
    config = FanqiePublisherConfig(
        cdp_port=9222,
        headless=False,
        timeout=30000
    )
    
    publisher = FanqiePublisher(config)
    
    def on_status(status: SubmitStatus, message: str):
        print(f"  [{status.value}] {message}")
    
    publisher.set_status_callback(on_status)
    
    try:
        print("\n尝试连接浏览器...")
        success = await publisher.connect_browser()
        
        if success:
            print("✅ 浏览器连接成功!")
            
            print("\n尝试获取当前页面URL...")
            url = publisher.page.url
            print(f"  当前URL: {url}")
            
            print("\n尝试截图...")
            await publisher.page.screenshot(path="test_screenshot.png")
            print("  ✅ 截图保存: test_screenshot.png")
            
            return True
        else:
            print("❌ 浏览器连接失败")
            print("\n请先启动调试模式浏览器:")
            print("  chrome.exe --remote-debugging-port=9222")
            return False
            
    except Exception as e:
        print(f"❌ 测试出错: {e}")
        return False
    finally:
        await publisher.close()


async def test_navigate_to_writer():
    """测试导航到作家后台"""
    print("\n" + "="*60)
    print("测试2: 导航到作家后台")
    print("="*60)
    
    config = FanqiePublisherConfig(
        cdp_port=9222,
        headless=False,
        timeout=30000
    )
    
    publisher = FanqiePublisher(config)
    
    def on_status(status: SubmitStatus, message: str):
        print(f"  [{status.value}] {message}")
    
    publisher.set_status_callback(on_status)
    
    try:
        if not await publisher.connect_browser():
            print("❌ 浏览器连接失败")
            return False
        
        print("\n尝试导航到番茄作家后台...")
        success = await publisher.navigate_to_writer()
        
        if success:
            print("✅ 导航成功!")
            url = publisher.page.url
            print(f"  当前URL: {url}")
            
            await asyncio.sleep(2)
            await publisher.page.screenshot(path="test_writer_page.png")
            print("  ✅ 截图保存: test_writer_page.png")
            
            return True
        else:
            print("❌ 导航失败")
            print("  可能需要先登录番茄作家助手")
            return False
            
    except Exception as e:
        print(f"❌ 测试出错: {e}")
        return False
    finally:
        await publisher.close()


async def test_parse_markdown():
    """测试Markdown解析"""
    print("\n" + "="*60)
    print("测试3: Markdown文件解析")
    print("="*60)
    
    test_file = Path(__file__).parent.parent.parent / "正文" / "第001章_大嘴侦探登场.md"
    
    if not test_file.exists():
        print(f"❌ 测试文件不存在: {test_file}")
        return False
    
    print(f"\n解析文件: {test_file}")
    chapter = parse_markdown_file(str(test_file))
    
    if chapter:
        print("✅ 解析成功!")
        print(f"  标题: {chapter.title}")
        print(f"  章节号: {chapter.chapter_number}")
        print(f"  字数: {chapter.word_count}")
        print(f"  内容预览: {chapter.content[:100]}...")
        return True
    else:
        print("❌ 解析失败")
        return False


async def test_submit_draft():
    """测试提交草稿"""
    print("\n" + "="*60)
    print("测试4: 提交草稿")
    print("="*60)
    
    test_file = Path(__file__).parent.parent.parent / "正文" / "第001章_大嘴侦探登场.md"
    
    if not test_file.exists():
        print(f"❌ 测试文件不存在: {test_file}")
        return False
    
    chapter = parse_markdown_file(str(test_file))
    if not chapter:
        print("❌ 解析文件失败")
        return False
    
    chapter.title = "[测试] " + chapter.title
    
    config = FanqiePublisherConfig(
        cdp_port=9222,
        headless=False,
        timeout=30000,
        max_retries=2,
        screenshot_on_error=True
    )
    
    publisher = FanqiePublisher(config)
    
    def on_status(status: SubmitStatus, message: str):
        print(f"  [{status.value}] {message}")
    
    publisher.set_status_callback(on_status)
    
    try:
        print("\n连接浏览器...")
        if not await publisher.connect_browser():
            print("❌ 浏览器连接失败")
            return False
        
        print("\n导航到作家后台...")
        if not await publisher.navigate_to_writer():
            print("❌ 导航失败")
            return False
        
        print(f"\n提交章节: {chapter.title}")
        result = await publisher.submit_to_draft(chapter)
        
        print("\n提交结果:")
        print(f"  状态: {result.status.value}")
        print(f"  错误码: {result.error_code.value}")
        if result.error_message:
            print(f"  错误信息: {result.error_message}")
        if result.submit_time:
            print(f"  提交时间: {result.submit_time}")
        if result.screenshot_path:
            print(f"  截图: {result.screenshot_path}")
        
        return result.is_success
        
    except Exception as e:
        print(f"❌ 测试出错: {e}")
        return False
    finally:
        await publisher.close()


async def run_all_tests():
    """运行所有测试"""
    print("\n" + "="*60)
    print("番茄作家助手发布工具 - 调试测试")
    print("="*60)
    
    tests = [
        ("浏览器连接", test_browser_connection),
        ("Markdown解析", test_parse_markdown),
        ("导航到作家后台", test_navigate_to_writer),
        ("提交草稿", test_submit_draft),
    ]
    
    results = {}
    
    for name, test_func in tests:
        try:
            result = await test_func()
            results[name] = result
        except Exception as e:
            print(f"\n❌ 测试 '{name}' 异常: {e}")
            results[name] = False
        
        choice = input("\n继续下一个测试? (y/n): ")
        if choice.lower() != 'y':
            break
    
    print("\n" + "="*60)
    print("测试结果汇总")
    print("="*60)
    for name, result in results.items():
        status = "✅ 通过" if result else "❌ 失败"
        print(f"  {name}: {status}")


async def interactive_test():
    """交互式测试"""
    print("\n" + "="*60)
    print("交互式测试模式")
    print("="*60)
    print("\n可用测试:")
    print("  1. 测试浏览器连接")
    print("  2. 测试Markdown解析")
    print("  3. 测试导航到作家后台")
    print("  4. 测试提交草稿")
    print("  5. 运行所有测试")
    print("  0. 退出")
    
    while True:
        choice = input("\n请选择测试 (0-5): ")
        
        if choice == '0':
            break
        elif choice == '1':
            await test_browser_connection()
        elif choice == '2':
            await test_parse_markdown()
        elif choice == '3':
            await test_navigate_to_writer()
        elif choice == '4':
            await test_submit_draft()
        elif choice == '5':
            await run_all_tests()
            break
        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="调试测试脚本")
    parser.add_argument("--all", action="store_true", help="运行所有测试")
    args = parser.parse_args()
    
    if args.all:
        asyncio.run(run_all_tests())
    else:
        asyncio.run(interactive_test())

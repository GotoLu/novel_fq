"""
自动运行测试 - 无需用户交互
"""

import asyncio
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
if os.path.exists(lib_path):
    sys.path.insert(0, lib_path)

print("="*60)
print("自动运行测试")
print("="*60)


async def test_browser():
    """测试浏览器启动和访问"""
    print("\n[测试] 启动浏览器并访问番茄作家助手")
    
    try:
        from playwright.async_api import async_playwright
        
        print("  1. 启动Playwright...")
        playwright = await async_playwright().start()
        print("     [OK] Playwright已启动")
        
        print("  2. 启动Chromium浏览器...")
        browser = await playwright.chromium.launch(
            headless=False,
            slow_mo=100
        )
        print("     [OK] 浏览器已启动")
        
        print("  3. 创建新页面...")
        page = await browser.new_page()
        print("     [OK] 页面已创建")
        
        print("  4. 访问番茄作家助手...")
        await page.goto("https://fanqienovel.com/writer", 
                       wait_until="networkidle", 
                       timeout=30000)
        url = page.url
        print(f"     [OK] 页面已加载")
        print(f"     当前URL: {url}")
        
        if "login" in url or "passport" in url:
            print("     [提示] 需要登录")
            print("     请在浏览器中登录，然后继续...")
        else:
            print("     [OK] 已登录或可直接访问")
        
        print("  5. 截图...")
        await page.screenshot(path="browser_test.png")
        print("     [OK] 截图已保存: browser_test.png")
        
        print("\n  浏览器将保持打开10秒，请查看...")
        await asyncio.sleep(10)
        
        print("\n  6. 关闭浏览器...")
        await browser.close()
        print("     [OK] 浏览器已关闭")
        
        return True
        
    except Exception as e:
        print(f"     [ERROR] 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_submit_flow():
    """测试提交流程（不实际提交）"""
    print("\n[测试] 模拟提交流程")
    
    try:
        from publisher import (
            FanqiePublisher, 
            FanqiePublisherConfig,
            parse_markdown_file
        )
        
        print("  1. 创建配置...")
        config = FanqiePublisherConfig(
            headless=False,
            timeout=30000
        )
        print("     [OK] 配置已创建")
        
        print("  2. 创建发布器...")
        publisher = FanqiePublisher(config)
        print("     [OK] 发布器已创建")
        
        print("  3. 连接浏览器...")
        if not await publisher.connect_browser():
            print("     [ERROR] 连接失败")
            return False
        print("     [OK] 浏览器已连接")
        
        print("  4. 导航到作家后台...")
        if not await publisher.navigate_to_writer():
            print("     [ERROR] 导航失败")
            await publisher.close()
            return False
        print("     [OK] 已到达作家后台")
        
        print("  5. 解析章节文件...")
        chapter_file = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "正文", "第001章_大嘴侦探登场.md"
        )
        chapter_file = os.path.abspath(chapter_file)
        
        chapter = parse_markdown_file(chapter_file)
        if not chapter:
            print("     [ERROR] 解析失败")
            await publisher.close()
            return False
        
        print(f"     [OK] 解析成功")
        print(f"       标题: {chapter.title}")
        print(f"       字数: {chapter.word_count}")
        
        print("  6. 截图当前页面...")
        await publisher.page.screenshot(path="submit_flow_test.png")
        print("     [OK] 截图已保存: submit_flow_test.png")
        
        print("\n  [提示] 实际提交已跳过（测试模式）")
        print("  浏览器将保持打开5秒...")
        await asyncio.sleep(5)
        
        print("\n  7. 关闭连接...")
        await publisher.close()
        print("     [OK] 已关闭")
        
        return True
        
    except Exception as e:
        print(f"     [ERROR] 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    print("\n选择测试:")
    print("  1. 测试浏览器启动")
    print("  2. 测试完整提交流程（不实际提交）")
    print("  3. 两者都测试")
    
    # 自动选择测试3
    choice = "3"
    print(f"\n自动选择: {choice}")
    
    results = []
    
    if choice in ["1", "3"]:
        result1 = await test_browser()
        results.append(("浏览器启动", result1))
    
    if choice in ["2", "3"]:
        result2 = await test_submit_flow()
        results.append(("提交流程", result2))
    
    print("\n" + "="*60)
    print("测试结果汇总")
    print("="*60)
    for name, result in results:
        status = "[OK] 通过" if result else "[FAIL] 失败"
        print(f"  {name}: {status}")
    
    success_count = sum(1 for _, r in results if r)
    print(f"\n总计: {success_count}/{len(results)} 通过")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n用户中断")
    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()

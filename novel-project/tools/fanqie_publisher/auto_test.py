"""
自动化测试脚本 - 无需用户交互
"""

import asyncio
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
if os.path.exists(lib_path):
    sys.path.insert(0, lib_path)

print("="*60)
print("番茄作家助手发布工具 - 自动化测试")
print("="*60)

async def test_basic():
    """基本测试"""
    print("\n[测试1] Playwright导入测试")
    try:
        from playwright.async_api import async_playwright
        print("  [OK] Playwright导入成功")
        return True
    except ImportError as e:
        print(f"  [FAIL] Playwright导入失败: {e}")
        print("  请运行: pip install playwright && playwright install chromium")
        return False

async def test_launch_browser():
    """启动浏览器测试"""
    print("\n[测试2] 启动浏览器测试")
    try:
        from playwright.async_api import async_playwright
        
        print("  启动Playwright...")
        playwright = await async_playwright().start()
        
        print("  启动Chromium...")
        browser = await playwright.chromium.launch(headless=True)
        
        print("  创建页面...")
        page = await browser.new_page()
        
        print("  访问测试页面...")
        await page.goto("https://www.baidu.com", timeout=10000)
        
        print(f"  当前URL: {page.url}")
        
        await browser.close()
        print("  [OK] 浏览器测试成功")
        return True
        
    except Exception as e:
        print(f"  [FAIL] 浏览器测试失败: {e}")
        return False

async def test_fanqie_page():
    """访问番茄页面测试"""
    print("\n[测试3] 访问番茄作家助手测试")
    try:
        from playwright.async_api import async_playwright
        
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("  访问番茄作家助手...")
        await page.goto("https://fanqienovel.com/writer", timeout=30000, wait_until="networkidle")
        
        url = page.url
        print(f"  当前URL: {url}")
        
        if "login" in url or "passport" in url:
            print("  [WARN] 需要登录")
        else:
            print("  [OK] 已登录或可访问")
        
        await page.screenshot(path="test_fanqie_screenshot.png")
        print("  [OK] 截图保存: test_fanqie_screenshot.png")
        
        await browser.close()
        return True
        
    except Exception as e:
        print(f"  [FAIL] 访问失败: {e}")
        return False

async def test_parse_chapter():
    """解析章节测试"""
    print("\n[测试4] 解析章节文件测试")
    try:
        from publisher import parse_markdown_file
        from pathlib import Path
        
        chapter_file = Path(__file__).parent.parent.parent / "正文" / "第001章_大嘴侦探登场.md"
        
        if not chapter_file.exists():
            print(f"  [WARN] 章节文件不存在: {chapter_file}")
            return False
        
        print(f"  解析文件: {chapter_file.name}")
        chapter = parse_markdown_file(str(chapter_file))
        
        if chapter:
            print(f"  [OK] 解析成功")
            print(f"    标题: {chapter.title}")
            print(f"    章节号: {chapter.chapter_number}")
            print(f"    字数: {chapter.word_count}")
            return True
        else:
            print("  [FAIL] 解析失败")
            return False
            
    except Exception as e:
        print(f"  [FAIL] 测试失败: {e}")
        return False

async def main():
    results = []
    
    results.append(await test_basic())
    results.append(await test_launch_browser())
    results.append(await test_fanqie_page())
    results.append(await test_parse_chapter())
    
    print("\n" + "="*60)
    print("测试结果汇总")
    print("="*60)
    
    names = ["Playwright导入", "启动浏览器", "访问番茄页面", "解析章节文件"]
    for name, result in zip(names, results):
        status = "[OK] 通过" if result else "[FAIL] 失败"
        print(f"  {name}: {status}")
    
    success_count = sum(results)
    print(f"\n总计: {success_count}/{len(results)} 通过")
    
    return success_count == len(results)

if __name__ == "__main__":
    try:
        success = asyncio.run(main())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n用户中断")
        sys.exit(1)

"""
简单测试脚本 - 测试Playwright和浏览器连接
"""

import asyncio
import sys

print("="*60)
print("简单测试脚本")
print("="*60)

async def test_playwright():
    print("\n1. 测试Playwright导入...")
    try:
        from playwright.async_api import async_playwright
        print("   ✅ Playwright导入成功")
    except ImportError as e:
        print(f"   ❌ Playwright导入失败: {e}")
        return False
    
    print("\n2. 测试启动浏览器...")
    try:
        playwright = await async_playwright().start()
        print("   ✅ Playwright启动成功")
        
        print("\n3. 启动Chromium浏览器...")
        browser = await playwright.chromium.launch(headless=False)
        print("   ✅ 浏览器启动成功")
        
        print("\n4. 创建新页面...")
        page = await browser.new_page()
        print("   ✅ 页面创建成功")
        
        print("\n5. 访问番茄作家助手...")
        await page.goto("https://fanqienovel.com/writer", wait_until="networkidle", timeout=30000)
        print(f"   ✅ 页面加载成功")
        print(f"   当前URL: {page.url}")
        
        print("\n6. 截图...")
        await page.screenshot(path="test_fanqie.png")
        print("   ✅ 截图保存: test_fanqie.png")
        
        print("\n7. 等待5秒，请查看浏览器...")
        await asyncio.sleep(5)
        
        print("\n8. 关闭浏览器...")
        await browser.close()
        print("   ✅ 浏览器已关闭")
        
        return True
        
    except Exception as e:
        print(f"   ❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_cdp_connection():
    """测试CDP连接"""
    print("\n" + "="*60)
    print("测试CDP连接 (需要先启动调试模式浏览器)")
    print("="*60)
    
    print("\n启动命令: chrome.exe --remote-debugging-port=9222")
    print("或者: msedge.exe --remote-debugging-port=9222")
    
    try:
        from playwright.async_api import async_playwright
        
        print("\n1. 启动Playwright...")
        playwright = await async_playwright().start()
        
        print("\n2. 尝试连接到CDP端口 9222...")
        cdp_url = "http://127.0.0.1:9222"
        
        try:
            browser = await playwright.chromium.connect_over_cdp(cdp_url)
            print(f"   ✅ CDP连接成功: {cdp_url}")
            
            contexts = browser.contexts
            if contexts:
                context = contexts[0]
                pages = context.pages
                if pages:
                    page = pages[0]
                    print(f"   当前页面URL: {page.url}")
                else:
                    page = await context.new_page()
                    print("   创建新页面")
            else:
                context = await browser.new_context()
                page = await context.new_page()
                print("   创建新上下文和页面")
            
            print("\n3. 导航到番茄作家助手...")
            await page.goto("https://fanqienovel.com/writer", wait_until="networkidle", timeout=30000)
            print(f"   ✅ 导航成功")
            print(f"   当前URL: {page.url}")
            
            print("\n4. 截图...")
            await page.screenshot(path="test_cdp_fanqie.png")
            print("   ✅ 截图保存: test_cdp_fanqie.png")
            
            print("\n5. 等待5秒...")
            await asyncio.sleep(5)
            
            return True
            
        except Exception as e:
            print(f"   ❌ CDP连接失败: {e}")
            print("   请确保已启动调试模式浏览器")
            return False
            
    except Exception as e:
        print(f"   ❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    print("\n选择测试:")
    print("  1. 测试Playwright基本功能（启动新浏览器）")
    print("  2. 测试CDP连接（连接已有浏览器）")
    print("  3. 两者都测试")
    
    choice = input("\n请选择 (1/2/3): ").strip()
    
    if choice == '1':
        await test_playwright()
    elif choice == '2':
        await test_cdp_connection()
    elif choice == '3':
        await test_playwright()
        print("\n" + "="*60)
        await test_cdp_connection()
    else:
        print("无效选择，运行基本测试...")
        await test_playwright()

if __name__ == "__main__":
    asyncio.run(main())

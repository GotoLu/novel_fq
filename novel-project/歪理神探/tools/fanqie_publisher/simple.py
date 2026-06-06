import asyncio
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

async def main():
    print("Starting test...")
    from playwright.async_api import async_playwright
    
    print("1. Starting Playwright...")
    playwright = await async_playwright().start()
    print("   OK")
    
    print("2. Launching browser...")
    browser = await playwright.chromium.launch(headless=False)
    print("   OK")
    
    print("3. Creating page...")
    page = await browser.new_page()
    print("   OK")
    
    print("4. Navigating to Fanqie...")
    await page.goto("https://fanqienovel.com/writer", timeout=30000)
    print(f"   URL: {page.url}")
    
    print("5. Taking screenshot...")
    await page.screenshot(path="test.png")
    print("   Saved: test.png")
    
    print("6. Waiting 5 seconds...")
    await asyncio.sleep(5)
    
    print("7. Closing...")
    await browser.close()
    print("   Done!")

asyncio.run(main())

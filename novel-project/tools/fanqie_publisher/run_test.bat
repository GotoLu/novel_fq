@echo off
chcp 65001 >nul
echo ============================================================
echo 番茄作家助手发布工具 - 调试测试
echo ============================================================
echo.

cd /d "%~dp0"

echo 1. 检查Python版本...
python --version
echo.

echo 2. 检查Playwright安装...
python -c "from playwright.async_api import async_playwright; print('Playwright OK')"
if errorlevel 1 (
    echo Playwright未安装，正在安装...
    python -m pip install playwright
    python -m playwright install chromium
)
echo.

echo 3. 运行简单测试...
python -c "import asyncio; from playwright.async_api import async_playwright; asyncio.run(async_playwright().start()); print('Playwright启动成功')"
echo.

echo 4. 启动测试浏览器...
echo 请在新打开的浏览器中登录番茄作家助手
echo 登录地址: https://fanqienovel.com/writer
echo.
pause

echo.
echo 5. 运行完整测试...
python simple_test.py

echo.
echo ============================================================
echo 测试完成
echo ============================================================
pause

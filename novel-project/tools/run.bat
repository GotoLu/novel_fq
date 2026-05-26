@echo off
chcp 65001 >nul
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║         番茄作家助手自动提交工具                         ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0"

if "%1"=="" goto menu
if "%1"=="install" goto install
if "%1"=="browser" goto browser
if "%1"=="submit" goto submit
if "%1"=="batch" goto batch
goto menu

:menu
echo 请选择操作:
echo.
echo   1. 安装依赖
echo   2. 启动调试浏览器
echo   3. 提交单个章节
echo   4. 批量提交章节
echo   5. 运行示例
echo   0. 退出
echo.

set /p choice="请输入选项: "

if "%choice%"=="1" goto install
if "%choice%"=="2" goto browser
if "%choice%"=="3" goto submit
if "%choice%"=="4" goto batch
if "%choice%"=="5" goto example
if "%choice%"=="0" goto end
goto menu

:install
echo.
echo [安装依赖]
echo.
pip install -r fanqie_publisher\requirements.txt
echo.
echo 安装Playwright浏览器...
playwright install chromium
echo.
echo ✅ 安装完成
pause
goto menu

:browser
echo.
echo [启动调试浏览器]
echo.
python -m fanqie_publisher.cli browser --start
pause
goto menu

:submit
echo.
echo [提交单个章节]
echo.
set /p file="请输入章节文件路径: "
python -m fanqie_publisher.cli submit -f "%file%"
pause
goto menu

:batch
echo.
echo [批量提交章节]
echo.
set /p dir="请输入章节目录 (默认为正文): "
if "%dir%"=="" set dir=..\正文
python -m fanqie_publisher.cli batch -d "%dir%" --sort -o "%dir%\submit_report.json"
pause
goto menu

:example
echo.
echo [运行示例]
echo.
python fanqie_publisher\examples.py
pause
goto menu

:end
echo.
echo 再见!
exit /b 0

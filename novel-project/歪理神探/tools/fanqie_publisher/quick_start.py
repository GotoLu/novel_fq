"""
快速开始示例
演示如何使用番茄作家助手发布工具
"""

import asyncio
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
if os.path.exists(lib_path):
    sys.path.insert(0, lib_path)

from publisher import (
    FanqiePublisher,
    FanqiePublisherConfig,
    ChapterContent,
    SubmitStatus,
    parse_markdown_file
)


async def quick_start():
    """快速开始示例"""
    
    print("="*60)
    print("番茄作家助手发布工具 - 快速开始")
    print("="*60)
    
    # 1. 创建配置
    print("\n[步骤1] 创建配置...")
    config = FanqiePublisherConfig(
        cdp_port=9222,          # CDP端口
        headless=False,         # 非无头模式，可以看到浏览器
        timeout=30000,          # 超时时间30秒
        max_retries=3,          # 最大重试3次
        screenshot_on_error=True # 失败时截图
    )
    print("  配置创建成功")
    
    # 2. 创建发布器
    print("\n[步骤2] 创建发布器...")
    publisher = FanqiePublisher(config)
    
    # 设置状态回调
    def on_status(status: SubmitStatus, message: str):
        print(f"  [{status.value}] {message}")
    
    publisher.set_status_callback(on_status)
    print("  发布器创建成功")
    
    # 3. 连接浏览器
    print("\n[步骤3] 连接浏览器...")
    print("  提示: 如果连接失败，请先启动调试模式浏览器")
    print("  命令: chrome.exe --remote-debugging-port=9222")
    
    if not await publisher.connect_browser():
        print("  [ERROR] 浏览器连接失败")
        print("  请确保:")
        print("  1. 已启动Chrome调试模式")
        print("  2. 端口9222未被占用")
        return False
    
    # 4. 导航到作家后台
    print("\n[步骤4] 导航到作家后台...")
    if not await publisher.navigate_to_writer():
        print("  [ERROR] 导航失败")
        print("  可能需要先登录番茄作家助手")
        await publisher.close()
        return False
    
    # 5. 解析章节文件
    print("\n[步骤5] 解析章节文件...")
    chapter_file = os.path.join(
        os.path.dirname(__file__),
        "..", "..", "正文", "第001章_大嘴侦探登场.md"
    )
    chapter_file = os.path.abspath(chapter_file)
    
    if not os.path.exists(chapter_file):
        print(f"  [ERROR] 文件不存在: {chapter_file}")
        await publisher.close()
        return False
    
    chapter = parse_markdown_file(chapter_file)
    if not chapter:
        print("  [ERROR] 解析失败")
        await publisher.close()
        return False
    
    print(f"  标题: {chapter.title}")
    print(f"  字数: {chapter.word_count}")
    
    # 6. 提交草稿
    print("\n[步骤6] 提交草稿...")
    print("  警告: 这将实际提交到番茄作家助手!")
    
    confirm = input("  确认提交? (y/n): ")
    if confirm.lower() != 'y':
        print("  已取消")
        await publisher.close()
        return False
    
    result = await publisher.submit_to_draft(chapter)
    
    # 7. 显示结果
    print("\n[步骤7] 显示结果...")
    if result.is_success:
        print("  [SUCCESS] 提交成功!")
        print(f"  时间: {result.submit_time}")
    else:
        print("  [FAILED] 提交失败")
        print(f"  错误: {result.error_message}")
        if result.screenshot_path:
            print(f"  截图: {result.screenshot_path}")
    
    # 8. 关闭
    print("\n[步骤8] 关闭连接...")
    await publisher.close()
    
    return result.is_success


async def demo_without_submit():
    """演示模式（不实际提交）"""
    
    print("="*60)
    print("演示模式 - 不实际提交")
    print("="*60)
    
    # 创建配置
    config = FanqiePublisherConfig()
    publisher = FanqiePublisher(config)
    
    # 连接浏览器
    print("\n尝试连接浏览器...")
    if await publisher.connect_browser():
        print("浏览器连接成功!")
        
        # 获取当前URL
        url = publisher.page.url
        print(f"当前URL: {url}")
        
        # 截图
        await publisher.page.screenshot(path="demo_screenshot.png")
        print("截图保存: demo_screenshot.png")
        
        await publisher.close()
    else:
        print("浏览器连接失败")


if __name__ == "__main__":
    print("\n选择模式:")
    print("  1. 快速开始（实际提交）")
    print("  2. 演示模式（不提交）")
    
    choice = input("\n请选择 (1/2): ").strip()
    
    if choice == '1':
        asyncio.run(quick_start())
    elif choice == '2':
        asyncio.run(demo_without_submit())
    else:
        print("无效选择")

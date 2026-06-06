"""
使用示例脚本
演示如何使用番茄作家助手自动提交工具
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from fanqie_publisher import (
    FanqiePublisher,
    FanqiePublisherConfig,
    ChapterContent,
    SubmitStatus,
    parse_markdown_file,
    generate_report
)


async def example_submit_single():
    """示例：提交单个章节"""
    print("=" * 60)
    print("示例：提交单个章节")
    print("=" * 60)
    
    config = FanqiePublisherConfig(
        cdp_port=9222,
        headless=False,
        max_retries=3,
        screenshot_on_error=True
    )
    
    publisher = FanqiePublisher(config)
    
    def on_status(status: SubmitStatus, message: str):
        icons = {
            SubmitStatus.PENDING: "⏳",
            SubmitStatus.PREPARING: "🔧",
            SubmitStatus.SUBMITTING: "📤",
            SubmitStatus.SUCCESS: "✅",
            SubmitStatus.FAILED: "❌",
            SubmitStatus.RETRYING: "🔄"
        }
        print(f"{icons.get(status, '📌')} {message}")
    
    publisher.set_status_callback(on_status)
    
    try:
        print("\n1. 连接浏览器...")
        if not await publisher.connect_browser():
            print("❌ 连接失败，请确保浏览器已启动调试模式")
            print("启动命令: chrome.exe --remote-debugging-port=9222")
            return
        
        print("\n2. 导航到作家后台...")
        if not await publisher.navigate_to_writer():
            print("❌ 导航失败")
            return
        
        print("\n3. 准备章节内容...")
        chapter = ChapterContent(
            title="测试章节 - 自动提交示例",
            content="这是第一段内容。\n\n这是第二段内容。\n\n这是第三段内容，用于测试自动提交功能。",
            chapter_number=999
        )
        print(f"   标题: {chapter.title}")
        print(f"   字数: {chapter.word_count}")
        
        print("\n4. 提交到草稿...")
        result = await publisher.submit_to_draft(chapter)
        
        print("\n5. 提交结果:")
        if result.is_success:
            print(f"   ✅ 成功!")
            print(f"   时间: {result.submit_time}")
        else:
            print(f"   ❌ 失败")
            print(f"   错误: {result.error_message}")
            if result.screenshot_path:
                print(f"   截图: {result.screenshot_path}")
        
    finally:
        await publisher.close()


async def example_submit_from_file():
    """示例：从文件提交"""
    print("=" * 60)
    print("示例：从Markdown文件提交")
    print("=" * 60)
    
    file_path = Path(__file__).parent.parent / "正文" / "第001章_大嘴侦探登场.md"
    
    if not file_path.exists():
        print(f"❌ 文件不存在: {file_path}")
        return
    
    print(f"\n解析文件: {file_path}")
    chapter = parse_markdown_file(str(file_path))
    
    if not chapter:
        print("❌ 解析失败")
        return
    
    print(f"   标题: {chapter.title}")
    print(f"   章节号: {chapter.chapter_number}")
    print(f"   字数: {chapter.word_count}")
    print(f"   内容预览: {chapter.content[:100]}...")
    
    config = FanqiePublisherConfig(cdp_port=9222)
    publisher = FanqiePublisher(config)
    
    try:
        if not await publisher.connect_browser():
            return
        if not await publisher.navigate_to_writer():
            return
        
        result = await publisher.submit_to_draft(chapter)
        
        if result.is_success:
            print(f"\n✅ 提交成功: {chapter.title}")
        else:
            print(f"\n❌ 提交失败: {result.error_message}")
        
    finally:
        await publisher.close()


async def example_batch_submit():
    """示例：批量提交"""
    print("=" * 60)
    print("示例：批量提交目录下所有章节")
    print("=" * 60)
    
    directory = Path(__file__).parent.parent / "正文"
    
    if not directory.exists():
        print(f"❌ 目录不存在: {directory}")
        return
    
    files = list(directory.glob("*.md"))
    files = [f for f in files if not f.name.startswith("草稿")]
    
    print(f"\n发现 {len(files)} 个文件:")
    for f in files:
        print(f"   - {f.name}")
    
    chapters = []
    for file_path in files:
        chapter = parse_markdown_file(str(file_path))
        if chapter:
            chapters.append(chapter)
    
    chapters.sort(key=lambda c: c.chapter_number or 999)
    
    print(f"\n解析到 {len(chapters)} 个章节:")
    for i, chapter in enumerate(chapters, 1):
        print(f"   {i}. {chapter.title} ({chapter.word_count}字)")
    
    config = FanqiePublisherConfig(cdp_port=9222)
    publisher = FanqiePublisher(config)
    
    try:
        if not await publisher.connect_browser():
            return
        if not await publisher.navigate_to_writer():
            return
        
        results = await publisher.submit_batch(chapters)
        
        success_count = sum(1 for r in results if r.is_success)
        print(f"\n📊 结果: 成功 {success_count}/{len(results)}")
        
        report_path = directory / "submit_report.json"
        generate_report(results, str(report_path))
        print(f"   报告已保存: {report_path}")
        
    finally:
        await publisher.close()


async def main():
    """主函数"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║         番茄作家助手自动提交工具 - 使用示例              ║
╚═══════════════════════════════════════════════════════════╝
""")
    
    print("请选择示例:")
    print("1. 提交单个章节（测试）")
    print("2. 从Markdown文件提交")
    print("3. 批量提交目录")
    print("0. 退出")
    
    choice = input("\n请输入选项 (0-3): ").strip()
    
    if choice == "1":
        await example_submit_single()
    elif choice == "2":
        await example_submit_from_file()
    elif choice == "3":
        await example_batch_submit()
    else:
        print("退出")


if __name__ == "__main__":
    asyncio.run(main())

"""
简单调试脚本
"""

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
if os.path.exists(lib_path):
    sys.path.insert(0, lib_path)

print("="*60)
print("简单调试测试")
print("="*60)

print("\n[步骤1] 检查Python版本")
print(f"Python: {sys.version}")

print("\n[步骤2] 检查lib目录")
print(f"lib路径: {lib_path}")
print(f"lib存在: {os.path.exists(lib_path)}")

if os.path.exists(lib_path):
    print(f"lib内容: {os.listdir(lib_path)[:5]}")

print("\n[步骤3] 尝试导入Playwright")
try:
    from playwright.async_api import async_playwright
    print("[OK] Playwright导入成功")
except ImportError as e:
    print(f"[FAIL] Playwright导入失败: {e}")
    sys.exit(1)

print("\n[步骤4] 尝试导入yaml")
try:
    import yaml
    print("[OK] yaml导入成功")
except ImportError as e:
    print(f"[FAIL] yaml导入失败: {e}")

print("\n[步骤5] 尝试导入publisher模块")
try:
    from publisher import FanqiePublisher, FanqiePublisherConfig
    print("[OK] publisher模块导入成功")
except Exception as e:
    print(f"[FAIL] publisher模块导入失败: {e}")
    import traceback
    traceback.print_exc()

print("\n[步骤6] 检查章节文件")
chapter_file = os.path.join(os.path.dirname(__file__), "..", "..", "正文", "第001章_大嘴侦探登场.md")
chapter_file = os.path.abspath(chapter_file)
print(f"章节文件路径: {chapter_file}")
print(f"章节文件存在: {os.path.exists(chapter_file)}")

if os.path.exists(chapter_file):
    try:
        from publisher import parse_markdown_file
        chapter = parse_markdown_file(chapter_file)
        if chapter:
            print(f"[OK] 章节解析成功")
            print(f"  标题: {chapter.title}")
            print(f"  字数: {chapter.word_count}")
        else:
            print("[FAIL] 章节解析失败")
    except Exception as e:
        print(f"[FAIL] 章节解析出错: {e}")

print("\n" + "="*60)
print("测试完成")
print("="*60)

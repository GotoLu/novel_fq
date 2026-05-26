# 番茄作家助手发布工具 - 调试报告

## 测试结果

### 基础测试（已通过）

| 测试项 | 状态 | 说明 |
|--------|------|------|
| Playwright导入 | ✅ 通过 | 已安装到 lib 目录 |
| yaml导入 | ✅ 通过 | 已安装到 lib 目录 |
| publisher模块导入 | ✅ 通过 | 核心模块正常 |
| 章节文件解析 | ✅ 通过 | 成功解析第001章 |

### 解析结果示例

```
标题: 第一章 大嘴侦探登场
字数: 4313
```

---

## 使用方法

### 方法一：使用CLI命令行工具

```powershell
# 进入工具目录
cd d:\workspace\ai\novel\novel-project\tools\fanqie_publisher

# 提交单个章节
python cli.py submit -f "../../正文/第001章_大嘴侦探登场.md"

# 批量提交
python cli.py batch -d "../../正文" -p "*.md"
```

### 方法二：启动调试浏览器后连接

```powershell
# 步骤1：启动Chrome调试模式
chrome.exe --remote-debugging-port=9222

# 步骤2：在浏览器中登录番茄作家助手
# 访问 https://fanqienovel.com/writer

# 步骤3：运行提交工具
python cli.py submit -f "../../正文/第001章_大嘴侦探登场.md" --cdp-port 9222
```

### 方法三：使用Python脚本

```python
import asyncio
from publisher import FanqiePublisher, FanqiePublisherConfig, parse_markdown_file

async def main():
    # 配置
    config = FanqiePublisherConfig(
        cdp_port=9222,
        headless=False,
        max_retries=3
    )
    
    # 创建发布器
    publisher = FanqiePublisher(config)
    
    # 连接浏览器
    await publisher.connect_browser()
    
    # 导航到作家后台
    await publisher.navigate_to_writer()
    
    # 解析章节
    chapter = parse_markdown_file("../../正文/第001章_大嘴侦探登场.md")
    
    # 提交草稿
    result = await publisher.submit_to_draft(chapter)
    
    # 关闭
    await publisher.close()

asyncio.run(main())
```

---

## 常见问题

### Q1: ModuleNotFoundError: No module named 'playwright'

**解决方案**：
```powershell
# 安装到lib目录
python -m pip install playwright pyyaml --target d:\workspace\ai\novel\novel-project\tools\fanqie_publisher\lib

# 安装浏览器
python -m playwright install chromium
```

### Q2: 连接浏览器失败

**解决方案**：
1. 确保已启动调试模式浏览器
2. 检查端口是否正确（默认9222）
3. 检查防火墙设置

### Q3: 需要登录

**解决方案**：
1. 在浏览器中手动登录番茄作家助手
2. 登录后工具会保持会话状态

### Q4: UnicodeEncodeError

**解决方案**：
- 设置环境变量：`$env:PYTHONIOENCODING="utf-8"`
- 或使用支持UTF-8的终端

---

## 文件结构

```
fanqie_publisher/
├── publisher.py      # 核心发布逻辑
├── cli.py            # 命令行接口
├── config.yaml       # 配置文件
├── requirements.txt  # 依赖列表
├── lib/              # 本地依赖库
│   ├── playwright/
│   └── yaml/
├── debug_test.py     # 调试测试脚本
├── auto_test.py      # 自动化测试
└── README.md         # 使用说明
```

---

## 下一步

1. **实际测试提交**：在真实环境中测试提交功能
2. **优化选择器**：根据番茄页面实际结构调整选择器
3. **添加错误处理**：增强异常处理和重试机制
4. **日志记录**：添加详细的日志记录功能

---

生成时间: 2026-05-27

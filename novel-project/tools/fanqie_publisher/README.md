# 番茄作家助手自动提交工具

基于 Playwright 浏览器自动化，模拟用户操作将文章提交到番茄作家助手草稿箱。

## 功能特性

- ✅ 自动连接已登录的浏览器（CDP协议）
- ✅ 支持单个章节和批量提交
- ✅ 自动解析Markdown文件提取标题和内容
- ✅ 完善的错误处理和重试机制
- ✅ 失败时自动截图便于排查
- ✅ 实时状态反馈
- ✅ 生成提交报告

## 安装

```bash
# 安装依赖
pip install -r requirements.txt

# 安装Playwright浏览器
playwright install chromium
```

## 使用方法

### 第一步：启动调试模式浏览器

```bash
# 方式一：使用工具启动
python -m fanqie_publisher.cli browser --start

# 方式二：手动启动
chrome.exe --remote-debugging-port=9222
```

### 第二步：在浏览器中登录

打开浏览器后，访问 https://fanqienovel.com/writer 并登录您的番茄作家助手账号。

### 第三步：提交章节

```bash
# 提交单个章节
python -m fanqie_publisher.cli submit -f "第001章_大嘴侦探登场.md"

# 批量提交目录下所有章节
python -m fanqie_publisher.cli batch -d "./正文" -o report.json

# 按章节号排序提交
python -m fanqie_publisher.cli batch -d "./正文" --sort

# 仅解析不提交（dry-run）
python -m fanqie_publisher.cli batch -d "./正文" --dry-run
```

## 命令行参数

### submit - 提交单个章节

| 参数 | 说明 |
|------|------|
| `-f, --file` | 章节文件路径（必需） |
| `-t, --title` | 章节标题（可选，默认从文件提取） |
| `-c, --config` | 配置文件路径 |
| `--cdp-port` | CDP端口（默认9222） |
| `--no-screenshot` | 失败时不截图 |

### batch - 批量提交

| 参数 | 说明 |
|------|------|
| `-d, --directory` | 章节目录（必需） |
| `-p, --pattern` | 文件匹配模式（默认*.md） |
| `-o, --output` | 报告输出路径 |
| `--sort` | 按章节号排序 |
| `--dry-run` | 仅解析不提交 |

## 配置文件

```yaml
cdp_port: 9222              # CDP调试端口
headless: false             # 是否无头模式
timeout: 30000              # 超时时间（毫秒）
max_retries: 3              # 最大重试次数
retry_delay: 2.0            # 重试间隔（秒）
screenshot_on_error: true   # 失败时截图
screenshot_dir: "./screenshots"
log_level: "INFO"
fanqie_url: "https://fanqienovel.com/writer"
slow_mo: 100                # 操作延迟（毫秒）
```

## Python API

```python
import asyncio
from fanqie_publisher import (
    FanqiePublisher,
    FanqiePublisherConfig,
    ChapterContent,
    parse_markdown_file
)

async def main():
    # 创建配置
    config = FanqiePublisherConfig(
        cdp_port=9222,
        max_retries=3
    )
    
    # 创建发布器
    publisher = FanqiePublisher(config)
    
    # 设置状态回调
    def on_status(status, message):
        print(f"[{status.value}] {message}")
    
    publisher.set_status_callback(on_status)
    
    try:
        # 连接浏览器
        await publisher.connect_browser()
        
        # 导航到作家后台
        await publisher.navigate_to_writer()
        
        # 解析文件
        chapter = parse_markdown_file("第001章_大嘴侦探登场.md")
        
        # 提交到草稿
        result = await publisher.submit_to_draft(chapter)
        
        if result.is_success:
            print("提交成功!")
        else:
            print(f"提交失败: {result.error_message}")
            
    finally:
        await publisher.close()

asyncio.run(main())
```

## 工作原理

1. **浏览器自动化**：使用 Playwright 控制真实浏览器，模拟用户操作
2. **CDP连接**：通过 Chrome DevTools Protocol 连接已登录的浏览器，复用登录态
3. **元素定位**：使用多种选择器策略定位页面元素，提高兼容性
4. **内容填充**：支持 ProseMirror 等富文本编辑器

## 注意事项

1. **登录状态**：提交前请确保已在浏览器中登录番茄作家助手
2. **浏览器端口**：确保调试端口未被占用
3. **网络稳定**：提交过程中请保持网络稳定
4. **人工确认**：建议在正式发布前人工检查草稿内容

## 错误代码

| 代码 | 说明 |
|------|------|
| 0 | 成功 |
| 1001 | 浏览器连接失败 |
| 1002 | 页面加载失败 |
| 1003 | 需要登录 |
| 1004 | 元素未找到 |
| 1005 | 内容填充失败 |
| 1006 | 提交失败 |
| 1007 | 超时 |
| 9999 | 未知错误 |

## 目录结构

```
fanqie_publisher/
├── __init__.py      # 包入口
├── publisher.py     # 核心发布逻辑
├── cli.py           # 命令行接口
├── config.yaml      # 配置文件
├── requirements.txt # 依赖
└── README.md        # 文档
```

## 许可证

MIT License

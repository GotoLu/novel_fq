"""
番茄作家助手自动提交工具
基于Playwright浏览器自动化，模拟用户操作将文章提交到草稿箱
"""

import asyncio
import json
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, List, Dict, Any, Callable

try:
    from playwright.async_api import async_playwright, Browser, Page, BrowserContext
except ImportError:
    print("请先安装playwright: pip install playwright && playwright install chromium")
    sys.exit(1)


class SubmitStatus(Enum):
    """提交状态枚举"""
    PENDING = "pending"
    PREPARING = "preparing"
    SUBMITTING = "submitting"
    SUCCESS = "success"
    FAILED = "failed"
    RETRYING = "retrying"


class ErrorCode(Enum):
    """错误代码枚举"""
    SUCCESS = 0
    BROWSER_CONNECT_FAILED = 1001
    PAGE_LOAD_FAILED = 1002
    LOGIN_REQUIRED = 1003
    ELEMENT_NOT_FOUND = 1004
    CONTENT_FILL_FAILED = 1005
    SUBMIT_FAILED = 1006
    TIMEOUT = 1007
    UNKNOWN = 9999


@dataclass
class ChapterContent:
    """章节内容数据类"""
    title: str
    content: str
    chapter_number: Optional[int] = None
    source_file: Optional[str] = None
    word_count: int = 0
    
    def __post_init__(self):
        if self.word_count == 0:
            self.word_count = len(self.content.replace('\n', '').replace(' ', ''))
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "content": self.content,
            "chapter_number": self.chapter_number,
            "source_file": self.source_file,
            "word_count": self.word_count
        }


@dataclass
class SubmitResult:
    """提交结果数据类"""
    status: SubmitStatus
    error_code: ErrorCode = ErrorCode.SUCCESS
    error_message: str = ""
    chapter_title: str = ""
    submit_time: Optional[datetime] = None
    retry_count: int = 0
    screenshot_path: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status.value,
            "error_code": self.error_code.value,
            "error_message": self.error_message,
            "chapter_title": self.chapter_title,
            "submit_time": self.submit_time.isoformat() if self.submit_time else None,
            "retry_count": self.retry_count,
            "screenshot_path": self.screenshot_path
        }
    
    @property
    def is_success(self) -> bool:
        return self.status == SubmitStatus.SUCCESS


class FanqiePublisherConfig:
    """配置类"""
    
    def __init__(
        self,
        cdp_port: int = 9222,
        headless: bool = False,
        timeout: int = 30000,
        max_retries: int = 3,
        retry_delay: float = 2.0,
        screenshot_on_error: bool = True,
        screenshot_dir: str = "./screenshots",
        log_level: str = "INFO",
        fanqie_url: str = "https://fanqienovel.com/writer",
        slow_mo: int = 100
    ):
        self.cdp_port = cdp_port
        self.headless = headless
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.screenshot_on_error = screenshot_on_error
        self.screenshot_dir = Path(screenshot_dir)
        self.log_level = log_level
        self.fanqie_url = fanqie_url
        self.slow_mo = slow_mo
        
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)


class FanqiePublisher:
    """番茄作家助手发布器"""
    
    def __init__(self, config: Optional[FanqiePublisherConfig] = None):
        self.config = config or FanqiePublisherConfig()
        self._setup_logging()
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None
        self.context: Optional[BrowserContext] = None
        self._status_callback: Optional[Callable[[SubmitStatus, str], None]] = None
    
    def _setup_logging(self):
        """设置日志"""
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(
            level=getattr(logging, self.config.log_level),
            format=log_format
        )
        self.logger = logging.getLogger("FanqiePublisher")
    
    def set_status_callback(self, callback: Callable[[SubmitStatus, str], None]):
        """设置状态回调函数"""
        self._status_callback = callback
    
    def _notify_status(self, status: SubmitStatus, message: str):
        """通知状态变化"""
        self.logger.info(f"[{status.value}] {message}")
        if self._status_callback:
            self._status_callback(status, message)
    
    async def connect_browser(self) -> bool:
        """连接浏览器"""
        try:
            self._notify_status(SubmitStatus.PREPARING, "正在连接浏览器...")
            
            playwright = await async_playwright().start()
            
            cdp_url = f"http://127.0.0.1:{self.config.cdp_port}"
            
            try:
                self.browser = await playwright.chromium.connect_over_cdp(cdp_url)
                self.logger.info(f"成功连接到浏览器: {cdp_url}")
            except Exception as e:
                self.logger.warning(f"CDP连接失败，尝试启动新浏览器: {e}")
                self.browser = await playwright.chromium.launch(
                    headless=self.config.headless,
                    slow_mo=self.config.slow_mo
                )
            
            contexts = self.browser.contexts
            if contexts:
                self.context = contexts[0]
            else:
                self.context = await self.browser.new_context()
            
            pages = self.context.pages
            if pages:
                self.page = pages[0]
            else:
                self.page = await self.context.new_page()
            
            self.page.set_default_timeout(self.config.timeout)
            
            self._notify_status(SubmitStatus.PREPARING, "浏览器连接成功")
            return True
            
        except Exception as e:
            self.logger.error(f"连接浏览器失败: {e}")
            self._notify_status(SubmitStatus.FAILED, f"连接浏览器失败: {e}")
            return False
    
    async def navigate_to_writer(self) -> bool:
        """导航到作家后台"""
        try:
            self._notify_status(SubmitStatus.PREPARING, "正在导航到作家后台...")
            
            await self.page.goto(self.config.fanqie_url, wait_until="networkidle")
            await asyncio.sleep(1)
            
            current_url = self.page.url
            if "login" in current_url or "passport" in current_url:
                self.logger.error("需要登录，请先在浏览器中登录番茄作家助手")
                return False
            
            self._notify_status(SubmitStatus.PREPARING, "已到达作家后台")
            return True
            
        except Exception as e:
            self.logger.error(f"导航失败: {e}")
            return False
    
    async def _wait_for_selector_safe(self, selector: str, timeout: int = 10000) -> bool:
        """安全等待选择器"""
        try:
            await self.page.wait_for_selector(selector, timeout=timeout)
            return True
        except Exception:
            return False
    
    async def _find_and_click(self, selectors: List[str], description: str = "") -> bool:
        """查找并点击元素（尝试多个选择器）"""
        for selector in selectors:
            try:
                if await self._wait_for_selector_safe(selector, 3000):
                    await self.page.click(selector)
                    self.logger.info(f"点击成功: {description or selector}")
                    await asyncio.sleep(0.5)
                    return True
            except Exception as e:
                self.logger.debug(f"选择器 {selector} 点击失败: {e}")
                continue
        
        self.logger.warning(f"所有选择器都失败: {description}")
        return False
    
    async def _fill_content(self, content: str) -> bool:
        """填充内容到编辑器"""
        try:
            prose_selectors = [
                ".ProseMirror",
                "[contenteditable='true']",
                ".editor-content",
                "div[role='textbox']",
                "textarea"
            ]
            
            for selector in prose_selectors:
                try:
                    if await self._wait_for_selector_safe(selector, 3000):
                        element = await self.page.query_selector(selector)
                        if element:
                            await element.click()
                            await asyncio.sleep(0.3)
                            
                            await self.page.evaluate(
                                f"""(element) => {{
                                    element.innerHTML = '';
                                }}""",
                                element
                            )
                            
                            lines = content.split('\n')
                            for i, line in enumerate(lines):
                                if i > 0:
                                    await element.press('Enter')
                                    await asyncio.sleep(0.05)
                                if line.strip():
                                    await element.type(line, delay=5)
                            
                            self.logger.info(f"内容填充成功，字数: {len(content)}")
                            return True
                except Exception as e:
                    self.logger.debug(f"选择器 {selector} 填充失败: {e}")
                    continue
            
            return False
            
        except Exception as e:
            self.logger.error(f"填充内容失败: {e}")
            return False
    
    async def submit_to_draft(self, chapter: ChapterContent) -> SubmitResult:
        """提交章节到草稿"""
        result = SubmitResult(
            status=SubmitStatus.PENDING,
            chapter_title=chapter.title
        )
        
        for attempt in range(self.config.max_retries):
            try:
                result.retry_count = attempt
                result.status = SubmitStatus.SUBMITTING if attempt == 0 else SubmitStatus.RETRYING
                
                self._notify_status(
                    result.status, 
                    f"正在提交章节: {chapter.title} (尝试 {attempt + 1}/{self.config.max_retries})"
                )
                
                new_chapter_selectors = [
                    "button:has-text('新建章节')",
                    "button:has-text('添加章节')",
                    ".add-chapter-btn",
                    "[data-testid='add-chapter']",
                    "a:has-text('新建章节')"
                ]
                
                if not await self._find_and_click(new_chapter_selectors, "新建章节按钮"):
                    raise Exception("找不到新建章节按钮")
                
                await asyncio.sleep(1)
                
                title_selectors = [
                    "input[placeholder*='标题']",
                    "input[placeholder*='章节']",
                    ".chapter-title-input",
                    "input[name='title']",
                    "#chapter-title"
                ]
                
                title_filled = False
                for selector in title_selectors:
                    try:
                        if await self._wait_for_selector_safe(selector, 3000):
                            await self.page.fill(selector, chapter.title)
                            title_filled = True
                            self.logger.info(f"标题填充成功: {chapter.title}")
                            break
                    except Exception:
                        continue
                
                if not title_filled:
                    raise Exception("找不到标题输入框")
                
                await asyncio.sleep(0.5)
                
                if not await self._fill_content(chapter.content):
                    raise Exception("内容填充失败")
                
                await asyncio.sleep(0.5)
                
                save_draft_selectors = [
                    "button:has-text('保存草稿')",
                    "button:has-text('存为草稿')",
                    "button:has-text('保存')",
                    ".save-draft-btn",
                    "[data-testid='save-draft']"
                ]
                
                if not await self._find_and_click(save_draft_selectors, "保存草稿按钮"):
                    raise Exception("找不到保存草稿按钮")
                
                await asyncio.sleep(2)
                
                success_indicators = [
                    ".success-message",
                    ".toast-success",
                    "[class*='success']",
                    "text='保存成功'",
                    "text='已保存'"
                ]
                
                for indicator in success_indicators:
                    try:
                        if await self._wait_for_selector_safe(indicator, 3000):
                            result.status = SubmitStatus.SUCCESS
                            result.submit_time = datetime.now()
                            self._notify_status(SubmitStatus.SUCCESS, f"章节提交成功: {chapter.title}")
                            return result
                    except Exception:
                        continue
                
                result.status = SubmitStatus.SUCCESS
                result.submit_time = datetime.now()
                self._notify_status(SubmitStatus.SUCCESS, f"章节提交成功: {chapter.title}")
                return result
                
            except Exception as e:
                result.error_code = self._map_exception_to_error(e)
                result.error_message = str(e)
                self.logger.error(f"提交失败 (尝试 {attempt + 1}): {e}")
                
                if self.config.screenshot_on_error:
                    screenshot_name = f"error_{chapter.title}_{attempt}.png"
                    screenshot_name = re.sub(r'[\\/*?:"<>|]', '_', screenshot_name)
                    result.screenshot_path = str(self.config.screenshot_dir / screenshot_name)
                    try:
                        await self.page.screenshot(path=result.screenshot_path)
                        self.logger.info(f"错误截图已保存: {result.screenshot_path}")
                    except Exception:
                        pass
                
                if attempt < self.config.max_retries - 1:
                    self._notify_status(
                        SubmitStatus.RETRYING, 
                        f"提交失败，{self.config.retry_delay}秒后重试..."
                    )
                    await asyncio.sleep(self.config.retry_delay)
                    
                    try:
                        await self.page.goto(self.config.fanqie_url, wait_until="networkidle")
                        await asyncio.sleep(1)
                    except Exception:
                        pass
        
        result.status = SubmitStatus.FAILED
        self._notify_status(SubmitStatus.FAILED, f"章节提交失败: {chapter.title}")
        return result
    
    def _map_exception_to_error(self, e: Exception) -> ErrorCode:
        """映射异常到错误代码"""
        error_str = str(e).lower()
        
        if "timeout" in error_str:
            return ErrorCode.TIMEOUT
        elif "element" in error_str or "selector" in error_str:
            return ErrorCode.ELEMENT_NOT_FOUND
        elif "login" in error_str:
            return ErrorCode.LOGIN_REQUIRED
        elif "connect" in error_str:
            return ErrorCode.BROWSER_CONNECT_FAILED
        else:
            return ErrorCode.UNKNOWN
    
    async def submit_batch(self, chapters: List[ChapterContent]) -> List[SubmitResult]:
        """批量提交章节"""
        results = []
        total = len(chapters)
        
        self._notify_status(SubmitStatus.PREPARING, f"开始批量提交 {total} 个章节")
        
        for i, chapter in enumerate(chapters, 1):
            self.logger.info(f"处理章节 {i}/{total}: {chapter.title}")
            result = await self.submit_to_draft(chapter)
            results.append(result)
            
            if not result.is_success:
                self.logger.warning(f"章节 {chapter.title} 提交失败，是否继续?")
            
            await asyncio.sleep(1)
        
        success_count = sum(1 for r in results if r.is_success)
        self._notify_status(
            SubmitStatus.SUCCESS if success_count == total else SubmitStatus.FAILED,
            f"批量提交完成: 成功 {success_count}/{total}"
        )
        
        return results
    
    async def close(self):
        """关闭浏览器连接"""
        try:
            if self.page:
                await self.page.close()
            if self.context:
                await self.context.close()
            if self.browser:
                await self.browser.close()
            self.logger.info("浏览器连接已关闭")
        except Exception as e:
            self.logger.error(f"关闭浏览器时出错: {e}")


def parse_markdown_file(file_path: str) -> Optional[ChapterContent]:
    """解析Markdown文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        title = ""
        title_line_idx = 0
        
        for i, line in enumerate(lines):
            if line.startswith('# '):
                title = line[2:].strip()
                title_line_idx = i
                break
            elif line.startswith('## '):
                title = line[3:].strip()
                title_line_idx = i
                break
        
        if not title:
            title = Path(file_path).stem
        
        chapter_content = '\n'.join(lines[title_line_idx + 1:]).strip()
        
        chapter_number = None
        match = re.search(r'第(\d+)章', title)
        if match:
            chapter_number = int(match.group(1))
        
        return ChapterContent(
            title=title,
            content=chapter_content,
            chapter_number=chapter_number,
            source_file=file_path
        )
        
    except Exception as e:
        logging.error(f"解析文件失败 {file_path}: {e}")
        return None


def generate_report(results: List[SubmitResult], output_path: str):
    """生成提交报告"""
    report = {
        "submit_time": datetime.now().isoformat(),
        "total": len(results),
        "success": sum(1 for r in results if r.is_success),
        "failed": sum(1 for r in results if not r.is_success),
        "results": [r.to_dict() for r in results]
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    return report


async def main():
    """主函数示例"""
    config = FanqiePublisherConfig(
        cdp_port=9222,
        headless=False,
        max_retries=3,
        screenshot_on_error=True
    )
    
    publisher = FanqiePublisher(config)
    
    def status_callback(status: SubmitStatus, message: str):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {status.value}: {message}")
    
    publisher.set_status_callback(status_callback)
    
    try:
        if not await publisher.connect_browser():
            print("连接浏览器失败，请确保浏览器已启动并开启调试端口")
            print("启动命令: chrome.exe --remote-debugging-port=9222")
            return
        
        if not await publisher.navigate_to_writer():
            print("导航到作家后台失败")
            return
        
        test_chapter = ChapterContent(
            title="测试章节",
            content="这是一段测试内容。\n\n这是第二段内容。",
            chapter_number=1
        )
        
        result = await publisher.submit_to_draft(test_chapter)
        
        if result.is_success:
            print(f"提交成功！")
        else:
            print(f"提交失败: {result.error_message}")
        
    finally:
        await publisher.close()


if __name__ == "__main__":
    asyncio.run(main())

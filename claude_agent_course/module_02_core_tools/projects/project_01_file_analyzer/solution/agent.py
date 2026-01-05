"""
File Analyzer Agent Implementation
"""

import os
from dotenv import load_dotenv
from typing import AsyncGenerator
from claude_agent_sdk import (
    ClaudeSDKClient, 
    ClaudeAgentOptions, 
    AssistantMessage, 
    TextBlock
)

load_dotenv()

class FileAnalyzer:
    """文件分析器 - 使用 ClaudeSDKClient"""

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.base_url = os.getenv("ANTHROPIC_BASE_URL")
        self.model = os.getenv("MODEL_NAME", "claude-sonnet-4-20250514")
        self.client = None

    async def __aenter__(self):
        env_vars = {}
        if self.api_key:
            env_vars["ANTHROPIC_API_KEY"] = self.api_key
        if self.base_url:
            env_vars["ANTHROPIC_BASE_URL"] = self.base_url

        options = ClaudeAgentOptions(
            model=self.model,
            allowed_tools=["Read", "Bash"],
            permission_mode='acceptEdits',
            env=env_vars
        )

        self.client = ClaudeSDKClient(options=options)
        await self.client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.__aexit__(exc_type, exc_val, exc_tb)
            self.client = None

    async def _query(self, prompt: str) -> AsyncGenerator[str, None]:
        """发送查询并获取流式响应"""
        if not self.client:
            raise RuntimeError("请使用 async with FileAnalyzer() 创建实例")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def scan_directory(self, path: str = ".") -> str:
        """扫描目录结构"""
        prompt = f"""
        请分析目录 {path} 的结构：
        1. 使用 ls -la {path} 列出所有文件
        2. 按文件类型分类
        3. 返回结构化的文件列表
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        
        print()
        return "".join(result)

    async def count_lines(self, path: str = ".") -> str:
        """统计代码行数"""
        prompt = f"""
        统计 {path} 目录下的代码行数：
        1. 找出所有代码文件 (.py, .js, .md 等)
        2. 使用 wc -l 统计每个文件
        3. 按语言汇总
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        
        print()
        return "".join(result)

    async def generate_report(self, path: str = ".") -> str:
        """生成项目报告"""
        prompt = f"""
        为 {path} 生成 Markdown 项目报告：
        1. 使用 ls 查看目录结构
        2. 读取 README.md（如有）
        3. 统计代码行数
        4. 生成报告
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        
        print()
        return "".join(result)

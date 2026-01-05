"""
Bash Automation Agent Implementation
"""

import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from claude_agent_sdk import (
    ClaudeSDKClient, 
    ClaudeAgentOptions, 
    AssistantMessage, 
    TextBlock
)

load_dotenv()

class BashAutomation:
    """Bash 自动化助手 - 使用 ClaudeSDKClient"""

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
            allowed_tools=["Bash", "Read"],
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
        if not self.client:
            raise RuntimeError("请使用 async with BashAutomation() 创建实例")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def run_git_command(self, git_args: str) -> str:
        prompt = f"""
        执行 Git 命令并用中文解读结果：
        git {git_args}
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        print()
        return "".join(result)

    async def check_environment(self) -> str:
        prompt = """
        检查开发环境，执行以下命令并报告版本：
        1. python3 --version
        2. node --version
        3. git --version
        4. docker --version
        
        格式：✅ 已安装 或 ❌ 未安装
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        print()
        return "".join(result)

    async def analyze_logs(self, log_file: str) -> str:
        prompt = f"""
        分析日志文件 {log_file}：
        1. 查看最近 50 行
        2. 统计错误和警告数量
        3. 给出分析报告
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        print()
        return "".join(result)

    async def execute_command(self, command: str) -> str:
        prompt = f"执行命令并解释结果：{command}"
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        print()
        return "".join(result)

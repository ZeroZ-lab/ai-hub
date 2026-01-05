"""
Resume Analyzer Agent Implementation
"""

import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions, 
    AssistantMessage, 
    TextBlock,
    create_sdk_mcp_server
)
from solution.tools import extract_contact, extract_skills, calculate_match

load_dotenv()

# 创建 MCP 服务器
resume_server = create_sdk_mcp_server(
    name="resume",
    version="1.0.0",
    tools=[extract_contact, extract_skills, calculate_match]
)


class ResumeAnalyzer:
    """简历分析器 - 使用 ClaudeSDKClient"""

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
            mcp_servers={"resume": resume_server},
            allowed_tools=[
                "mcp__resume__extract_contact",
                "mcp__resume__extract_skills",
                "mcp__resume__calculate_match"
            ],
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
            raise RuntimeError("请使用 async with ResumeAnalyzer() 创建实例")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def analyze(self, resume_text: str) -> str:
        """分析简历"""
        prompt = f"""
        请分析这份简历，提取关键信息：
        
        {resume_text}
        
        使用提供的工具提取联系方式和技能。
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        print()
        return "".join(result)

    async def match_job(self, resume_text: str, requirements: list) -> str:
        """匹配职位"""
        prompt = f"""
        分析简历与职位要求的匹配度：
        
        ## 简历
        {resume_text[:800]}
        
        ## 职位要求技能
        {', '.join(requirements)}
        
        使用工具提取技能并计算匹配度。
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        print()
        return "".join(result)

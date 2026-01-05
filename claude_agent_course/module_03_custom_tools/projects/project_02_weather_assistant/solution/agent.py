"""
Weather Assistant Agent Implementation
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
from solution.tools import get_weather, get_clothing_advice, check_weather_alert

load_dotenv()

# 创建 MCP 服务器
weather_server = create_sdk_mcp_server(
    name="weather",
    version="1.0.0",
    tools=[get_weather, get_clothing_advice, check_weather_alert]
)


class WeatherAssistant:
    """天气助手 - 使用 ClaudeSDKClient"""

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
            mcp_servers={"weather": weather_server},
            allowed_tools=[
                "mcp__weather__get_weather",
                "mcp__weather__get_clothing_advice",
                "mcp__weather__check_weather_alert"
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
            raise RuntimeError("请使用 async with WeatherAssistant() 创建实例")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def query_weather(self, city: str) -> str:
        """查询天气"""
        prompt = f"""
        查询 {city} 的天气情况。
        
        请执行以下步骤：
        1. 获取天气数据
        2. 根据温度获取穿衣建议
        3. 检查是否有天气预警
        4. 汇总信息给用户
        """
        
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
            print(chunk, end="", flush=True)
        print()
        return "".join(result)

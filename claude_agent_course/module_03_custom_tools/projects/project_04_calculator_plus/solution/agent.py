"""Calculator Plus agent implementation."""

import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
    create_sdk_mcp_server,
)
from solution.tools import add, subtract, multiply, divide, power, sqrt, mean

load_dotenv()

calculator_server = create_sdk_mcp_server(
    name="calculator",
    version="1.0.0",
    tools=[add, subtract, multiply, divide, power, sqrt, mean],
)


class CalculatorPlus:
    """Calculator agent using ClaudeSDKClient."""

    def __init__(self) -> None:
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
            mcp_servers={"calculator": calculator_server},
            allowed_tools=[
                "mcp__calculator__add",
                "mcp__calculator__subtract",
                "mcp__calculator__multiply",
                "mcp__calculator__divide",
                "mcp__calculator__power",
                "mcp__calculator__sqrt",
                "mcp__calculator__mean",
            ],
            env=env_vars,
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
            raise RuntimeError("Use async with CalculatorPlus() to create an instance.")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def calculate(self, message: str) -> str:
        """Calculate based on user input."""
        prompt = f"""
You are a calculator. Use tools to compute the result.
Return only the final numeric result without extra text.

User input:
{message}
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

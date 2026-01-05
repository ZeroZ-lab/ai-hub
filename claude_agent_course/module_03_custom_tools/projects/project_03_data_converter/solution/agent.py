"""Data Converter agent implementation."""

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
from solution.tools import detect_format, csv_to_json, json_to_csv

load_dotenv()

converter_server = create_sdk_mcp_server(
    name="converter",
    version="1.0.0",
    tools=[detect_format, csv_to_json, json_to_csv],
)


class DataConverter:
    """Data converter agent using ClaudeSDKClient."""

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
            mcp_servers={"converter": converter_server},
            allowed_tools=[
                "mcp__converter__detect_format",
                "mcp__converter__csv_to_json",
                "mcp__converter__json_to_csv",
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
            raise RuntimeError("Use async with DataConverter() to create an instance.")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def detect_format(self, input_text: str) -> str:
        """Detect input format."""
        prompt = f"""
Detect the data format for the input text.
Use the detect_format tool. Return only one word: csv or json.

Input:
{input_text}
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def convert(self, input_text: str, target_format: str) -> str:
        """Convert input text to target format."""
        target_format = target_format.lower().strip()
        if target_format not in {"csv", "json"}:
            raise ValueError("target_format must be 'csv' or 'json'.")

        prompt = f"""
Convert the input data to the target format: {target_format}.

Rules:
- First, detect the input format using detect_format.
- If input format equals target, return the input unchanged.
- If input is CSV, call csv_to_json.
- If input is JSON, call json_to_csv.
- Output only the converted data and nothing else.

Input:
{input_text}
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

"""Filesystem MCP client solution."""

import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
)

load_dotenv()


class FilesystemAgent:
    """Filesystem MCP client agent."""

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

        # Get absolute path to samples directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)
        samples_dir = os.path.join(project_dir, "samples")

        # Configure filesystem MCP server
        options = ClaudeAgentOptions(
            model=self.model,
            mcp_servers={
                "fs": f"npx -y @modelcontextprotocol/server-filesystem {samples_dir}"
            },
            allowed_tools=[
                "mcp__fs__list_directory",
                "mcp__fs__read_file",
                "mcp__fs__search",
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
            raise RuntimeError("Use async with FilesystemAgent() to create an instance.")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def list_dir(self, path: str) -> str:
        prompt = f"""
List directory contents for: {path}
Use list_directory tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def read_file(self, path: str) -> str:
        prompt = f"""
Read file contents: {path}
Use read_file tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def search(self, path: str, keyword: str) -> str:
        prompt = f"""
Search for keyword "{keyword}" under: {path}
Use search tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

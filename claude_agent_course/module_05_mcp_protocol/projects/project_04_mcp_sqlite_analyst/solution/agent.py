"""SQLite MCP analyst solution."""

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


class SQLiteAnalyst:
    """SQLite MCP client agent."""

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

        # Get absolute path to samples database
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)
        db_path = os.path.join(project_dir, "samples", "sample.db")

        # Configure SQLite MCP server
        options = ClaudeAgentOptions(
            model=self.model,
            mcp_servers={
                "sqlite": f"npx -y @modelcontextprotocol/server-sqlite --db-path {db_path}"
            },
            allowed_tools=[
                "mcp__sqlite__list_tables",
                "mcp__sqlite__run_query",
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
            raise RuntimeError("Use async with SQLiteAnalyst() to create an instance.")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def list_tables(self, db_path: str) -> str:
        prompt = f"""
List tables for database: {db_path}
Use list_tables tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def run_query(self, db_path: str, query: str) -> str:
        prompt = f"""
Run SQL query on database: {db_path}
Query: {query}
Use run_query tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def aggregate(self, db_path: str, query: str) -> str:
        prompt = f"""
Run aggregate SQL query on database: {db_path}
Query: {query}
Use run_query tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

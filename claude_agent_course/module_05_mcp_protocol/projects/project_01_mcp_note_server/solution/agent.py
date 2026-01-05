"""MCP Notes client implementation."""

import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
)
from solution.server import notes_server

load_dotenv()


class NoteAgent:
    """Client agent for MCP note server."""

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
            mcp_servers={"notes": notes_server},
            allowed_tools=[
                "mcp__notes__add_note",
                "mcp__notes__list_notes",
                "mcp__notes__search_notes",
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
            raise RuntimeError("Use async with NoteAgent() to create an instance.")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def add_note(self, title: str, body: str) -> str:
        prompt = f"""
Add a note with the following details. Use add_note tool and return the JSON result only.

Title: {title}
Body: {body}
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def list_notes(self) -> str:
        prompt = """
List all notes. Use list_notes tool and return the JSON result only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def search_notes(self, keyword: str) -> str:
        prompt = f"""
Search notes by keyword: {keyword}.
Use search_notes tool and return the JSON result only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

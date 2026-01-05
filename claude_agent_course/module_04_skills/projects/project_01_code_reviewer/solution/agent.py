"""Code Reviewer agent implementation."""

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


class CodeReviewer:
    """Code review agent using ClaudeSDKClient and project skills."""

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
            setting_sources=["project"],
            allowed_tools=["Skill", "Read", "Bash"],
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
            raise RuntimeError("Use async with CodeReviewer() to create an instance.")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def review_file(self, file_path: str, content: str) -> str:
        """Review a single file with the code-reviewer skill."""
        prompt = f"""
Please review the following file. Focus on correctness, risks, and missing tests.
Use the code-reviewer skill and follow its output format.

File: {file_path}

```python
{content}
```
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

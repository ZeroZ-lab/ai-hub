"""Git MCP inspector solution."""

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


class GitInspector:
    """Git MCP client agent."""

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

        # Configure git MCP server pointing to current repository
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)

        options = ClaudeAgentOptions(
            model=self.model,
            mcp_servers={
                "git": f"npx -y @modelcontextprotocol/server-git --repository {project_dir}"
            },
            allowed_tools=[
                "mcp__git__recent_commits",
                "mcp__git__search_commits",
                "mcp__git__show_commit",
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
            raise RuntimeError("Use async with GitInspector() to create an instance.")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def recent_commits(self, repo_path: str, limit: int = 5) -> str:
        prompt = f"""
List the most recent {limit} commits for repo: {repo_path}
Use recent_commits tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def search_commits(self, repo_path: str, keyword: str) -> str:
        prompt = f"""
Search commits in repo: {repo_path} for keyword: {keyword}
Use search_commits tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def show_commit(self, repo_path: str, commit: str) -> str:
        prompt = f"""
Show details for commit {commit} in repo: {repo_path}
Use show_commit tool and return results only.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

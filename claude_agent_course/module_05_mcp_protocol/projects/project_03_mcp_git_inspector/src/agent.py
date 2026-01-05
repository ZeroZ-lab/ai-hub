"""
Git MCP inspector.

TODO:
1. Configure ClaudeAgentOptions with MCP server connection
2. Implement recent_commits, search_commits, show_commit
"""


class GitInspector:
    """Git MCP client agent."""

    def __init__(self):
        # TODO: set up ClaudeSDKClient options
        pass

    async def recent_commits(self, repo_path: str, limit: int = 5) -> str:
        """List recent commits."""
        # TODO: call MCP git tool
        pass

    async def search_commits(self, repo_path: str, keyword: str) -> str:
        """Search commits by keyword."""
        # TODO: call MCP git tool
        pass

    async def show_commit(self, repo_path: str, commit: str) -> str:
        """Show commit details."""
        # TODO: call MCP git tool
        pass

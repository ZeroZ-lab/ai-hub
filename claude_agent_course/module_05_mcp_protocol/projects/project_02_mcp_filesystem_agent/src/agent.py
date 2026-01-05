"""
Filesystem MCP client.

TODO:
1. Configure ClaudeAgentOptions with MCP server connection
2. Implement list_dir, read_file, search
"""


class FilesystemAgent:
    """Filesystem MCP client agent."""

    def __init__(self):
        # TODO: set up ClaudeSDKClient options
        pass

    async def list_dir(self, path: str) -> str:
        """List directory contents."""
        # TODO: call MCP filesystem tool
        pass

    async def read_file(self, path: str) -> str:
        """Read file contents."""
        # TODO: call MCP filesystem tool
        pass

    async def search(self, path: str, keyword: str) -> str:
        """Search keyword in files under path."""
        # TODO: call MCP filesystem tool
        pass

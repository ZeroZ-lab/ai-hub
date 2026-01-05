"""
News Aggregator agent.

TODO:
1. Create MCP server with tools from tools.py
2. Configure ClaudeAgentOptions with allowed tools
3. Implement top, search, category, digest methods
"""


class NewsAggregator:
    """News aggregator agent."""

    def __init__(self):
        # TODO: create MCP server and client options
        pass

    async def top(self, limit: int = 5) -> str:
        """Get top headlines."""
        # TODO: query the agent and return result
        pass

    async def search(self, query: str) -> str:
        """Search news."""
        # TODO: query the agent and return result
        pass

    async def category(self, category: str) -> str:
        """Filter news by category."""
        # TODO: query the agent and return result
        pass

    async def digest(self, query: str) -> str:
        """Summarize news for a topic."""
        # TODO: query the agent and return result
        pass

    async def sources(self) -> str:
        """List available sources."""
        # TODO: query the agent and return result
        pass

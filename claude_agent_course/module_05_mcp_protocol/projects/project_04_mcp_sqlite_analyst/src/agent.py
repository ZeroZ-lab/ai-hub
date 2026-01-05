"""
SQLite MCP analyst.

TODO:
1. Configure ClaudeAgentOptions with MCP server connection
2. Implement list_tables, run_query, aggregate
"""


class SQLiteAnalyst:
    """SQLite MCP client agent."""

    def __init__(self):
        # TODO: set up ClaudeSDKClient options
        pass

    async def list_tables(self, db_path: str) -> str:
        """List tables in database."""
        # TODO: call MCP sqlite tool
        pass

    async def run_query(self, db_path: str, query: str) -> str:
        """Run SQL query."""
        # TODO: call MCP sqlite tool
        pass

    async def aggregate(self, db_path: str, query: str) -> str:
        """Run aggregate query."""
        # TODO: call MCP sqlite tool
        pass

"""
Data Converter agent.

TODO:
1. Create MCP server with tools from tools.py
2. Configure ClaudeAgentOptions with allowed tools
3. Implement detect_format and convert methods
"""


class DataConverter:
    """Data converter agent."""

    def __init__(self):
        # TODO: create MCP server and client options
        pass

    async def detect_format(self, text: str) -> str:
        """Detect input format."""
        # TODO: query the agent and return format string
        pass

    async def convert(self, text: str, target_format: str) -> str:
        """Convert input text to target format."""
        # TODO: detect input format, then convert
        pass

"""
Notes client agent.

TODO:
1. Configure ClaudeAgentOptions with MCP server
2. Implement add_note, list_notes, search_notes
"""


class NoteAgent:
    """Client agent for MCP note server."""

    def __init__(self):
        # TODO: set up ClaudeSDKClient options
        pass

    async def add_note(self, title: str, body: str) -> str:
        """Add a note."""
        # TODO: prompt the agent and return result
        pass

    async def list_notes(self) -> str:
        """List notes."""
        # TODO: prompt the agent and return result
        pass

    async def search_notes(self, keyword: str) -> str:
        """Search notes by keyword."""
        # TODO: prompt the agent and return result
        pass

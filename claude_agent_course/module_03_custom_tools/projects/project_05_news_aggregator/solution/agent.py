"""News Aggregator agent implementation."""

import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
    create_sdk_mcp_server,
)
from solution.tools import (
    list_sources,
    get_top_headlines,
    search_news,
    filter_by_category,
    get_article,
)

load_dotenv()

news_server = create_sdk_mcp_server(
    name="news",
    version="1.0.0",
    tools=[list_sources, get_top_headlines, search_news, filter_by_category, get_article],
)


class NewsAggregator:
    """News aggregator agent using ClaudeSDKClient."""

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
            mcp_servers={"news": news_server},
            allowed_tools=[
                "mcp__news__list_sources",
                "mcp__news__get_top_headlines",
                "mcp__news__search_news",
                "mcp__news__filter_by_category",
                "mcp__news__get_article",
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
            raise RuntimeError("Use async with NewsAggregator() to create an instance.")

        await self.client.query(prompt=prompt)

        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    async def sources(self) -> str:
        """List available sources."""
        prompt = """
List available sources.
Call list_sources and return a bulleted list.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def top(self, limit: int = 5) -> str:
        """Get top headlines."""
        prompt = f"""
Get the latest {limit} headlines.
Call get_top_headlines with the limit and return a numbered list
with title and source.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def search(self, query: str) -> str:
        """Search news."""
        prompt = f"""
Search for news about: {query}.
Call search_news and return a numbered list with title and source.
If there are no results, say so.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def category(self, category: str) -> str:
        """Filter news by category."""
        prompt = f"""
Filter news by category: {category}.
Call filter_by_category and return a numbered list with title and source.
If there are no results, say so.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def digest(self, query: str) -> str:
        """Summarize news for a topic."""
        prompt = f"""
Create a short digest about: {query}.
Call search_news and then summarize up to 3 items.
Include source names in each bullet.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

    async def article(self, article_id: int) -> str:
        """Get a single article."""
        prompt = f"""
Get the article with id {article_id}.
Call get_article and return title, source, and summary.
"""
        result = []
        async for chunk in self._query(prompt):
            result.append(chunk)
        return "".join(result).strip()

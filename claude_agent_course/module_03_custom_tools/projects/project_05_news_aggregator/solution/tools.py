"""News Aggregator tools."""

import json
from pathlib import Path
from claude_agent_sdk import tool

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "articles.json"
_ARTICLE_CACHE = None


def _error(message: str) -> dict:
    return {
        "content": [{"type": "text", "text": message}],
        "is_error": True,
    }


def _load_articles() -> list[dict]:
    global _ARTICLE_CACHE
    if _ARTICLE_CACHE is None:
        if not DATA_PATH.exists():
            _ARTICLE_CACHE = []
        else:
            _ARTICLE_CACHE = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    return _ARTICLE_CACHE


def _serialize(articles: list[dict]) -> str:
    payload = []
    for article in articles:
        payload.append(
            {
                "id": article.get("id"),
                "title": article.get("title"),
                "source": article.get("source"),
                "category": article.get("category"),
                "published_at": article.get("published_at"),
                "summary": article.get("summary"),
                "url": article.get("url"),
            }
        )
    return json.dumps(payload, ensure_ascii=True)


@tool("list_sources", "List available news sources", {})
async def list_sources(args: dict) -> dict:
    """List sources."""
    articles = _load_articles()
    sources = sorted({article.get("source", "") for article in articles if article.get("source")})
    return {"content": [{"type": "text", "text": json.dumps(sources, ensure_ascii=True)}]}


@tool("get_top_headlines", "Get top headlines", {"limit": int})
async def get_top_headlines(args: dict) -> dict:
    """Get top headlines."""
    articles = _load_articles()
    limit = args.get("limit", 5)
    try:
        limit = int(limit)
    except (TypeError, ValueError):
        return _error("limit must be an integer.")

    sorted_articles = sorted(
        articles,
        key=lambda item: item.get("published_at", ""),
        reverse=True,
    )
    return {"content": [{"type": "text", "text": _serialize(sorted_articles[:limit])}]}


@tool("search_news", "Search news by keyword", {"query": str})
async def search_news(args: dict) -> dict:
    """Search news by keyword."""
    query = (args.get("query") or "").strip().lower()
    if not query:
        return _error("query is required.")

    articles = _load_articles()
    matches = []
    for article in articles:
        title = (article.get("title") or "").lower()
        summary = (article.get("summary") or "").lower()
        if query in title or query in summary:
            matches.append(article)

    return {"content": [{"type": "text", "text": _serialize(matches)}]}


@tool("filter_by_category", "Filter news by category", {"category": str})
async def filter_by_category(args: dict) -> dict:
    """Filter news by category."""
    category = (args.get("category") or "").strip().lower()
    if not category:
        return _error("category is required.")

    articles = _load_articles()
    matches = [article for article in articles if (article.get("category") or "").lower() == category]
    return {"content": [{"type": "text", "text": _serialize(matches)}]}


@tool("get_article", "Get a single article by id", {"article_id": int})
async def get_article(args: dict) -> dict:
    """Get an article by id."""
    article_id = args.get("article_id")
    try:
        article_id = int(article_id)
    except (TypeError, ValueError):
        return _error("article_id must be an integer.")

    articles = _load_articles()
    for article in articles:
        if article.get("id") == article_id:
            return {"content": [{"type": "text", "text": _serialize([article])}]}

    return _error(f"article_id {article_id} not found.")

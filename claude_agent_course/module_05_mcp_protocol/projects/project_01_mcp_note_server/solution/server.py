"""MCP Notes server implementation."""

import json
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import tool, create_sdk_mcp_server

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "notes.json"


def _load_notes() -> list[dict]:
    if not DATA_PATH.exists():
        return []
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def _save_notes(notes: list[dict]) -> None:
    DATA_PATH.write_text(json.dumps(notes, ensure_ascii=True, indent=2), encoding="utf-8")


def _error(message: str) -> dict:
    return {
        "content": [{"type": "text", "text": message}],
        "is_error": True,
    }


@tool("add_note", "Add a note", {"title": str, "body": str})
async def add_note(args: dict) -> dict:
    title = (args.get("title") or "").strip()
    body = (args.get("body") or "").strip()
    if not title or not body:
        return _error("title and body are required.")

    notes = _load_notes()
    next_id = max([note.get("id", 0) for note in notes], default=0) + 1
    note = {
        "id": next_id,
        "title": title,
        "body": body,
        "created_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    notes.append(note)
    _save_notes(notes)
    return {"content": [{"type": "text", "text": json.dumps(note, ensure_ascii=True)}]}


@tool("list_notes", "List notes", {})
async def list_notes(args: dict) -> dict:
    notes = _load_notes()
    summary = [
        {"id": note.get("id"), "title": note.get("title"), "created_at": note.get("created_at")}
        for note in notes
    ]
    return {"content": [{"type": "text", "text": json.dumps(summary, ensure_ascii=True)}]}


@tool("search_notes", "Search notes by keyword", {"keyword": str})
async def search_notes(args: dict) -> dict:
    keyword = (args.get("keyword") or "").strip().lower()
    if not keyword:
        return _error("keyword is required.")

    notes = _load_notes()
    matches = []
    for note in notes:
        title = (note.get("title") or "").lower()
        body = (note.get("body") or "").lower()
        if keyword in title or keyword in body:
            matches.append(note)

    return {"content": [{"type": "text", "text": json.dumps(matches, ensure_ascii=True)}]}


notes_server = create_sdk_mcp_server(
    name="notes",
    version="1.0.0",
    tools=[add_note, list_notes, search_notes],
)

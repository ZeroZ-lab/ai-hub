"""Data converter tools."""

import csv
import io
import json
from claude_agent_sdk import tool

SUPPORTED_FORMATS = ["csv", "json"]


def _error(message: str) -> dict:
    return {
        "content": [{"type": "text", "text": message}],
        "is_error": True,
    }


@tool("detect_format", "Detect input data format (csv or json)", {"text": str})
async def detect_format(args: dict) -> dict:
    """Detect input format."""
    text = (args.get("text") or "").strip()
    if not text:
        return _error("Input is empty.")

    if text.startswith("{") or text.startswith("["):
        return {"content": [{"type": "text", "text": "json"}]}

    lines = text.splitlines()
    if len(lines) > 1 and "," in lines[0]:
        return {"content": [{"type": "text", "text": "csv"}]}

    return _error("Unable to detect format. Expected CSV or JSON.")


@tool("csv_to_json", "Convert CSV text to JSON array", {"text": str})
async def csv_to_json(args: dict) -> dict:
    """Convert CSV text to JSON array."""
    text = (args.get("text") or "").strip()
    if not text:
        return _error("CSV input is empty.")

    reader = csv.DictReader(io.StringIO(text))
    if not reader.fieldnames:
        return _error("CSV header not found.")

    rows = list(reader)
    return {
        "content": [
            {"type": "text", "text": json.dumps(rows, ensure_ascii=True)}
        ]
    }


@tool("json_to_csv", "Convert JSON array/object to CSV", {"text": str})
async def json_to_csv(args: dict) -> dict:
    """Convert JSON array/object to CSV."""
    text = (args.get("text") or "").strip()
    if not text:
        return _error("JSON input is empty.")

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        return _error(f"Invalid JSON: {exc}")

    if isinstance(data, dict):
        data = [data]

    if not isinstance(data, list):
        return _error("JSON input must be an object or array of objects.")
    if not data:
        return _error("JSON array is empty.")

    fieldnames = []
    for row in data:
        if not isinstance(row, dict):
            return _error("JSON array must contain objects only.")
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        normalized = {}
        for key in fieldnames:
            value = row.get(key, "")
            if isinstance(value, (dict, list)):
                value = json.dumps(value, ensure_ascii=True)
            normalized[key] = value
        writer.writerow(normalized)

    return {"content": [{"type": "text", "text": output.getvalue()}]}

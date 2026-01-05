"""
Data conversion tools.

TODO: implement the following tools with @tool:
- detect_format
- csv_to_json
- json_to_csv
"""

SUPPORTED_FORMATS = ["csv", "json"]


# TODO: use @tool to implement detect_format
async def detect_format(args: dict) -> dict:
    """Detect input format (csv or json)."""
    pass


# TODO: use @tool to implement csv_to_json
async def csv_to_json(args: dict) -> dict:
    """Convert CSV text to JSON array."""
    pass


# TODO: use @tool to implement json_to_csv
async def json_to_csv(args: dict) -> dict:
    """Convert JSON array/object to CSV text."""
    pass

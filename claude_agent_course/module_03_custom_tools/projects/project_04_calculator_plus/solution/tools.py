"""Calculator Plus tools."""

import math
from claude_agent_sdk import tool


def _error(message: str) -> dict:
    return {
        "content": [{"type": "text", "text": message}],
        "is_error": True,
    }


def _parse_number(value) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _parse_numbers(args: dict) -> list[float] | None:
    numbers = args.get("numbers")
    if not isinstance(numbers, list) or not numbers:
        return None
    values = []
    for item in numbers:
        parsed = _parse_number(item)
        if parsed is None:
            return None
        values.append(parsed)
    return values


@tool("add", "Add numbers", {"numbers": list})
async def add(args: dict) -> dict:
    """Add numbers."""
    values = _parse_numbers(args)
    if values is None:
        return _error("numbers must be a non-empty list of numbers.")
    return {"content": [{"type": "text", "text": str(sum(values))}]}


@tool("subtract", "Subtract two numbers", {"a": float, "b": float})
async def subtract(args: dict) -> dict:
    """Subtract two numbers."""
    a = _parse_number(args.get("a"))
    b = _parse_number(args.get("b"))
    if a is None or b is None:
        return _error("a and b must be numbers.")
    return {"content": [{"type": "text", "text": str(a - b)}]}


@tool("multiply", "Multiply numbers", {"numbers": list})
async def multiply(args: dict) -> dict:
    """Multiply numbers."""
    values = _parse_numbers(args)
    if values is None:
        return _error("numbers must be a non-empty list of numbers.")
    result = 1.0
    for value in values:
        result *= value
    return {"content": [{"type": "text", "text": str(result)}]}


@tool("divide", "Divide two numbers", {"a": float, "b": float})
async def divide(args: dict) -> dict:
    """Divide two numbers."""
    a = _parse_number(args.get("a"))
    b = _parse_number(args.get("b"))
    if a is None or b is None:
        return _error("a and b must be numbers.")
    if b == 0:
        return _error("division by zero is not allowed.")
    return {"content": [{"type": "text", "text": str(a / b)}]}


@tool("power", "Raise a to the power of b", {"a": float, "b": float})
async def power(args: dict) -> dict:
    """Power operation."""
    a = _parse_number(args.get("a"))
    b = _parse_number(args.get("b"))
    if a is None or b is None:
        return _error("a and b must be numbers.")
    return {"content": [{"type": "text", "text": str(a ** b)}]}


@tool("sqrt", "Square root", {"value": float})
async def sqrt(args: dict) -> dict:
    """Square root."""
    value = _parse_number(args.get("value"))
    if value is None:
        return _error("value must be a number.")
    if value < 0:
        return _error("cannot take sqrt of a negative number.")
    return {"content": [{"type": "text", "text": str(math.sqrt(value))}]}


@tool("mean", "Mean of numbers", {"numbers": list})
async def mean(args: dict) -> dict:
    """Mean of numbers."""
    values = _parse_numbers(args)
    if values is None:
        return _error("numbers must be a non-empty list of numbers.")
    return {"content": [{"type": "text", "text": str(sum(values) / len(values))}]}

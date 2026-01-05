"""Code Reviewer solution CLI."""

import asyncio
from pathlib import Path
from solution.agent import CodeReviewer


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


async def main() -> None:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python src/main.py <file_path>")
        raise SystemExit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        raise SystemExit(1)

    content = _read_text(file_path)

    try:
        async with CodeReviewer() as agent:
            result = await agent.review_file(str(file_path), content)
            print(result)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    asyncio.run(main())

"""Code Reviewer CLI.

Run: uv run python src/main.py samples/payment_service.py
"""

import asyncio
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import CodeReviewer


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

    # TODO: agent = CodeReviewer()
    # TODO: result = await agent.review_file(str(file_path), content)
    # TODO: print(result)
    print("TODO: implement CodeReviewer.review_file")


if __name__ == "__main__":
    asyncio.run(main())

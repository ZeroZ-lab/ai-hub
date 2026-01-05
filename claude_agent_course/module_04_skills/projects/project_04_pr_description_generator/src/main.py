"""PR Description Generator CLI.

Run: uv run python src/main.py samples/change_notes.txt
"""

import asyncio
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import PRDescriptionGenerator


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

    change_notes = _read_text(file_path)

    # TODO: agent = PRDescriptionGenerator()
    # TODO: result = await agent.generate(change_notes)
    # TODO: print(result)
    print("TODO: implement PRDescriptionGenerator.generate")


if __name__ == "__main__":
    asyncio.run(main())

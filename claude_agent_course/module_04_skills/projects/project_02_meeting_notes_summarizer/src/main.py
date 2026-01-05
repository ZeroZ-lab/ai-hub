"""Meeting Notes Summarizer CLI.

Run: uv run python src/main.py samples/meeting_notes.txt
"""

import asyncio
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import MeetingNotesSummarizer


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

    notes = _read_text(file_path)

    # TODO: agent = MeetingNotesSummarizer()
    # TODO: result = await agent.summarize(notes)
    # TODO: print(result)
    print("TODO: implement MeetingNotesSummarizer.summarize")


if __name__ == "__main__":
    asyncio.run(main())

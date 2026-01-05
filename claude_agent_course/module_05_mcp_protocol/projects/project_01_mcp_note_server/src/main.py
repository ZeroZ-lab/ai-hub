"""MCP Note Server CLI.

Run: uv run python src/main.py
"""

import asyncio
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import NoteAgent


async def main() -> None:
    print("=" * 60)
    print("MCP Note Server")
    print("=" * 60)
    print("Commands:")
    print("  add <title> | <body>")
    print("  list")
    print("  search <keyword>")
    print("  exit")
    print("=" * 60)

    # TODO: agent = NoteAgent()

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Bye.")
                break

            if user_input.startswith("add "):
                # TODO: parse and call add_note
                print("TODO: implement add")
                continue

            if user_input.startswith("list"):
                # TODO: result = await agent.list_notes()
                print("TODO: implement list")
                continue

            if user_input.startswith("search "):
                # TODO: result = await agent.search_notes(keyword)
                print("TODO: implement search")
                continue

            print("Unknown command.")

        except KeyboardInterrupt:
            print("\nBye.")
            break
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    asyncio.run(main())

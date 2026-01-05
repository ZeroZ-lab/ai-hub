"""Filesystem MCP CLI.

Run: uv run python src/main.py
"""

import asyncio
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import FilesystemAgent


async def main() -> None:
    print("=" * 60)
    print("Filesystem MCP Agent")
    print("=" * 60)
    print("Commands:")
    print("  ls <path>")
    print("  read <path>")
    print("  search <path> <keyword>")
    print("  exit")
    print("=" * 60)

    # TODO: agent = FilesystemAgent()

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Bye.")
                break

            if user_input.startswith("ls "):
                print("TODO: implement ls")
                continue
            if user_input.startswith("read "):
                print("TODO: implement read")
                continue
            if user_input.startswith("search "):
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

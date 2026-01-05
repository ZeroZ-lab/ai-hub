"""Git MCP Inspector CLI.

Run: uv run python src/main.py
"""

import asyncio
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import GitInspector


async def main() -> None:
    print("=" * 60)
    print("Git MCP Inspector")
    print("=" * 60)
    print("Commands:")
    print("  recent <repo_path> [limit]")
    print("  search <repo_path> <keyword>")
    print("  show <repo_path> <commit>")
    print("  exit")
    print("=" * 60)

    # TODO: agent = GitInspector()

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Bye.")
                break

            if user_input.startswith("recent "):
                print("TODO: implement recent")
                continue
            if user_input.startswith("search "):
                print("TODO: implement search")
                continue
            if user_input.startswith("show "):
                print("TODO: implement show")
                continue

            print("Unknown command.")
        except KeyboardInterrupt:
            print("\nBye.")
            break
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    asyncio.run(main())

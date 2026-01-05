"""SQLite MCP Analyst CLI.

Run: uv run python src/main.py
"""

import asyncio
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import SQLiteAnalyst


async def main() -> None:
    print("=" * 60)
    print("SQLite MCP Analyst")
    print("=" * 60)
    print("Commands:")
    print("  tables <db_path>")
    print("  query <db_path> <sql>")
    print("  agg <db_path> <sql>")
    print("  exit")
    print("=" * 60)

    # TODO: agent = SQLiteAnalyst()

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Bye.")
                break

            if user_input.startswith("tables "):
                print("TODO: implement tables")
                continue
            if user_input.startswith("query "):
                print("TODO: implement query")
                continue
            if user_input.startswith("agg "):
                print("TODO: implement agg")
                continue

            print("Unknown command.")
        except KeyboardInterrupt:
            print("\nBye.")
            break
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    asyncio.run(main())

"""
News Aggregator CLI.

Run: uv run python src/main.py
"""

import asyncio
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import NewsAggregator


async def main() -> None:
    print("=" * 60)
    print("News Aggregator")
    print("=" * 60)
    print("Commands:")
    print("  top 5")
    print("  search <keyword>")
    print("  category <name>")
    print("  digest <keyword>")
    print("  sources")
    print("  exit")
    print("=" * 60)

    # TODO: agent = NewsAggregator()

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Bye.")
                break

            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else ""

            if command == "top":
                # TODO: result = await agent.top(int(arg) if arg else 5)
                print("TODO: implement NewsAggregator.top")
            elif command == "search":
                # TODO: result = await agent.search(arg)
                print("TODO: implement NewsAggregator.search")
            elif command == "category":
                # TODO: result = await agent.category(arg)
                print("TODO: implement NewsAggregator.category")
            elif command == "digest":
                # TODO: result = await agent.digest(arg)
                print("TODO: implement NewsAggregator.digest")
            elif command == "sources":
                # TODO: result = await agent.sources()
                print("TODO: implement NewsAggregator.sources")
            else:
                print(f"Unknown command: {command}")

        except KeyboardInterrupt:
            print("\nBye.")
            break
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    asyncio.run(main())

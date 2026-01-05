"""News Aggregator solution entry point."""

import asyncio
from solution.agent import NewsAggregator


async def main() -> None:
    print("=" * 60)
    print("News Aggregator (Solution)")
    print("=" * 60)
    print("Commands:")
    print("  top 5")
    print("  search <keyword>")
    print("  category <name>")
    print("  digest <keyword>")
    print("  sources")
    print("  article <id>")
    print("  exit")
    print("=" * 60)

    try:
        async with NewsAggregator() as agent:
            print("Ready.")

            while True:
                try:
                    user_input = input("\n> ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ["exit", "quit", "q"]:
                        break

                    parts = user_input.split(maxsplit=1)
                    command = parts[0].lower()
                    arg = parts[1] if len(parts) > 1 else ""

                    if command == "top":
                        limit = int(arg) if arg else 5
                        result = await agent.top(limit)
                    elif command == "search":
                        result = await agent.search(arg)
                    elif command == "category":
                        result = await agent.category(arg)
                    elif command == "digest":
                        result = await agent.digest(arg)
                    elif command == "sources":
                        result = await agent.sources()
                    elif command == "article":
                        if not arg:
                            print("Usage: article <id>")
                            continue
                        result = await agent.article(int(arg))
                    else:
                        print(f"Unknown command: {command}")
                        continue

                    print(result)

                except KeyboardInterrupt:
                    print("\nInterrupted.")
                    break

    except Exception as exc:
        print(f"Error: {exc}")

    print("Goodbye.")


if __name__ == "__main__":
    asyncio.run(main())

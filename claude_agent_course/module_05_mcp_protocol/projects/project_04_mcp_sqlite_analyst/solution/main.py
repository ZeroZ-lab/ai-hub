"""SQLite MCP Analyst solution CLI."""

import asyncio
from solution.agent import SQLiteAnalyst


async def main() -> None:
    print("=" * 60)
    print("SQLite MCP Analyst (Solution)")
    print("=" * 60)
    print("Commands:")
    print("  tables <db_path>")
    print("  query <db_path> <sql>")
    print("  agg <db_path> <sql>")
    print("  exit")
    print("=" * 60)

    try:
        async with SQLiteAnalyst() as agent:
            print("Ready.")

            while True:
                try:
                    user_input = input("\n> ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ["exit", "quit", "q"]:
                        break

                    if user_input.startswith("tables "):
                        db_path = user_input[7:].strip()
                        result = await agent.list_tables(db_path)
                        print(result)
                        continue

                    if user_input.startswith("query "):
                        parts = user_input.split(maxsplit=2)
                        if len(parts) < 3:
                            print("Usage: query <db_path> <sql>")
                            continue
                        _, db_path, sql = parts
                        result = await agent.run_query(db_path, sql)
                        print(result)
                        continue

                    if user_input.startswith("agg "):
                        parts = user_input.split(maxsplit=2)
                        if len(parts) < 3:
                            print("Usage: agg <db_path> <sql>")
                            continue
                        _, db_path, sql = parts
                        result = await agent.aggregate(db_path, sql)
                        print(result)
                        continue

                    print("Unknown command.")

                except KeyboardInterrupt:
                    print("\nInterrupted.")
                    break

    except Exception as exc:
        print(f"Error: {exc}")

    print("Goodbye.")


if __name__ == "__main__":
    asyncio.run(main())

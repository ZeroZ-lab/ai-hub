"""Git MCP Inspector solution CLI."""

import asyncio
from solution.agent import GitInspector


async def main() -> None:
    print("=" * 60)
    print("Git MCP Inspector (Solution)")
    print("=" * 60)
    print("Commands:")
    print("  recent <repo_path> [limit]")
    print("  search <repo_path> <keyword>")
    print("  show <repo_path> <commit>")
    print("  exit")
    print("=" * 60)

    try:
        async with GitInspector() as agent:
            print("Ready.")

            while True:
                try:
                    user_input = input("\n> ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ["exit", "quit", "q"]:
                        break

                    if user_input.startswith("recent "):
                        parts = user_input.split(maxsplit=2)
                        repo_path = parts[1] if len(parts) > 1 else ""
                        limit = int(parts[2]) if len(parts) > 2 else 5
                        result = await agent.recent_commits(repo_path, limit)
                        print(result)
                        continue

                    if user_input.startswith("search "):
                        parts = user_input.split(maxsplit=2)
                        if len(parts) < 3:
                            print("Usage: search <repo_path> <keyword>")
                            continue
                        _, repo_path, keyword = parts
                        result = await agent.search_commits(repo_path, keyword)
                        print(result)
                        continue

                    if user_input.startswith("show "):
                        parts = user_input.split(maxsplit=2)
                        if len(parts) < 3:
                            print("Usage: show <repo_path> <commit>")
                            continue
                        _, repo_path, commit = parts
                        result = await agent.show_commit(repo_path, commit)
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

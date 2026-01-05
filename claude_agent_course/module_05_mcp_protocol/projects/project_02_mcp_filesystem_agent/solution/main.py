"""Filesystem MCP CLI solution."""

import asyncio
from solution.agent import FilesystemAgent


async def main() -> None:
    print("=" * 60)
    print("Filesystem MCP Agent (Solution)")
    print("=" * 60)
    print("Commands:")
    print("  ls <path>")
    print("  read <path>")
    print("  search <path> <keyword>")
    print("  exit")
    print("=" * 60)

    try:
        async with FilesystemAgent() as agent:
            print("Ready.")

            while True:
                try:
                    user_input = input("\n> ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ["exit", "quit", "q"]:
                        break

                    if user_input.startswith("ls "):
                        path = user_input[3:].strip()
                        result = await agent.list_dir(path)
                        print(result)
                        continue

                    if user_input.startswith("read "):
                        path = user_input[5:].strip()
                        result = await agent.read_file(path)
                        print(result)
                        continue

                    if user_input.startswith("search "):
                        parts = user_input.split(maxsplit=2)
                        if len(parts) < 3:
                            print("Usage: search <path> <keyword>")
                            continue
                        _, path, keyword = parts
                        result = await agent.search(path, keyword)
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

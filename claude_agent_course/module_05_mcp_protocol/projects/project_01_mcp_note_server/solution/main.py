"""MCP Note Server solution CLI."""

import asyncio
from solution.agent import NoteAgent


def _parse_add_payload(text: str) -> tuple[str, str] | None:
    if "|" not in text:
        return None
    title, body = text.split("|", 1)
    title = title.strip()
    body = body.strip()
    if not title or not body:
        return None
    return title, body


async def main() -> None:
    print("=" * 60)
    print("MCP Note Server (Solution)")
    print("=" * 60)
    print("Commands:")
    print("  add <title> | <body>")
    print("  list")
    print("  search <keyword>")
    print("  exit")
    print("=" * 60)

    try:
        async with NoteAgent() as agent:
            print("Ready.")

            while True:
                try:
                    user_input = input("\n> ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ["exit", "quit", "q"]:
                        break

                    if user_input.startswith("add "):
                        payload = user_input[4:]
                        parsed = _parse_add_payload(payload)
                        if not parsed:
                            print("Usage: add <title> | <body>")
                            continue
                        title, body = parsed
                        result = await agent.add_note(title, body)
                        print(result)
                        continue

                    if user_input.startswith("list"):
                        result = await agent.list_notes()
                        print(result)
                        continue

                    if user_input.startswith("search "):
                        keyword = user_input[7:].strip()
                        if not keyword:
                            print("Usage: search <keyword>")
                            continue
                        result = await agent.search_notes(keyword)
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

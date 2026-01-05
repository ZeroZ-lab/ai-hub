"""Calculator Plus solution entry point."""

import asyncio
from solution.agent import CalculatorPlus


def _normalize_input(user_input: str) -> str:
    if user_input.lower().startswith("calc "):
        return user_input[5:]
    if user_input.lower().startswith("stats "):
        return user_input[6:]
    return user_input


async def main() -> None:
    print("=" * 60)
    print("Calculator Plus (Solution)")
    print("=" * 60)
    print("Examples:")
    print("  calc (3 + 5) * 2")
    print("  stats mean 3,5,9")
    print("  exit")
    print("=" * 60)

    try:
        async with CalculatorPlus() as agent:
            print("Ready.")

            while True:
                try:
                    user_input = input("\n> ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ["exit", "quit", "q"]:
                        break

                    query = _normalize_input(user_input)
                    result = await agent.calculate(query)
                    print(result)

                except KeyboardInterrupt:
                    print("\nInterrupted.")
                    break

    except Exception as exc:
        print(f"Error: {exc}")

    print("Goodbye.")


if __name__ == "__main__":
    asyncio.run(main())

"""
Calculator Plus CLI.

Run: uv run python src/main.py
"""

import asyncio
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import CalculatorPlus


async def main() -> None:
    print("=" * 60)
    print("Calculator Plus")
    print("=" * 60)
    print("Commands:")
    print("  calc <expression>")
    print("  stats mean 1,2,3")
    print("  exit")
    print("=" * 60)

    # TODO: agent = CalculatorPlus()

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Bye.")
                break

            # TODO: result = await agent.calculate(user_input)
            print("TODO: implement CalculatorPlus.calculate")

        except KeyboardInterrupt:
            print("\nBye.")
            break
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    asyncio.run(main())

"""
Data Converter CLI.

Run: uv run python src/main.py
"""

import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# TODO: from agent import DataConverter


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


async def main() -> None:
    print("=" * 60)
    print("Data Converter")
    print("=" * 60)
    print("Commands:")
    print("  detect <file>")
    print("  convert <file> <target_format> [output_file]")
    print("  exit")
    print("=" * 60)

    # TODO: converter = DataConverter()

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Bye.")
                break

            parts = user_input.split()
            command = parts[0].lower()

            if command == "detect":
                if len(parts) < 2:
                    print("Usage: detect <file>")
                    continue
                file_path = parts[1]
                if not os.path.exists(file_path):
                    print(f"File not found: {file_path}")
                    continue

                text = _read_text(file_path)
                # TODO: result = await converter.detect_format(text)
                print("TODO: implement detect_format")

            elif command == "convert":
                if len(parts) < 3:
                    print("Usage: convert <file> <target_format> [output_file]")
                    continue
                file_path = parts[1]
                target_format = parts[2].lower()
                output_path = parts[3] if len(parts) > 3 else None

                if not os.path.exists(file_path):
                    print(f"File not found: {file_path}")
                    continue

                text = _read_text(file_path)
                # TODO: result = await converter.convert(text, target_format)
                print("TODO: implement convert")

                if output_path:
                    print(f"Would write output to: {output_path}")

            else:
                print(f"Unknown command: {command}")

        except KeyboardInterrupt:
            print("\nBye.")
            break
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    asyncio.run(main())

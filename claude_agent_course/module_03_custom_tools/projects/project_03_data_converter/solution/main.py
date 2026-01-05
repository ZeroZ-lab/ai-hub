"""Data Converter solution entry point."""

import asyncio
from pathlib import Path
from solution.agent import DataConverter


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


async def main() -> None:
    print("=" * 60)
    print("Data Converter (Solution)")
    print("=" * 60)
    print("Commands:")
    print("  detect <file>")
    print("  convert <file> <target_format> [output_file]")
    print("  exit")
    print("=" * 60)

    try:
        async with DataConverter() as converter:
            print("Ready.")

            while True:
                try:
                    user_input = input("\n> ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ["exit", "quit", "q"]:
                        break

                    parts = user_input.split()
                    command = parts[0].lower()

                    if command == "detect":
                        if len(parts) < 2:
                            print("Usage: detect <file>")
                            continue

                        path = Path(parts[1])
                        if not path.exists():
                            print(f"File not found: {path}")
                            continue

                        text = _read_text(path)
                        fmt = await converter.detect_format(text)
                        print(fmt)

                    elif command == "convert":
                        if len(parts) < 3:
                            print("Usage: convert <file> <target_format> [output_file]")
                            continue

                        path = Path(parts[1])
                        if not path.exists():
                            print(f"File not found: {path}")
                            continue

                        target_format = parts[2].lower()
                        text = _read_text(path)
                        output_text = await converter.convert(text, target_format)

                        output_path = Path(parts[3]) if len(parts) > 3 else None
                        if output_path is None:
                            output_path = path.with_suffix(f".{target_format}")

                        _write_text(output_path, output_text)
                        print(f"Wrote output to: {output_path}")

                    else:
                        print(f"Unknown command: {command}")

                except KeyboardInterrupt:
                    print("\nInterrupted.")
                    break

    except Exception as exc:
        print(f"Error: {exc}")

    print("Goodbye.")


if __name__ == "__main__":
    asyncio.run(main())

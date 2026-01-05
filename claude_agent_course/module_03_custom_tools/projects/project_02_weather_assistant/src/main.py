"""
天气助手主程序

运行方式: uv run python src/main.py
"""

import asyncio
from agent import WeatherAssistant


async def main():
    print("=" * 50)
    print("🌤️  天气查询助手")
    print("=" * 50)
    print("输入城市名查询天气，输入 'quit' 退出\n")

    assistant = WeatherAssistant()

    while True:
        try:
            user_input = input("你: ").strip()
            if user_input.lower() in ["quit", "exit", "q"]:
                print("再见！")
                break
            if not user_input:
                continue

            response = await assistant.query(user_input)
            print(f"助手: {response}\n")

        except KeyboardInterrupt:
            print("\n再见！")
            break
        except Exception as e:
            print(f"错误: {e}\n")


if __name__ == "__main__":
    asyncio.run(main())

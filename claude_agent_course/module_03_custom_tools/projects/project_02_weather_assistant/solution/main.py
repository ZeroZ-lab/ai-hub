"""
Weather Assistant Solution Entry Point
"""

import asyncio
from solution.agent import WeatherAssistant

async def main():
    """主函数"""
    print("=" * 60)
    print("🌤️ Weather Assistant - 天气查询助手")
    print("=" * 60)
    print("\n支持城市: 北京, 上海, 广州, 深圳")
    print("可以直接输入城市名，或 exit 退出")
    print("=" * 60)

    try:
        async with WeatherAssistant() as agent:
            print("✅ 已连接到 Claude\n")

            while True:
                try:
                    user_input = input("\n💬 你: ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ['exit', 'quit']:
                        break

                    print()
                    await agent.query_weather(user_input)

                except KeyboardInterrupt:
                    print("\n\n⏸️ 中断...")
                    break

    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()

    print("\n👋 再见！")


if __name__ == "__main__":
    asyncio.run(main())

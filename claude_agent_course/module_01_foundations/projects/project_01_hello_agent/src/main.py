"""
Hello Agent - 主程序

Author: Your Name
Date: 2024-01-04
"""

import sys
import os
import asyncio
from dotenv import load_dotenv
from agent import FileAgent

load_dotenv()

# TODO: 1. 将 main 函数改为 async
async def main():
    """主函数"""
    print("=" * 60)
    print("🤖 Hello Agent - 文件查看助手")
    print("=" * 60)

    try:
        agent = FileAgent()
        print("✅ Agent 已启动\n")
    except ValueError as e:
        print(e)
        return

    # 交互循环
    while True:
        try:
            user_input = input("\n💬 你: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 再见！")
                break

            if user_input.lower() in ['ls', 'list']:
                print("\n🔍 正在分析文件...")
                # TODO: 2. 使用 async for 循环获取流式输出
                # async for chunk in agent.describe_files():
                #     print(chunk, end="", flush=True)
                pass
                
            # ... 其他命令 ...

        except KeyboardInterrupt:
            print("\n\n👋 检测到 Ctrl+C，退出程序")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")

if __name__ == "__main__":
    # TODO: 3. 使用 asyncio.run 运行主函数
    # asyncio.run(main())
    pass

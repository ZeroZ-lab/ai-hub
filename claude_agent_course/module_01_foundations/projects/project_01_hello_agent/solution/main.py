"""
Hello Agent - 完整参考实现

这是 Hello Agent 项目的完整实现。

Author: Claude Code Course
Date: 2024-01-04
"""

import sys
import os
import asyncio
from dotenv import load_dotenv
from agent import FileAgent

load_dotenv()


def show_environment():
    """显示环境信息"""
    print("\n📊 环境信息:")
    print(f"  Python 版本: {sys.version.split()[0]}")
    print(f"  当前目录: {os.getcwd()}")
    print()


async def main():
    """主函数"""
    print("=" * 60)
    print("🤖 Hello Agent - 文件查看助手")
    print("=" * 60)

    # 显示环境信息
    show_environment()

    # 创建 Agent
    try:
        agent = FileAgent()
        print("✅ Agent 已启动\n")
    except ValueError as e:
        print(e)
        return

    # 显示帮助
    print("命令列表:")
    print("  ls       - 列出并描述当前目录文件")
    print("  stat     - 统计文件类型")
    print("  help     - 显示帮助信息")
    print("  exit     - 退出程序")
    print("=" * 60)

    # 交互循环
    while True:
        try:
            # input 是阻塞的，但在简单 CLI 工具中可以接受
            user_input = input("\n💬 你: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit', '退出', 'q']:
                print("\n👋 再见！")
                break

            if user_input.lower() in ['help', 'h', '帮助']:
                print("\n可用命令:")
                print("  ls    - 列出并描述文件")
                print("  stat  - 统计文件类型")
                print("  exit  - 退出")
                continue

            if user_input.lower() in ['ls', 'list']:
                print("\n🔍 正在分析文件...")
                print(f"\n🤖 Agent:", end="\n", flush=True)
                async for chunk in agent.describe_files():
                    print(chunk, end="", flush=True)
                print() # 换行
                continue

            if user_input.lower() in ['stat', 'statistics']:
                print("\n📊 正在统计...")
                async for chunk in agent.statistics_report():
                    print(chunk, end="", flush=True)
                print() # 换行
                continue

            # 其他输入视为自由对话 (本项目未实现单纯聊天，仅文件操作)
            print("\n💡 提示: 使用 'ls' 查看文件，'stat' 查看统计，'help' 查看帮助")

        except KeyboardInterrupt:
            print("\n\n👋 检测到 Ctrl+C，退出程序")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")


if __name__ == "__main__":
    asyncio.run(main())

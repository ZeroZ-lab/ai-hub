"""高级 Agent 交互式 CLI"""

import asyncio
import os
from dotenv import load_dotenv
from agent import AdvancedAgent

load_dotenv()


def print_separator():
    """打印分隔线"""
    print("\n" + "=" * 60 + "\n")


def print_welcome():
    """打印欢迎信息"""
    print("╔════════════════════════════════════════════════════════════╗")
    print("║       🚀 高级 Agent - ClaudeSDKClient 演示                ║")
    print("║                                                            ║")
    print("║  可用命令:                                                 ║")
    print("║    <消息>      - 直接发送消息                              ║")
    print("║    /interrupt  - 中断当前执行                              ║")
    print("║    /session    - 显示会话 ID                               ║")
    print("║    /help       - 显示帮助                                  ║")
    print("║    /quit       - 断开并退出                                ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print_separator()


async def main():
    """主函数"""
    print_welcome()

    # 使用 async with 创建并管理 Agent
    try:
        async with AdvancedAgent() as agent:
            print("✅ 已连接到 Claude")
            print_separator()

            # 主交互循环
            while True:
                try:
                    user_input = input("💬 You: ").strip()

                    if not user_input:
                        continue

                    # 处理命令
                    if user_input.startswith('/'):
                        command = user_input.lower()

                        if command == '/quit':
                            print("\n👋 正在退出...")
                            break

                        elif command == '/help':
                            print("\n📚 可用命令:")
                            print("  <消息>      - 发送消息并获取回复")
                            print("  /interrupt  - 中断当前执行（如果 Agent 正在运行）")
                            print("  /session    - 显示当前会话 ID")
                            print("  /quit       - 退出程序")
                            continue

                        elif command == '/interrupt':
                            print("\n⏸️  中断执行...")
                            await agent.interrupt()
                            print("✅ 已发送中断信号")
                            continue

                        elif command == '/session':
                            session_id = agent.get_session_id()
                            print(f"\n📋 Session ID: {session_id or '未建立'}")
                            continue

                        else:
                            print(f"\n❌ 未知命令: {user_input}")
                            print("💡 输入 /help 查看可用命令")
                            continue

                    # 发送普通消息
                    print("\n🤖 Assistant: ", end="", flush=True)
                    try:
                        async for chunk in agent.chat(user_input):
                            print(chunk, end="", flush=True)
                        print()
                        print_separator()
                    except Exception as e:
                        print(f"\n❌ 错误: {e}")
                        print("💡 可能需要重新启动程序")

                except KeyboardInterrupt:
                    print("\n\n⏸️  检测到 Ctrl+C，发送中断信号...")
                    try:
                        await agent.interrupt()
                        print("✅ 已中断当前执行")
                        print("💡 输入 /quit 退出，或继续对话")
                    except Exception as e:
                        print(f"⚠️  中断失败: {e}")

                except EOFError:
                    print("\n\n👋 检测到 EOF，退出程序...")
                    break

    except Exception as e:
        print(f"❌ 初始化失败: {e}")
        print("💡 请检查:")
        print("  1. ANTHROPIC_API_KEY 是否在 .env 中配置")
        print("  2. 网络连接是否正常")
        print("  3. Claude Code CLI 是否已安装")


if __name__ == "__main__":
    asyncio.run(main())

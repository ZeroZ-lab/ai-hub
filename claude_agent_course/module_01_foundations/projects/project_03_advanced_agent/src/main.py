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

    # TODO: 1. 创建 Agent 实例
    # agent = AdvancedAgent()
    pass

    # TODO: 2. 建立初始连接
    # print("🔗 正在连接到 Claude...")
    # try:
    #     async for chunk in agent.connect(initial_prompt="你好，我是你的智能助手"):
    #         print(chunk, end="", flush=True)
    #     print()
    #     print_separator()
    # except Exception as e:
    #     print(f"❌ 连接失败: {e}")
    #     return
    pass

    # TODO: 3. 主交互循环
    # while True:
    #     try:
    #         user_input = input("💬 You: ").strip()
    #
    #         if not user_input:
    #             continue
    #
    #         # 处理命令
    #         if user_input.startswith('/'):
    #             command = user_input.lower()
    #
    #             if command == '/quit':
    #                 print("\n🔌 正在断开连接...")
    #                 await agent.disconnect()
    #                 print("👋 再见！")
    #                 break
    #
    #             elif command == '/help':
    #                 print("\n可用命令:")
    #                 print("  <消息>      - 发送消息")
    #                 print("  /interrupt  - 中断执行")
    #                 print("  /session    - 显示会话 ID")
    #                 print("  /quit       - 退出")
    #                 continue
    #
    #             elif command == '/interrupt':
    #                 print("\n⏸️  中断执行...")
    #                 await agent.interrupt()
    #                 print("✅ 已中断")
    #                 continue
    #
    #             elif command == '/session':
    #                 session_id = agent.get_session_id()
    #                 print(f"\n📋 Session ID: {session_id or '未建立'}")
    #                 continue
    #
    #             else:
    #                 print(f"\n❌ 未知命令: {user_input}")
    #                 continue
    #
    #         # 发送普通消息
    #         print("\n🤖 Assistant: ", end="", flush=True)
    #         try:
    #             async for chunk in agent.chat(user_input):
    #                 print(chunk, end="", flush=True)
    #             print()
    #             print_separator()
    #         except Exception as e:
    #             print(f"\n❌ 错误: {e}")
    #
    #     except KeyboardInterrupt:
    #         print("\n\n⏸️  检测到中断信号...")
    #         await agent.interrupt()
    #         print("💡 输入 /quit 退出，或继续对话")
    #
    #     except EOFError:
    #         print("\n\n🔌 断开连接...")
    #         await agent.disconnect()
    #         break
    pass


if __name__ == "__main__":
    # TODO: 4. 运行主函数
    # asyncio.run(main())
    print("⚠️  请先实现 agent.py 中的 TODO 项")

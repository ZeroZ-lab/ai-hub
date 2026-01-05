"""
Bash Automation Solution Entry Point
"""

import asyncio
from solution.agent import BashAutomation

async def main():
    """主函数"""
    print("=" * 60)
    print("💻 Bash Automation - 自动化助手")
    print("=" * 60)
    print("\n命令: git <args>, check, logs <file>, run <cmd>, exit")
    print("=" * 60)

    try:
        async with BashAutomation() as agent:
            print("✅ 已连接到 Claude\n")

            while True:
                try:
                    user_input = input("\n💬 你: ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ['exit', 'quit']:
                        break

                    parts = user_input.split(maxsplit=1)
                    command = parts[0].lower()
                    args = parts[1] if len(parts) > 1 else ""

                    print()
                    if command == "git":
                        print(f"📦 Git: {args}\n")
                        await agent.run_git_command(args)
                    elif command == "check":
                        print("🔍 检查环境...\n")
                        await agent.check_environment()
                    elif command == "logs":
                        if not args:
                            print("请指定日志文件")
                        else:
                            print(f"📋 分析: {args}\n")
                            await agent.analyze_logs(args)
                    elif command == "run":
                        if not args:
                            print("请指定命令")
                        else:
                            print(f"⚡ 执行: {args}\n")
                            await agent.execute_command(args)
                    else:
                        print(f"未知命令: {command}")

                except KeyboardInterrupt:
                    print("\n\n⏸️ 中断...")
                    break

    except Exception as e:
        print(f"❌ 错误: {e}")

    print("\n👋 再见！")


if __name__ == "__main__":
    asyncio.run(main())

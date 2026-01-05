"""
File Analyzer Solution Entry Point
"""

import asyncio
from solution.agent import FileAnalyzer

async def main():
    """主函数"""
    print("=" * 60)
    print("📂 File Analyzer - 文件分析器")
    print("=" * 60)
    print("\n命令: scan, count, report, exit")
    print("=" * 60)

    try:
        async with FileAnalyzer() as agent:
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
                    path = parts[1] if len(parts) > 1 else "."

                    print()
                    if command == "scan":
                        print(f"🔍 扫描: {path}\n")
                        await agent.scan_directory(path)
                    elif command == "count":
                        print(f"📊 统计: {path}\n")
                        await agent.count_lines(path)
                    elif command == "report":
                        print(f"📝 报告: {path}\n")
                        await agent.generate_report(path)
                    else:
                        print(f"未知命令: {command}")

                except KeyboardInterrupt:
                    print("\n\n⏸️ 中断...")
                    break

    except Exception as e:
        print(f"❌ 错误: {e}")
        print("请检查 ANTHROPIC_API_KEY 是否配置")

    print("\n👋 再见！")


if __name__ == "__main__":
    asyncio.run(main())

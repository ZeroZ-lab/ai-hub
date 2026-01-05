"""
File Analyzer - 主程序

使用 Claude Agent SDK 的 Read 和 Bash 工具分析项目文件结构。

Author: Claude Agent Course
Date: 2024-01-04
"""

import asyncio
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# TODO: 导入你实现的 FileAnalyzer
# from agent import FileAnalyzer


async def main():
    """主函数"""
    print("=" * 60)
    print("📂 File Analyzer - 文件分析器")
    print("=" * 60)
    print("\n命令:")
    print("  scan [path]  - 扫描目录结构")
    print("  count [path] - 统计代码行数")
    print("  report [path] - 生成项目报告")
    print("  exit         - 退出程序")
    print("=" * 60)

    # TODO: 初始化你的 FileAnalyzer
    # agent = FileAnalyzer()

    while True:
        try:
            user_input = input("\n💬 你: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 再见！")
                break

            # 解析命令
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            path = parts[1] if len(parts) > 1 else "."

            if command == "scan":
                print(f"\n🔍 扫描目录: {path}")
                # TODO: 调用 agent.scan_directory(path)
                print("⚠️ 请实现 scan_directory 方法")

            elif command == "count":
                print(f"\n📊 统计代码: {path}")
                # TODO: 调用 agent.count_lines(path)
                print("⚠️ 请实现 count_lines 方法")

            elif command == "report":
                print(f"\n📝 生成报告: {path}")
                # TODO: 调用 agent.generate_report(path)
                print("⚠️ 请实现 generate_report 方法")

            else:
                print(f"❓ 未知命令: {command}")
                print("可用命令: scan, count, report, exit")

        except KeyboardInterrupt:
            print("\n\n👋 检测到 Ctrl+C，退出程序")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")


if __name__ == "__main__":
    asyncio.run(main())

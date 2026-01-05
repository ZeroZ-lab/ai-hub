"""
File Analyzer - 参考答案 (简化版)

使用 Claude Agent SDK 的 Read 和 Bash 工具分析项目文件。
注意：此版本移除了 can_use_tool 以简化运行。

Author: Claude Agent Course
"""

import asyncio
import os
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions

load_dotenv()


class FileAnalyzer:
    """文件分析器 - 简化版"""

    def __init__(self):
        # 简化配置，不使用 can_use_tool
        self.options = ClaudeAgentOptions(
            allowed_tools=["Read", "Bash"],
            permission_mode='acceptEdits'
        )

    async def scan_directory(self, path: str = ".") -> str:
        """扫描目录结构"""
        prompt = f"""
        请分析目录 {path} 的结构：
        1. 使用 ls -la {path} 列出所有文件
        2. 按文件类型分类
        3. 返回结构化的文件列表
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
            elif hasattr(message, 'tool_name'):
                print(f"  🔧 {message.tool_name}...")
        
        return "\n".join(result) if result else "无法获取目录信息"

    async def count_lines(self, path: str = ".") -> str:
        """统计代码行数"""
        prompt = f"""
        统计 {path} 目录下的代码行数：
        1. 找出所有代码文件 (.py, .js, .md 等)
        2. 使用 wc -l 统计每个文件
        3. 按语言汇总
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
            elif hasattr(message, 'tool_name'):
                print(f"  🔧 {message.tool_name}...")
        
        return "\n".join(result) if result else "无法统计"

    async def generate_report(self, path: str = ".") -> str:
        """生成项目报告"""
        prompt = f"""
        为 {path} 生成 Markdown 项目报告：
        1. 使用 ls 查看目录结构
        2. 读取 README.md（如有）
        3. 统计代码行数
        4. 生成报告
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
            elif hasattr(message, 'tool_name'):
                print(f"  🔧 {message.tool_name}...")
        
        return "\n".join(result) if result else "无法生成报告"


async def main():
    """主函数"""
    print("=" * 60)
    print("📂 File Analyzer - 文件分析器")
    print("=" * 60)
    print("\n命令: scan, count, report, exit")
    print("=" * 60)

    agent = FileAnalyzer()

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

            if command == "scan":
                print(f"\n🔍 扫描: {path}\n")
                result = await agent.scan_directory(path)
                print(result)
            elif command == "count":
                print(f"\n📊 统计: {path}\n")
                result = await agent.count_lines(path)
                print(result)
            elif command == "report":
                print(f"\n📝 报告: {path}\n")
                result = await agent.generate_report(path)
                print(result)
            else:
                print(f"未知命令: {command}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")

    print("\n👋 再见！")


if __name__ == "__main__":
    asyncio.run(main())

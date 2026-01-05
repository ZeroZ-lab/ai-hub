"""
Bash Automation - 参考答案 (简化版)

使用 Claude Agent SDK 的 Bash 工具自动化开发任务。
注意：此版本移除了 can_use_tool 以简化运行。

Author: Claude Agent Course
"""

import asyncio
import os
from datetime import datetime
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions

load_dotenv()


class BashAutomation:
    """Bash 自动化助手 - 简化版"""

    def __init__(self):
        # 简化配置，不使用 can_use_tool
        self.options = ClaudeAgentOptions(
            allowed_tools=["Bash", "Read"],
            permission_mode='acceptEdits'
        )
        self.command_history = []

    async def run_git_command(self, git_args: str) -> str:
        """执行 Git 命令"""
        prompt = f"""
        执行 Git 命令并解读结果：
        git {git_args}
        
        用中文解释输出，如有需要给出建议。
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
            elif hasattr(message, 'tool_name'):
                print(f"  🔧 执行中...")
        
        return "\n".join(result) if result else "执行失败"

    async def check_environment(self) -> str:
        """检查开发环境"""
        prompt = """
        检查开发环境：
        1. python3 --version
        2. node --version
        3. git --version
        4. docker --version
        
        显示版本或标记为未安装。
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
            elif hasattr(message, 'tool_name'):
                print(f"  🔧 检查中...")
        
        return "\n".join(result) if result else "检查失败"

    async def analyze_logs(self, log_file: str) -> str:
        """分析日志文件"""
        prompt = f"""
        分析日志 {log_file}：
        1. tail -50 {log_file}
        2. 统计错误和警告数量
        3. 给出分析报告
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
            elif hasattr(message, 'tool_name'):
                print(f"  🔧 分析中...")
        
        return "\n".join(result) if result else "分析失败"

    async def execute_command(self, command: str) -> str:
        """执行命令"""
        prompt = f"""
        执行命令并解释结果：
        {command}
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
            elif hasattr(message, 'tool_name'):
                print(f"  🔧 执行中...")
        
        return "\n".join(result) if result else "执行失败"


async def main():
    """主函数"""
    print("=" * 60)
    print("💻 Bash Automation - 自动化助手")
    print("=" * 60)
    print("\n命令: git <args>, check, logs <file>, run <cmd>, exit")
    print("=" * 60)

    agent = BashAutomation()

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

            if command == "git":
                print(f"\n📦 Git: {args}\n")
                result = await agent.run_git_command(args)
                print(result)
            elif command == "check":
                print("\n🔍 检查环境...\n")
                result = await agent.check_environment()
                print(result)
            elif command == "logs":
                if not args:
                    print("请指定日志文件")
                else:
                    print(f"\n📋 分析: {args}\n")
                    result = await agent.analyze_logs(args)
                    print(result)
            elif command == "run":
                if not args:
                    print("请指定命令")
                else:
                    print(f"\n⚡ 执行: {args}\n")
                    result = await agent.execute_command(args)
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

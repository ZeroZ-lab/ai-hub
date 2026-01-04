"""
Hello Agent - 完整参考实现

这是 Hello Agent 项目的完整实现。

Author: Claude Code Course
Date: 2024-01-04
"""

import sys
import os
from pathlib import Path
from typing import Dict, List
from anthropic import Anthropic, APIError
from dotenv import load_dotenv

load_dotenv()


def show_environment():
    """显示环境信息"""
    print("\n📊 环境信息:")
    print(f"  Python 版本: {sys.version.split()[0]}")
    print(f"  当前目录: {os.getcwd()}")
    print()


def get_file_list(directory=".") -> Dict[str, List[str]]:
    """获取目录中的文件列表

    Args:
        directory: 目录路径

    Returns:
        dict: {"files": [...], "directories": [...]}
    """
    files = []
    directories = []

    try:
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)

            # 跳过隐藏文件
            if item.startswith('.') and item not in ['.env.example']:
                continue

            if os.path.isfile(full_path):
                files.append(item)
            elif os.path.isdir(full_path):
                directories.append(item)

        return {"files": sorted(files), "directories": sorted(directories)}

    except PermissionError:
        print(f"❌ 无权限访问目录: {directory}")
        return {"files": [], "directories": []}


def get_file_statistics(directory=".") -> Dict[str, int]:
    """统计文件类型

    Args:
        directory: 目录路径

    Returns:
        dict: 文件扩展名到数量的映射
    """
    stats = {}

    try:
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)

            if item.startswith('.'):
                continue

            if os.path.isfile(full_path):
                ext = Path(item).suffix or "(无扩展名)"
                stats[ext] = stats.get(ext, 0) + 1
            elif os.path.isdir(full_path):
                stats["[目录]"] = stats.get("[目录]", 0) + 1

        return stats

    except PermissionError:
        return {}


class FileAgent:
    """文件查看 Agent"""

    def __init__(self, model: str = "claude-3-5-sonnet-20241022"):
        """初始化 FileAgent"""
        api_key = os.getenv("ANTHROPIC_API_KEY")

        if not api_key:
            raise ValueError(
                "❌ 未找到 ANTHROPIC_API_KEY\n"
                "请检查:\n"
                "1. .env 文件是否存在\n"
                "2. .env 中是否设置了 ANTHROPIC_API_KEY"
            )

        # 支持自定义 base URL（用于代理或其他兼容 API）
        base_url = os.getenv("ANTHROPIC_BASE_URL")

        if base_url:
            self.client = Anthropic(api_key=api_key, base_url=base_url)
            print(f"🔗 使用自定义 API: {base_url}")
        else:
            self.client = Anthropic(api_key=api_key)

        self.model = model

    def describe_files(self, directory=".") -> str:
        """让 Claude 描述目录中的文件

        Args:
            directory: 目录路径

        Returns:
            str: Claude 的自然语言描述
        """
        # 获取文件列表
        file_info = get_file_list(directory)

        # 构建提示词
        prompt = f"""请用简洁友好的语言描述以下目录中的文件：

目录: {os.path.abspath(directory)}

文件:
{chr(10).join(f"- {f}" for f in file_info['files'])}

子目录:
{chr(10).join(f"- {d}/" for d in file_info['directories'])}

请用1-2句话总结这个目录的内容，并简要说明主要文件的可能用途。"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}]
            )

            return response.content[0].text

        except APIError as e:
            return f"❌ API 调用失败: {e}"

    def statistics_report(self, directory=".") -> str:
        """生成文件统计报告

        Args:
            directory: 目录路径

        Returns:
            str: 统计报告
        """
        stats = get_file_statistics(directory)

        if not stats:
            return "目录为空或无法访问"

        # 构建提示词
        stats_text = "\n".join(f"- {ext}: {count} 个" for ext, count in sorted(stats.items()))

        prompt = f"""请分析以下文件统计信息，并给出简要评价：

{stats_text}

请用1-2句话总结这个目录的文件组成特点。"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=256,
                messages=[{"role": "user", "content": prompt}]
            )

            result = f"📊 文件统计:\n{stats_text}\n\n💬 AI 分析:\n{response.content[0].text}"
            return result

        except APIError as e:
            return f"❌ API 调用失败: {e}"


def main():
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
                result = agent.describe_files()
                print(f"\n🤖 Agent:\n{result}")
                continue

            if user_input.lower() in ['stat', 'statistics']:
                print("\n📊 正在统计...")
                result = agent.statistics_report()
                print(f"\n{result}")
                continue

            # 其他输入视为自由对话
            print("\n💡 提示: 使用 'ls' 查看文件，'stat' 查看统计，'help' 查看帮助")

        except KeyboardInterrupt:
            print("\n\n👋 检测到 Ctrl+C，退出程序")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")


if __name__ == "__main__":
    main()

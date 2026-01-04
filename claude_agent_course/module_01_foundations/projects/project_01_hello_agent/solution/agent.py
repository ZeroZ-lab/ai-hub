"""文件查看 Agent 核心实现"""

import os
from pathlib import Path
from typing import Dict, List, AsyncGenerator
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock


def get_file_list(directory=".") -> Dict[str, List[str]]:
    """获取目录中的文件列表"""
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
    """统计文件类型"""
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
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.base_url = os.getenv("ANTHROPIC_BASE_URL")
        
        if not self.api_key:
            raise ValueError(
                "❌ 未找到 ANTHROPIC_API_KEY\n"
                "请检查:\n"
                "1. .env 文件是否存在\n"
                "2. .env 中是否设置了 ANTHROPIC_API_KEY"
            )

        if self.base_url:
            print(f"🔗 使用自定义 API: {self.base_url}")

        self.model = model

    async def _query_claude_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        """调用 Claude Agent SDK 获取流式响应

        Args:
            prompt: 提示词

        Yields:
            str: 响应片段
        """
        env_vars = {}
        if self.api_key:
            env_vars["ANTHROPIC_API_KEY"] = self.api_key
        if self.base_url:
            env_vars["ANTHROPIC_BASE_URL"] = self.base_url
            
        options = ClaudeAgentOptions(
            model=self.model,
            env=env_vars
        )

        try:
            async for message in query(prompt=prompt, options=options):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            yield block.text
        except Exception as e:
            yield f"❌ API 调用失败: {e}"

    async def describe_files(self, directory=".") -> AsyncGenerator[str, None]:
        """让 Claude 描述目录中的文件 (流式)

        Args:
            directory: 目录路径

        Yields:
             Claude 的描述片段
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

        async for chunk in self._query_claude_stream(prompt):
            yield chunk

    async def statistics_report(self, directory=".") -> AsyncGenerator[str, None]:
        """生成文件统计报告 (流式)

        Args:
            directory: 目录路径

        Yields:
            统计报告片段
        """
        stats = get_file_statistics(directory)

        if not stats:
            yield "目录为空或无法访问"
            return

        # 构建提示词
        stats_text = "\n".join(f"- {ext}: {count} 个" for ext, count in sorted(stats.items()))
        
        # 先输出统计信息
        yield f"📊 文件统计:\n{stats_text}\n\n💬 AI 分析:\n"

        prompt = f"""请分析以下文件统计信息，并给出简要评价：

{stats_text}

请用1-2句话总结这个目录的文件组成特点。"""

        # 再流式输出 AI 分析
        async for chunk in self._query_claude_stream(prompt):
            yield chunk

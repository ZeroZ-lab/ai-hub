"""智能助手核心实现"""

import os
from datetime import datetime
from typing import AsyncGenerator, List, Dict
# TODO: 1. 导入 claude_agent_sdk
# from claude_agent_sdk import ...


class SmartAssistant:
    """基于 Claude 的智能助手

    功能：
    - 多轮对话
    - 上下文记忆
    - 系统提示词定制
    - 流式响应
    """

    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str = "claude-3-5-sonnet-20241022"):
        """初始化助手

        Args:
            api_key: Anthropic API 密钥（可选，默认从环境变量读取）
            base_url: Anthropic API 基础 URL（可选，默认从环境变量读取）
            model: 使用的 Claude 模型
        """
        # TODO: 2. 初始化助手状态
        # self.api_key = ...
        # self.base_url = ...
        # self.model = ...
        # self.conversation_history = ...
        # self.session_id = None # 提示：使用 session_id 来维持 SDK 的上下文
        pass

    def _default_system_prompt(self) -> str:
        """默认系统提示词"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""你是一个友好、专业的智能助手。当前时间是 {current_time}。

你的特点：
- 提供准确、有用的信息
- 用清晰、简洁的语言回答
- 必要时询问澄清性问题
- 保持礼貌和专业

如果用户的问题不清楚，请主动询问以获取更多信息。"""

    def set_system_prompt(self, prompt: str) -> None:
        """设置自定义系统提示词

        Args:
            prompt: 系统提示词内容
        """
        # TODO: 实现设置系统提示词
        pass

    async def chat_stream(self, user_message: str) -> AsyncGenerator[str, None]:
        """发送消息并获取流式回复

        Args:
            user_message: 用户消息

        Yields:
            助手回复的片段
        """
        # TODO: 3. 准备 ClaudeAgentOptions
        # 提示：如果 self.session_id 存在，传入 resume=self.session_id
        # 提示：API Key 和 Base URL 需要通过 env 参数传递:
        # env = {}
        # if self.api_key: env["ANTHROPIC_API_KEY"] = self.api_key
        # if self.base_url: env["ANTHROPIC_BASE_URL"] = self.base_url
        # options = ClaudeAgentOptions(..., resume=self.session_id, env=env)
        pass
        
        # TODO: 4. 调用 query 函数获取流式响应
        # 提示：
        # async for message in query(prompt=..., options=...):
        #     if isinstance(message, AssistantMessage):
        #         ...
        #     elif isinstance(message, ResultMessage):
        #         # 获取并保存 session_id
        pass
        
        # TODO: 5. 更新本地历史记录
        # (主要用于 display history, 实际上下文由 session_id 维持)
        pass

    def clear_history(self) -> None:
        """清空对话历史"""
        self.conversation_history = []
        # TODO: 清空 session_id

    def get_history(self) -> List[Dict]:
        """获取对话历史

        Returns:
            对话历史列表
        """
        return self.conversation_history.copy()

    def save_history(self, filepath: str) -> None:
        """保存对话历史到文件

        Args:
            filepath: 保存路径
        """
        import json
        # TODO: 实现保存功能 (记得保存 session_id)
        pass

    def load_history(self, filepath: str) -> None:
        """从文件加载对话历史

        Args:
            filepath: 文件路径
        """
        import json
        # TODO: 实现加载功能 (记得加载 session_id)
        pass

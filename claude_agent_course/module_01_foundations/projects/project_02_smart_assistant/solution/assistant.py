"""智能助手核心实现"""

import os
from datetime import datetime
from typing import AsyncGenerator
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage, TextBlock


class SmartAssistant:
    """基于 Claude 的智能助手

    功能：
    - 多轮对话
    - 上下文记忆 (通过 SDK Session)
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
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.base_url = base_url or os.environ.get("ANTHROPIC_BASE_URL")
        self.model = model
        self.conversation_history: list[dict] = []
        self.system_prompt = self._default_system_prompt()
        self.session_id = None # 记录会话 ID

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
        self.system_prompt = prompt

    async def chat_stream(self, user_message: str) -> AsyncGenerator[str, None]:
        """发送消息并获取流式回复

        Args:
            user_message: 用户消息

        Yields:
            助手回复的片段
        """
        # 准备选项，如果有 session_id 则恢复会话
        # 构建 env 字典
        env_vars = {}
        if self.base_url:
            env_vars["ANTHROPIC_BASE_URL"] = self.base_url
        if self.api_key:
            env_vars["ANTHROPIC_API_KEY"] = self.api_key

        options = ClaudeAgentOptions(
            model=self.model,
            system_prompt=self.system_prompt,
            resume=self.session_id,
            env=env_vars
        )

        # 记录本次完整的回复（用于本地历史记录展示）
        full_response = []

        # 调用 SDK query
        try:
            async for message in query(prompt=user_message, options=options):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            text = block.text
                            full_response.append(text)
                            yield text
                elif isinstance(message, ResultMessage):
                    # 更新 session_id，以便下次继续对话
                    if message.session_id:
                        self.session_id = message.session_id
        except Exception as e:
            # 可以在这里处理错误，例如重置 session_id 或者抛出异常
            raise e
        
        # 更新本地历史记录（仅作展示用途，SDK 内部已维护上下文）
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        self.conversation_history.append({
            "role": "assistant",
            "content": "".join(full_response)
        })

    def clear_history(self) -> None:
        """清空对话历史"""
        self.conversation_history = []
        self.session_id = None # 清空会话 ID，开始新对话

    def get_history(self) -> list[dict]:
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

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                'model': self.model,
                'system_prompt': self.system_prompt,
                'history': self.conversation_history,
                'session_id': self.session_id # 保存 session_id
            }, f, ensure_ascii=False, indent=2)

    def load_history(self, filepath: str) -> None:
        """从文件加载对话历史

        Args:
            filepath: 文件路径
        """
        import json

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.model = data.get('model', self.model)
            self.system_prompt = data.get('system_prompt', self.system_prompt)
            self.conversation_history = data.get('history', [])
            self.session_id = data.get('session_id') # 尝试加载 session_id

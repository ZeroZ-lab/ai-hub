"""高级 Agent 核心实现 - 使用 ClaudeSDKClient"""

import os
from typing import AsyncGenerator, Optional
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, ResultMessage, TextBlock


class AdvancedAgent:
    """使用 ClaudeSDKClient 的高级 Agent

    功能：
    - 有状态的多轮对话
    - 流式响应
    - 中断执行
    - 会话管理
    """

    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str = "claude-3-5-sonnet-20241022"):
        """初始化高级 Agent

        Args:
            api_key: Anthropic API 密钥
            base_url: Anthropic API 基础 URL
            model: 使用的模型
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.base_url = base_url or os.environ.get("ANTHROPIC_BASE_URL")
        self.model = model
        self.client: Optional[ClaudeSDKClient] = None
        self.session_id: Optional[str] = None

    async def __aenter__(self):
        """异步上下文管理器入口"""
        # 创建配置
        env_vars = {}
        if self.api_key:
            env_vars["ANTHROPIC_API_KEY"] = self.api_key
        if self.base_url:
            env_vars["ANTHROPIC_BASE_URL"] = self.base_url

        options = ClaudeAgentOptions(
            model=self.model,
            env=env_vars
        )

        # 使用 ClaudeSDKClient 的上下文管理器
        self.client = ClaudeSDKClient(options=options)
        await self.client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器退出"""
        if self.client:
            await self.client.__aexit__(exc_type, exc_val, exc_tb)
            self.client = None
            self.session_id = None

    async def chat(self, prompt: str) -> AsyncGenerator[str, None]:
        """发送消息并获取流式响应

        Args:
            prompt: 用户消息

        Yields:
            响应片段
        """
        if not self.client:
            raise RuntimeError("请使用 async with AdvancedAgent() as agent 创建实例")

        # 发送查询
        await self.client.query(prompt=prompt)

        # 接收响应
        async for message in self.client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text
            elif isinstance(message, ResultMessage):
                if message.session_id:
                    self.session_id = message.session_id

    async def interrupt(self) -> None:
        """中断当前执行"""
        if self.client:
            await self.client.interrupt()

    def get_session_id(self) -> Optional[str]:
        """获取当前会话 ID

        Returns:
            会话 ID
        """
        return self.session_id

"""Conversational Agent - 支持会话管理的 Agent [完整解决方案]"""

import os
from typing import Optional
from anthropic import Anthropic
from .session import SessionManager


class ConversationalAgent:
    """支持会话持久化的对话 Agent"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        初始化 Agent
        
        Args:
            api_key: Anthropic API key（如果不提供则从环境变量读取）
        """
        # 初始化 Anthropic client
        self.client = Anthropic(api_key=api_key or os.getenv('ANTHROPIC_API_KEY'))
        
        # 初始化 SessionManager
        storage_dir = os.getenv('SESSION_STORAGE_DIR', './data/sessions')
        self.session_manager = SessionManager(storage_dir=storage_dir)
        
        # 当前活动会话
        self.current_session = None
    
    def start_new_conversation(self, user_id: str = "default") -> str:
        """
        开始新对话
        
        Args:
            user_id: 用户ID
            
        Returns:
            session_id: 新会话的ID
        """
        # 创建新会话
        self.current_session = self.session_manager.create_session(user_id)
        
        print(f"✨ 创建新会话: {self.current_session}")
        
        return self.current_session
    
    def resume_conversation(self, session_id: str):
        """
        恢复之前的对话
        
        Args:
            session_id: 要恢复的会话ID
        """
        # 验证会话存在
        session_data = self.session_manager.load_session(session_id)
        
        # 设置为当前会话
        self.current_session = session_id
        
        # 显示历史信息
        message_count = len(session_data["messages"])
        print(f"🔄 恢复会话: {session_id}")
        print(f"📜 历史记录: {message_count} 条消息")
    
    def chat(self, user_message: str) -> str:
        """
        发送消息并获取回复
        
        Args:
            user_message: 用户消息
            
        Returns:
            assistant_message: AI 的回复
            
        Raises:
            ValueError: 如果没有活动会话
        """
        if not self.current_session:
            raise ValueError("没有活动会话，请先创建或恢复会话")
        
        # 保存用户消息
        self.session_manager.add_message(
            self.current_session,
            "user",
            user_message
        )
        
        # 获取历史消息
        history = self.session_manager.get_messages(self.current_session)
        
        # 转换为 Claude API 格式
        messages = self._format_messages(history)
        
        # 调用 Claude API
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=messages
        )
        
        # 提取响应文本
        assistant_message = response.content[0].text
        
        # 保存 AI 响应
        self.session_manager.add_message(
            self.current_session,
            "assistant",
            assistant_message
        )
        
        return assistant_message
    
    def _format_messages(self, messages: list) -> list:
        """
        将会话消息转换为 Claude API 格式
        
        Args:
            messages: 会话消息列表
            
        Returns:
            formatted_messages: Claude API 格式的消息
        """
        # 移除 timestamp 字段，只保留 role 和 content
        return [
            {"role": msg["role"], "content": msg["content"]}
            for msg in messages
        ]

"""Conversational Agent - 支持会话管理的 Agent"""

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
        # TODO: 实现初始化逻辑
        # 1. 创建 Anthropic client
        # 2. 创建 SessionManager 实例
        # 3. 初始化 current_session 为 None
        pass
    
    def start_new_conversation(self, user_id: str = "default") -> str:
        """
        开始新对话
        
        Args:
            user_id: 用户ID
            
        Returns:
            session_id: 新会话的ID
        """
        # TODO: 实现新对话创建
        # 1. 调用 SessionManager 创建新会话
        # 2. 设置 current_session
        # 3. 打印提示信息
        # 4. 返回 session_id
        pass
    
    def resume_conversation(self, session_id: str):
        """
        恢复之前的对话
        
        Args:
            session_id: 要恢复的会话ID
        """
        # TODO: 实现会话恢复
        # 1. 验证会话是否存在（调用 load_session）
        # 2. 设置 current_session
        # 3. 打印历史记录信息
        pass
    
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
        # TODO: 实现对话功能
        # 1. 检查是否有活动会话
        # 2. 保存用户消息到会话
        # 3. 获取历史消息
        # 4. 构建 messages 列表（Claude API 格式）
        # 5. 调用 Claude API
        # 6. 保存 AI 响应到会话
        # 7. 返回响应文本
        pass
    
    def _format_messages(self, messages: list) -> list:
        """
        将会话消息转换为 Claude API 格式
        
        Args:
            messages: 会话消息列表
            
        Returns:
            formatted_message: Claude API 格式的消息
        """
        # TODO: 实现消息格式转换
        # 将 {'role': '...', 'content': '...', 'timestamp': '...'}
        # 转换为 {'role': '...', 'content': '...'}
        pass

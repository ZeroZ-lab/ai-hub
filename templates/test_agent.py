"""
单元测试

测试 Agent 的核心功能。

Usage:
    pytest tests/test_agent.py

Author: Your Name
Date: 2024-01-01
"""

import pytest
from unittest.mock import Mock, patch
from src.agent import MyAgent


class TestMyAgent:
    """MyAgent 类的单元测试"""

    def test_init(self):
        """测试初始化"""
        # TODO: 实现测试
        pass

    def test_chat(self):
        """测试聊天功能"""
        # TODO: 使用 Mock 测试 API 调用
        pass

    def test_reset(self):
        """测试重置对话历史"""
        # TODO: 实现测试
        pass

    # 添加更多测试用例...


# 示例：Mock API 调用的测试
@patch('src.agent.Anthropic')
def test_chat_with_mock(mock_anthropic):
    """使用 Mock 测试聊天功能"""
    # 设置 Mock 响应
    mock_response = Mock()
    mock_response.content = [Mock(text="Hello!")]
    mock_anthropic.return_value.messages.create.return_value = mock_response

    # 测试
    # agent = MyAgent(api_key="test-key")
    # result = agent.chat("Hi")
    # assert result == "Hello!"

    # TODO: 取消注释并完善测试
    pass

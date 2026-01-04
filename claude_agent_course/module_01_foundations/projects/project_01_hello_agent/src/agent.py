"""
File Agent - 文件查看 Agent

这个模块包含 FileAgent 类，负责文件系统操作和 AI 交互。

Author: Your Name
Date: 2024-01-04
"""

import os
from typing import Dict, List
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


def get_file_list(directory="."):
    """获取目录中的文件列表

    Args:
        directory: 目录路径，默认当前目录

    Returns:
        dict: {"files": [...], "directories": [...]}
    """
    # TODO: 实现文件列表获取
    pass


class FileAgent:
    """文件查看 Agent

    Attributes:
        client: Anthropic API 客户端
        model: 使用的模型名称
    """

    def __init__(self, model: str = "claude-3-5-sonnet-20241022"):
        """初始化 FileAgent

        Args:
            model: Claude 模型名称
        """
        # TODO: 1. 从环境变量获取 API Key
        api_key = os.getenv("ANTHROPIC_API_KEY")

        # TODO: 2. 检查 API Key 是否存在
        if not api_key:
            raise ValueError("请在 .env 文件中设置 ANTHROPIC_API_KEY")

        # TODO: 3. 创建 Anthropic 客户端
        # 提示：支持自定义 base_url，从环境变量 ANTHROPIC_BASE_URL 读取
        base_url = os.getenv("ANTHROPIC_BASE_URL")  # 可选配置
        if base_url:
            self.client = Anthropic(api_key=api_key, base_url=base_url)
        else:
            self.client = Anthropic(api_key=api_key)

        # TODO: 4. 设置模型名称
        self.model = model

    def describe_files(self, directory="."):
        """让 Claude 描述目录中的文件

        Args:
            directory: 目录路径

        Returns:
            str: Claude 的描述
        """
        # TODO: 1. 获取文件列表
        # TODO: 2. 构建提示词
        # TODO: 3. 调用 Claude API
        # TODO: 4. 返回结果
        pass

    def file_statistics(self, directory="."):
        """统计文件类型"""
        # TODO: 实现文件统计
        pass

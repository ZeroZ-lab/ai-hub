"""
项目主程序入口

这是项目的主要运行文件。

Usage:
    python src/main.py

Author: Your Name
Date: 2024-01-01
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# 加载环境变量
load_dotenv()


def main():
    """主函数"""
    # 检查 API Key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "请设置 ANTHROPIC_API_KEY 环境变量\n"
            "1. 复制 .env.example 为 .env\n"
            "2. 在 .env 中填入你的 API Key"
        )

    # TODO: 在这里实现你的 Agent 逻辑
    print("Hello, Claude Agent!")

    # 示例：简单的 API 调用
    client = Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Say hello!"}
        ]
    )

    print(f"Claude: {response.content[0].text}")


if __name__ == "__main__":
    main()

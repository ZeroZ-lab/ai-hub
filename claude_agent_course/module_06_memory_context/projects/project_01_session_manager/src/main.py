"""CLI - 命令行界面"""

import os
import sys
import argparse
from dotenv import load_dotenv
from .agent import ConversationalAgent


def main():
    """主函数 - 处理命令行参数"""
    # 加载环境变量
    load_dotenv()
    
    # TODO: 实现命令行解析
    # 1. 创建 ArgumentParser
    # 2. 添加子命令: new, resume, list
    # 3. 解析参数
    
    parser = argparse.ArgumentParser(
        description="Session Manager - 会话管理器"
    )
    parser.add_argument(
        'command',
        choices=['new', 'resume', 'list'],
        help='命令: new (新建会话), resume (恢复会话), list (列出所有会话)'
    )
    parser.add_argument(
        'session_id',
        nargs='?',
        help='会话ID (用于 resume 命令)'
    )
    
    args = parser.parse_args()
    
    # 创建 Agent
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ 错误: 请在 .env 文件中设置 ANTHROPIC_API_KEY")
        sys.exit(1)
    
    agent = ConversationalAgent(api_key=api_key)
    
    # TODO: 根据命令执行相应操作
    if args.command == 'new':
        # 创建新会话
        pass
    
    elif args.command == 'resume':
        # 恢复会话
        pass
    
    elif args.command == 'list':
        # 列出所有会话
        pass


def chat_loop(agent: ConversationalAgent):
    """
    对话循环
    
    Args:
        agent: ConversationalAgent 实例
    """
    # TODO: 实现对话循环
    # 1. 显示提示符
    # 2. 读取用户输入
    # 3. 如果输入 'exit' 或 'quit' 则退出
    # 4. 调用 agent.chat() 获取回复
    # 5. 打印回复
    # 6. 重复
    pass


if __name__ == "__main__":
    main()

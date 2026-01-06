"""CLI - 命令行界面 [完整解决方案]"""

import os
import sys
import argparse
from dotenv import load_dotenv
from .agent import ConversationalAgent
from .session import SessionManager


def main():
    """主函数 - 处理命令行参数"""
    # 加载环境变量
    load_dotenv()
    
    # 命令行解析
    parser = argparse.ArgumentParser(
        description="Session Manager - 会话管理器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python -m solution.main new              # 创建新会话
  python -m solution.main resume sess_xxx  # 恢复会话
  python -m solution.main list             # 列出所有会话
        """
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
    
    # 检查 API Key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ 错误: 请在 .env 文件中设置 ANTHROPIC_API_KEY")
        print("提示: 复制 .env.example 为 .env 并填入你的 API key")
        sys.exit(1)
    
    # 创建 Agent
    agent = ConversationalAgent(api_key=api_key)
    
    # 执行命令
    if args.command == 'new':
        # 创建新会话并开始对话
        agent.start_new_conversation()
        chat_loop(agent)
    
    elif args.command == 'resume':
        # 恢复会话
        if not args.session_id:
            print("❌ 错误: resume 命令需要提供 session_id")
            print("用法: python -m solution.main resume <session_id>")
            sys.exit(1)
        
        try:
            agent.resume_conversation(args.session_id)
            chat_loop(agent)
        except ValueError as e:
            print(f"❌ 错误: {e}")
            sys.exit(1)
    
    elif args.command == 'list':
        # 列出所有会话
        list_sessions()


def chat_loop(agent: ConversationalAgent):
    """
    对话循环
    
    Args:
        agent: ConversationalAgent 实例
    """
    print("\n💬 开始对话（输入 'exit' 或 'quit' 退出）\n")
    
    while True:
        try:
            # 读取用户输入
            user_input = input("> ").strip()
            
            # 检查退出命令
            if user_input.lower() in ['exit', 'quit', 'q']:
                print(f"\n💾 会话已保存: {agent.current_session}")
                print("👋 再见！")
                break
            
            # 跳过空输入
            if not user_input:
                continue
            
            # 获取 AI 响应
            response = agent.chat(user_input)
            
            # 打印响应
            print(f"\n[Assistant]: {response}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n💾 会话已保存: {agent.current_session}")
            print("👋 再见！")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}\n")


def list_sessions():
    """列出所有会话"""
    storage_dir = os.getenv('SESSION_STORAGE_DIR', './data/sessions')
    session_manager = SessionManager(storage_dir=storage_dir)
    
    sessions = session_manager.list_sessions()
    
    if not sessions:
        print("📭 还没有任何会话")
        print("提示: 运行 'python -m solution.main new' 创建新会话")
        return
    
    print(f"\n📋 共有 {len(sessions)} 个会话:\n")
    
    for i, session in enumerate(sessions, 1):
        print(f"{i}. {session['session_id']}")
        print(f"   创建时间: {session['created_at'][:19].replace('T', ' ')}")
        print(f"   消息数量: {session['message_count']} 条")
        print(f"   最后更新: {session['updated_at'][:19].replace('T', ' ')}")
        print()


if __name__ == "__main__":
    main()

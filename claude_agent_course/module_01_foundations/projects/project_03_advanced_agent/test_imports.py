"""测试脚本 - 验证 ClaudeSDKClient 导入"""

import sys
print(f"Python: {sys.version}")

try:
    from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
    print("✅ ClaudeSDKClient 导入成功")

    from claude_agent_sdk import AssistantMessage, ResultMessage, TextBlock
    print("✅ 消息类型导入成功")

    print("\n📚 ClaudeSDKClient 可用方法:")
    for attr in dir(ClaudeSDKClient):
        if not attr.startswith('_'):
            print(f"  - {attr}")

except ImportError as e:
    print(f"❌ 导入失败: {e}")

# Project 03 - 高级 Agent

## 项目简介

本项目演示如何使用 **ClaudeSDKClient** 实现更高级的 Agent 功能，包括：

- ✅ 有状态的多轮对话
- ✅ 流式响应
- ✅ 中断正在执行的任务
- ✅ 回滚文件更改
- ✅ 会话管理

## 学习目标

1. 理解 `ClaudeSDKClient` 与简单 `query()` 函数的区别
2. 掌握客户端的生命周期管理（connect, disconnect）
3. 学习如何处理流式消息（receive_messages, receive_response）
4. 了解中断和回滚机制

## 核心概念

### ClaudeSDKClient vs query()

| 特性 | `query()` | `ClaudeSDKClient` |
|------|-----------|-------------------|
| 使用场景 | 简单一次性查询 | 复杂多轮对话 |
| 状态管理 | 需要手动传递 session_id | 自动管理会话状态 |
| 中断功能 | ❌ | ✅ |
| 回滚功能 | ❌ | ✅ |
| 生命周期 | 自动 | 需要手动 connect/disconnect |

### 关键方法

```python
# 1. 初始化客户端
client = ClaudeSDKClient(options=ClaudeAgentOptions(...))

# 2. 建立连接
await client.connect(prompt="初始提示")

# 3. 接收消息（流式）
async for message in client.receive_response():
    if isinstance(message, AssistantMessage):
        # 处理助手消息
        pass

# 4. 发送新查询
await client.query(prompt="下一个问题", session_id=session_id)

# 5. 中断执行
await client.interrupt()

# 6. 回滚文件
await client.rewind_files(user_message_uuid="...")

# 7. 关闭连接
await client.disconnect()
```

## 项目结构

```
project_03_advanced_agent/
├── src/
│   ├── __init__.py
│   ├── agent.py         # AdvancedAgent 类（使用 ClaudeSDKClient）
│   └── main.py          # 交互式 CLI
├── solution/
│   ├── __init__.py
│   ├── agent.py         # 完整实现
│   └── main.py          # 完整实现
├── pyproject.toml
└── README.md
```

## 安装依赖

```bash
# 使用 uv
uv sync

# 或使用 pip
pip install -e .
```

## 使用方法

### 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的 API Key
# ANTHROPIC_API_KEY=your_api_key_here
```

### 运行程序

```bash
# 方法 1：使用 PYTHONPATH（推荐）
PYTHONPATH=solution uv run python solution/main.py

# 方法 2：进入 solution 目录运行
cd solution
PYTHONPATH=. uv run python main.py

# 运行学生版本（src 目录）
PYTHONPATH=src uv run python src/main.py
```

### 可用命令

- `chat <message>` - 发送消息并获取流式回复
- `/interrupt` - 中断当前执行
- `/history` - 查看对话历史（通过 session 维护）
- `/disconnect` - 断开连接并退出
- `/help` - 显示帮助

## 实现提示

### 1. 初始化客户端

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

env_vars = {}
if api_key:
    env_vars["ANTHROPIC_API_KEY"] = api_key

options = ClaudeAgentOptions(
    model="claude-3-5-sonnet-20241022",
    env=env_vars
)

client = ClaudeSDKClient(options=options)
```

### 2. 连接并发送初始消息

```python
await client.connect(prompt="你好，我是智能助手")
```

### 3. 接收流式响应

```python
async for message in client.receive_response():
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock):
                print(block.text, end="", flush=True)
    elif isinstance(message, ResultMessage):
        session_id = message.session_id
        # 保存 session_id 供后续使用
```

### 4. 发送后续查询

```python
await client.query(prompt="下一个问题", session_id=session_id)
async for message in client.receive_response():
    # 处理响应...
```

## 扩展挑战

1. **添加工具调用监控**：显示 Agent 调用了哪些工具
2. **实现会话保存/加载**：将 session_id 保存到文件
3. **添加超时机制**：长时间无响应时自动中断
4. **实现思维链可视化**：展示 Agent 的思考过程（ThinkingBlock）

## 参考资源

- [Claude Agent SDK 文档](https://platform.claude.com/docs/agent-sdk)
- [ClaudeSDKClient API 参考](https://platform.claude.com/docs/agent-sdk/python)

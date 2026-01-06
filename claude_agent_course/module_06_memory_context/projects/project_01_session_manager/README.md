# Project 1: Session Manager - 会话管理器

> 学习如何实现持久化的对话会话管理

## 📚 项目简介

本项目实现一个完整的 Session 管理系统，支持：
- ✅ 创建和管理多个会话
- ✅ 持久化对话历史
- ✅ 恢复之前的对话
- ✅ 会话元数据管理

## 🎯 学习目标

完成本项目后，你将学会：
1. 设计会话数据结构
2. 实现会话持久化（JSON 存储）
3. 管理多轮对话历史
4. 实现会话的创建、保存、加载和列表功能

## 📋 功能需求

### 核心功能

1. **会话创建**
   ```bash
   $ python -m src.main new
   ✨ 创建新会话: sess_abc12345
   ```

2. **发送消息**
   ```bash
   > 你好，我想学习 Agent 开发
   [Assistant]: 很高兴帮助您！Agent 是...
   ```

3. **会话恢复**
   ```bash
   $ python -m src.main resume sess_abc12345
   🔄 恢复会话: sess_abc12345
   📜 历史记录: 5 条消息
   ```

4. **列出所有会话**
   ```bash
   $ python -m src.main list
   📋 所有会话:
   1. sess_abc12345 (5 条消息) - 2024-01-06 10:00
   2. sess_def67890 (3 条消息) - 2024-01-06 09:30
   ```

## 📁 项目结构

```
project_01_session_manager/
├── README.md                 # 本文件
├── pyproject.toml           # 项目配置和依赖
├── .env.example             # 环境变量示例
├── src/
│   ├── __init__.py
│   ├── session.py           # Session 管理核心逻辑
│   ├── agent.py             # 带会话支持的 Agent
│   └── main.py              # CLI 入口
├── solution/                # 完整解决方案
│   ├── __init__.py
│   ├── session.py
│   ├── agent.py
│   └── main.py
└── data/                    # 会话数据存储目录
    └── sessions/            # 各个会话的 JSON 文件
```

## 🚀 快速开始

### 1. 安装依赖

```bash
cd module_06_memory_context/projects/project_01_session_manager
pip install -e .
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 填入你的 ANTHROPIC_API_KEY
```

### 3. 运行项目

```bash
# 创建新会话
python -m src.main new

# 恢复会话
python -m src.main resume sess_abc12345

# 列出所有会话
python -m src.main list
```

## 📝 实现任务

### Task 1: Session 数据结构设计

在 `src/session.py` 中实现 `SessionManager` 类：

```python
class SessionManager:
    """会话管理器"""
    
    def __init__(self, storage_dir: str = "./data/sessions"):
        """初始化，指定存储目录"""
        pass
    
    def create_session(self, user_id: str = "default") -> str:
        """创建新会话，返回 session_id"""
        pass
    
    def add_message(self, session_id: str, role: str, content: str):
        """添加消息到会话"""
        pass
    
    def load_session(self, session_id: str) -> Dict:
        """加载会话数据"""
        pass
    
    def get_messages(self, session_id: str) -> List[Dict]:
        """获取会话的所有消息"""
        pass
    
    def list_sessions(self) -> List[Dict]:
        """列出所有会话及其元数据"""
        pass
```

**提示**：
- 使用 `uuid` 生成唯一 session_id
- 用 `json` 模块保存/加载会话数据
- 会话数据应包含：session_id, created_at, updated_at, messages

### Task 2: Agent 集成

在 `src/agent.py` 中实现 `ConversationalAgent`：

```python
from claude_agent_sdk import Agent
from .session import SessionManager

class ConversationalAgent:
    """支持会话管理的 Agent"""
    
    def __init__(self, api_key: str):
        """初始化 Agent 和 SessionManager"""
        pass
    
    def start_new_conversation(self, user_id: str = "default") -> str:
        """开始新对话"""
        pass
    
    def resume_conversation(self, session_id: str):
        """恢复之前的对话"""
        pass
    
    def chat(self, user_message: str) -> str:
        """发送消息并获取回复（自动保存到会话）"""
        pass
```

**提示**：
- 每次 chat 时，传入完整的历史消息给 Agent
- 保存用户消息和 AI 响应到 session

### Task 3: CLI 界面

在 `src/main.py` 中实现命令行界面：

```python
import argparse
from .agent import ConversationalAgent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['new', 'resume', 'list'])
    parser.add_argument('session_id', nargs='?', help='Session ID (for resume)')
    args = parser.parse_args()
    
    # 实现各个命令
    # ...
```

**命令**：
- `new`: 创建新会话并进入对话循环
- `resume <session_id>`: 恢复指定会话
- `list`: 列出所有会话

## 🧪 测试场景

### 场景 1：创建新会话并对话

```bash
$ python -m src.main new
✨ 创建新会话: sess_a1b2c3d4

> 你好
[Assistant]: 你好！有什么我可以帮助你的吗？

> 我叫 Alice
[Assistant]: 很高兴认识你，Alice！

> exit
💾 会话已保存: sess_a1b2c3d4
```

### 场景 2：恢复会话

```bash
$ python -m src.main resume sess_a1b2c3d4
🔄 恢复会话: sess_a1b2c3d4
📜 历史记录: 4 条消息

> 我叫什么名字？
[Assistant]: 你叫 Alice！

> exit
```

### 场景 3：列出所有会话

```bash
$ python -m src.main list
📋 所有会话:
  1. sess_a1b2c3d4
     创建时间: 2024-01-06 10:15:30
     消息数量: 6 条
     最后更新: 2024-01-06 10:20:45
  
  2. sess_e5f6g7h8
     创建时间: 2024-01-06 09:30:20
     消息数量: 3 条
     最后更新: 2024-01-06 09:35:10
```

## 💡 扩展挑战

完成基础功能后，尝试以下扩展：

1. **会话搜索**
   - 根据关键词搜索会话内容
   - 按日期筛选会话

2. **会话导出**
   - 导出会话为 Markdown 格式
   - 支持分享会话链接

3. **会话统计**
   - 计算每个会话的 token 使用量
   - 统计平均对话轮次

4. **会话清理**
   - 自动删除 N 天前的旧会话
   - 会话归档功能

## 📚 相关文档

- [01_概念讲解.md](../../docs/01_概念讲解.md) - Session 管理原理
- [02_代码示例.md](../../docs/02_代码示例.md) - SessionManager 实现示例
- [Claude Agent SDK 文档](https://docs.anthropic.com/agent-sdk)

## ❓ 常见问题

### Q1: 如何处理会话 ID 冲突？
A: 使用 UUID 生成全局唯一 ID，冲突概率极低。

### Q2: 会话文件太多怎么办？
A: 可以按日期分目录存储，如 `data/sessions/2024-01-06/sess_xxx.json`

### Q3: 如何优化大会话的加载速度？
A: 可以只加载最近 N 条消息，或使用数据库代替 JSON 文件。

---

**开始实现吧！🚀**

如果遇到困难，可以参考 `solution/` 目录中的完整解决方案。

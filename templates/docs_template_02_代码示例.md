# [模块编号] - 代码示例

> 本文档提供可运行的代码示例，帮助你快速上手。

## 最小可运行示例

### 环境准备
```bash
# 1. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. 安装依赖
pip install anthropic python-dotenv

# 3. 配置 API Key
cp .env.example .env
# 编辑 .env，填入你的 ANTHROPIC_API_KEY
```

### Hello World 示例
```python
"""
最简示例：[一句话描述这个示例的作用]
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def hello_agent():
    """最简单的 Agent 示例"""
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Say hello!"}
        ]
    )

    print(response.content[0].text)

if __name__ == "__main__":
    hello_agent()
```

**运行结果**：
```
Hello! How can I assist you today?
```

---

## 完整功能示例

### 示例 1：[功能描述]

```python
"""
完整示例：[详细描述]

这个示例展示了：
1. [要点 1]
2. [要点 2]
3. [要点 3]
"""

import os
from typing import List, Dict
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class ExampleAgent:
    """示例 Agent 类

    Attributes:
        client: Anthropic 客户端
        model: 使用的模型名称
        conversation_history: 对话历史
    """

    def __init__(self, model: str = "claude-3-5-sonnet-20241022"):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = model
        self.conversation_history: List[Dict] = []

    def chat(self, user_message: str) -> str:
        """发送消息并获取响应

        Args:
            user_message: 用户输入

        Returns:
            Agent 的回复
        """
        # 添加用户消息到历史
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # 调用 API
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=self.conversation_history
        )

        # 提取回复
        assistant_message = response.content[0].text

        # 添加助手回复到历史
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    def reset(self):
        """重置对话历史"""
        self.conversation_history = []


def main():
    """主函数"""
    agent = ExampleAgent()

    # 示例对话
    print("Agent: 你好！我是你的 AI 助手。")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ['exit', 'quit', '退出']:
            print("Agent: 再见！")
            break

        if not user_input:
            continue

        response = agent.chat(user_input)
        print(f"Agent: {response}")


if __name__ == "__main__":
    main()
```

**使用方法**：
```bash
python example.py
```

---

## 常见用法对比

### ✅ 好的实践 vs ❌ 不好的实践

#### 1. 错误处理

❌ **不好的做法**：
```python
# 没有错误处理，API 失败时程序崩溃
response = client.messages.create(...)
```

✅ **好的做法**：
```python
try:
    response = client.messages.create(...)
except Exception as e:
    print(f"API 调用失败: {e}")
    # 实现重试逻辑或降级方案
```

#### 2. API Key 管理

❌ **不好的做法**：
```python
# 硬编码 API Key - 危险！
client = Anthropic(api_key="sk-ant-xxx")
```

✅ **好的做法**：
```python
# 使用环境变量
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
```

#### 3. [其他对比点]

---

## API 参考快查

### 核心方法

#### `client.messages.create()`
```python
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",  # 必需：模型名称
    max_tokens=1024,                      # 必需：最大生成 token 数
    messages=[...],                       # 必需：对话历史
    temperature=1.0,                      # 可选：创造性 (0-1)
    system="You are a helpful assistant", # 可选：系统提示
    tools=[...],                          # 可选：工具定义
)
```

**常用参数说明**：
- `model`: 模型选择
  - `claude-3-5-sonnet-20241022` - 平衡性能和成本
  - `claude-3-opus-20240229` - 最强性能
  - `claude-3-haiku-20240307` - 最快速度
- `max_tokens`: 控制输出长度 (建议 1024-4096)
- `temperature`: 创造性控制 (0=精确, 1=创造)

### 响应结构
```python
response = {
    "id": "msg_xxx",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "text",
            "text": "实际回复内容"
        }
    ],
    "model": "claude-3-5-sonnet-20241022",
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 10,
        "output_tokens": 20
    }
}
```

---

## 调试技巧

### 1. 打印中间结果
```python
# 查看发送给 API 的内容
print("发送消息:", messages)

response = client.messages.create(...)

# 查看完整响应
print("完整响应:", response)
```

### 2. 使用日志
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug(f"调用 API，参数: {params}")
```

### 3. Token 使用监控
```python
total_tokens = response.usage.input_tokens + response.usage.output_tokens
print(f"本次调用使用了 {total_tokens} tokens")
```

---

## 常见问题 (FAQ)

### Q1: API Key 报错怎么办？
**A**: 检查以下几点：
1. `.env` 文件是否存在
2. `ANTHROPIC_API_KEY` 是否正确
3. 是否调用了 `load_dotenv()`

### Q2: 如何限制响应长度？
**A**: 使用 `max_tokens` 参数：
```python
response = client.messages.create(
    max_tokens=512,  # 限制为 512 tokens
    ...
)
```

### Q3: [其他常见问题]

---

## 下一步

✅ 掌握了代码示例后：
- 阅读 [03_最佳实践.md] - 学习生产环境注意事项
- 完成 `projects/` 中的实战项目

💡 **提示**：建议先完整运行一遍示例代码，再尝试修改参数观察效果。

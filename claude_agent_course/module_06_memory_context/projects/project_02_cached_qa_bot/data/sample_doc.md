# Claude Agent SDK 完整文档

## 简介

Claude Agent SDK 是 Anthropic 提供的官方 Python SDK，用于构建基于 Claude 的 AI Agent。

## 核心概念

### 1. Messages API

Claude 使用 Messages API 进行对话：

```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)
```

### 2. Tool Use (Function Calling)

Claude 可以调用外部工具：

```python
tools = [
    {
        "name": "get_weather",
        "description": "获取指定城市的天气",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            }
        }
    }
]

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[...]
)
```

### 3. Prompt Caching

缓存大型上下文以节省成本：

```python
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Large document content...",
                    "cache_control": {"type": "ephemeral"}
                }
            ]
        }
    ]
)
```

## 最佳实践

### Token 管理

- 输入限制: 200K tokens (Claude 3.5 Sonnet)
- 输出限制: 4K tokens
- 监控 token 使用避免超限

### 错误处理

```python
try:
    response = client.messages.create(...)
except anthropic.RateLimitError:
    # 处理速率限制
    pass
except anthropic.APIError as e:
    # 处理其他 API 错误
    pass
```

### 成本优化

1. 使用 Prompt Caching 缓存固定内容
2. 压缩长对话历史
3. 选择合适的模型

## 模型选择

| 模型 | 上下文窗口 | 适用场景 |
|------|----------|---------|
| Claude 3.5 Sonnet | 200K | 复杂推理、代码生成 |
| Claude 3 Haiku | 200K | 快速响应、简单任务 |
| Claude 3 Opus | 200K | 最高能力、关键任务 |

## 高级特性

### Streaming

```python
with client.messages.stream(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[...]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### Vision

```python
import base64

with open("image.jpg", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data
                    }
                },
                {
                    "type": "text",
                    "text": "What's in this image?"
                }
            ]
        }
    ]
)
```

## 安全与合规

1. **API Key 安全**: 使用环境变量存储
2. **数据隐私**: 理解数据保留政策
3. **内容过滤**: 遵守使用政策

## 参考资源

- [Official Documentation](https://docs.anthropic.com/)
- [API Reference](https://docs.anthropic.com/api)
- [Python SDK](https://github.com/anthropics/anthropic-sdk-python)

---

*本文档为示例知识库，用于演示 Prompt Caching 功能。*

# [模块编号] - 最佳实践

> 本文档汇总了实际开发中的经验教训，帮助你避免常见陷阱，写出高质量的 Agent 代码。

## 常见陷阱和错误

### 陷阱 1：[陷阱名称]

**问题描述**：
[详细说明这个陷阱是什么，为什么容易犯错]

**错误示例**：
```python
# ❌ 错误的做法
def bad_example():
    # 展示错误代码
    pass
```

**为什么有问题**：
1. [问题 1]
2. [问题 2]
3. [可能导致的后果]

**正确做法**：
```python
# ✅ 正确的做法
def good_example():
    # 展示正确代码
    pass
```

**关键要点**：
- 💡 [要点 1]
- 💡 [要点 2]

---

### 陷阱 2：忽略错误处理

**问题描述**：
很多初学者直接调用 API 而不处理可能的异常，导致程序在网络问题或 API 限流时崩溃。

**错误示例**：
```python
# ❌ 没有错误处理
def chat(message):
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": message}]
    )
    return response.content[0].text
```

**正确做法**：
```python
# ✅ 完善的错误处理
import time
from anthropic import APIError, RateLimitError

def chat_with_retry(message, max_retries=3):
    """带重试机制的聊天函数"""
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": message}]
            )
            return response.content[0].text

        except RateLimitError as e:
            # 遇到限流，等待后重试
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 指数退避
                print(f"遇到限流，等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                raise

        except APIError as e:
            # 其他 API 错误
            print(f"API 错误: {e}")
            raise

        except Exception as e:
            # 未知错误
            print(f"未知错误: {e}")
            raise
```

---

### 陷阱 3：[添加更多陷阱]

---

## 性能优化建议

### 1. 减少 Token 消耗

#### 问题
Token 使用直接影响 API 成本，不必要的冗长提示会增加开销。

#### 优化策略

✅ **精简 System Prompt**：
```python
# ❌ 冗长的提示
system_prompt = """
You are a helpful assistant. You should always be polite and friendly.
When answering questions, please provide detailed explanations...
[很长的描述]
"""

# ✅ 简洁的提示
system_prompt = "你是一个专业的编程助手，提供准确的技术建议。"
```

✅ **使用 max_tokens 限制输出**：
```python
response = client.messages.create(
    max_tokens=512,  # 根据实际需求设置合理上限
    ...
)
```

✅ **清理对话历史**：
```python
# 保留最近 N 轮对话
MAX_HISTORY_LENGTH = 10

def add_message(messages, new_message):
    messages.append(new_message)
    # 只保留最新的对话
    if len(messages) > MAX_HISTORY_LENGTH:
        messages = messages[-MAX_HISTORY_LENGTH:]
    return messages
```

---

### 2. 并发请求优化

当需要批量处理时，使用异步调用：

```python
import asyncio
from anthropic import AsyncAnthropic

async def process_batch(prompts: list[str]):
    """并发处理多个请求"""
    client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    async def process_one(prompt):
        response = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    # 并发执行
    results = await asyncio.gather(*[process_one(p) for p in prompts])
    return results

# 使用示例
prompts = ["问题1", "问题2", "问题3"]
results = asyncio.run(process_batch(prompts))
```

---

### 3. 缓存机制

对于重复的请求，实现简单的缓存：

```python
from functools import lru_cache
import hashlib

class CachedAgent:
    def __init__(self):
        self.cache = {}

    def get_cache_key(self, prompt: str) -> str:
        """生成缓存键"""
        return hashlib.md5(prompt.encode()).hexdigest()

    def chat(self, prompt: str) -> str:
        """带缓存的聊天"""
        cache_key = self.get_cache_key(prompt)

        # 检查缓存
        if cache_key in self.cache:
            print("命中缓存")
            return self.cache[cache_key]

        # 调用 API
        response = client.messages.create(...)
        result = response.content[0].text

        # 存入缓存
        self.cache[cache_key] = result
        return result
```

---

## 安全注意事项

### 1. API Key 保护

✅ **正确做法**：
```python
# 使用环境变量
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("请设置 ANTHROPIC_API_KEY 环境变量")
```

❌ **危险做法**：
```python
# 永远不要硬编码 API Key
api_key = "sk-ant-api03-xxxxx"  # ❌❌❌

# 永远不要提交 .env 文件到 Git
# 添加到 .gitignore:
# .env
# *.key
```

---

### 2. 输入验证

```python
def safe_chat(user_input: str) -> str:
    """安全的聊天函数"""
    # 1. 长度检查
    if len(user_input) > 10000:
        raise ValueError("输入过长，请控制在 10000 字符以内")

    # 2. 内容过滤（根据业务需求）
    forbidden_keywords = ["敏感词1", "敏感词2"]
    if any(keyword in user_input for keyword in forbidden_keywords):
        raise ValueError("输入包含不允许的内容")

    # 3. 调用 API
    return client.messages.create(...)
```

---

### 3. 成本控制

```python
class CostTracker:
    """成本跟踪器"""

    # 价格（假设值，以实际为准）
    PRICING = {
        "claude-3-5-sonnet-20241022": {
            "input": 0.003,   # 每 1K tokens
            "output": 0.015,
        }
    }

    def __init__(self):
        self.total_cost = 0.0

    def track_request(self, response):
        """跟踪单次请求成本"""
        usage = response.usage
        model = response.model

        input_cost = (usage.input_tokens / 1000) * self.PRICING[model]["input"]
        output_cost = (usage.output_tokens / 1000) * self.PRICING[model]["output"]

        request_cost = input_cost + output_cost
        self.total_cost += request_cost

        print(f"本次成本: ${request_cost:.4f}")
        print(f"累计成本: ${self.total_cost:.4f}")

# 使用示例
tracker = CostTracker()
response = client.messages.create(...)
tracker.track_request(response)
```

---

## 调试技巧

### 1. 详细日志

```python
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'agent_{datetime.now():%Y%m%d}.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def debug_chat(message):
    """带调试信息的聊天"""
    logger.info(f"用户输入: {message}")

    response = client.messages.create(...)

    logger.debug(f"API 响应: {response}")
    logger.info(f"Token 使用: {response.usage}")

    return response.content[0].text
```

---

### 2. 断点调试技巧

```python
# 在关键位置打印中间结果
def complex_agent_step():
    # 步骤 1
    result1 = do_step1()
    print(f"步骤 1 结果: {result1}")  # 调试点 1

    # 步骤 2
    result2 = do_step2(result1)
    print(f"步骤 2 结果: {result2}")  # 调试点 2

    return result2
```

---

### 3. 单元测试

```python
import unittest
from unittest.mock import Mock, patch

class TestAgent(unittest.TestCase):
    """Agent 单元测试"""

    @patch('anthropic.Anthropic')
    def test_chat(self, mock_anthropic):
        """测试聊天功能"""
        # Mock API 响应
        mock_response = Mock()
        mock_response.content = [Mock(text="Hello!")]
        mock_anthropic.return_value.messages.create.return_value = mock_response

        # 测试
        agent = ExampleAgent()
        result = agent.chat("Hi")

        self.assertEqual(result, "Hello!")
```

---

## 生产环境检查清单

在部署到生产环境前，确保：

### 代码质量
- [ ] 所有函数都有类型提示
- [ ] 所有公开函数都有 Docstring
- [ ] 遵循 PEP 8 代码规范
- [ ] 通过了单元测试（覆盖率 > 80%）

### 安全性
- [ ] API Key 存储在环境变量中
- [ ] `.env` 文件已添加到 `.gitignore`
- [ ] 实现了输入验证
- [ ] 敏感信息不会被记录到日志

### 稳定性
- [ ] 实现了错误处理和重试机制
- [ ] 添加了超时控制
- [ ] 实现了日志记录
- [ ] 有监控和告警机制

### 性能
- [ ] Token 使用已优化
- [ ] 实现了必要的缓存
- [ ] 成本跟踪已部署
- [ ] 负载测试已通过

---

## 推荐工具和库

### 开发工具
- **Poetry**: Python 依赖管理
- **Black**: 代码格式化
- **Ruff**: 快速 Linter
- **pytest**: 单元测试框架

### 监控工具
- **Langfuse**: LLM 应用监控
- **Weights & Biases**: 实验跟踪

### 部署工具
- **Docker**: 容器化
- **FastAPI**: API 服务框架

---

## 学习资源

### 官方资源
- [Anthropic 官方文档](https://docs.anthropic.com)
- [Claude API 参考](https://docs.anthropic.com/claude/reference)

### 社区资源
- [GitHub Discussions](https://github.com/anthropics/anthropic-sdk-python/discussions)
- [Discord 社区]

---

## 下一步

✅ 学习完最佳实践后：
- 前往 `projects/` 目录完成实战项目
- 将这些实践应用到你的实际项目中

💡 **建议**：创建一个 `utils.py` 文件，封装常用的错误处理、重试、日志等功能，在后续项目中复用。

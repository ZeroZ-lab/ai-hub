# 使用自定义 API 指南

如果你想使用 API 代理或其他兼容 Claude API 的服务，请按以下步骤配置。

## 使用场景

1. **使用 API 代理服务**（如国内的代理）
2. **使用兼容 Claude API 的开源模型**（如某些本地部署的模型）
3. **使用企业内部的 API 网关**

---

## 配置方法

### 1. 编辑 .env 文件

```bash
# Anthropic API Key（某些代理服务可能不需要真实的 key）
ANTHROPIC_API_KEY=your-api-key-or-proxy-token

# 设置自定义 API Base URL
ANTHROPIC_BASE_URL=https://your-proxy-api.com/v1
```

### 2. 运行程序

程序会自动检测并使用自定义的 base URL：

```bash
uv run solution/main.py
```

你会看到类似的输出：
```
🔗 使用自定义 API: https://your-proxy-api.com/v1
✅ Agent 已启动
```

---

## 常见代理服务配置示例

### 示例 1：使用某个代理服务

```bash
# .env
ANTHROPIC_API_KEY=sk-xxx  # 代理服务提供的 key
ANTHROPIC_BASE_URL=https://proxy.example.com/v1
```

### 示例 2：使用本地模型

```bash
# .env
ANTHROPIC_API_KEY=local  # 本地模型可能不验证 key
ANTHROPIC_BASE_URL=http://localhost:8000/v1
MODEL_NAME=your-local-model-name
```

---

## 代码实现细节

在 `solution/main.py` 中，我们这样处理 base URL：

```python
# 读取环境变量
base_url = os.getenv("ANTHROPIC_BASE_URL")

# 创建客户端
if base_url:
    self.client = Anthropic(api_key=api_key, base_url=base_url)
    print(f"🔗 使用自定义 API: {base_url}")
else:
    self.client = Anthropic(api_key=api_key)
```

---

## 兼容性说明

- ✅ 支持所有兼容 Anthropic Messages API 格式的服务
- ✅ 支持 HTTP 和 HTTPS
- ⚠️ 确保目标 API 支持 `messages.create()` 接口
- ⚠️ 模型名称可能需要根据服务调整（通过 `MODEL_NAME` 环境变量）

---

## 故障排查

### 问题 1：连接失败

```
❌ API 调用失败: Connection error
```

**解决方案**：
1. 检查 `ANTHROPIC_BASE_URL` 是否正确
2. 确认网络可以访问该 URL
3. 检查是否需要 VPN 或代理

### 问题 2：认证失败

```
❌ API 调用失败: 401 Unauthorized
```

**解决方案**：
1. 确认 `ANTHROPIC_API_KEY` 正确
2. 某些服务可能使用不同的认证方式，查看服务商文档

### 问题 3：模型不存在

```
❌ API 调用失败: Model not found
```

**解决方案**：
在 `.env` 中设置正确的模型名称：
```bash
MODEL_NAME=your-actual-model-name
```

---

## 安全提示

⚠️ **注意**：
- 不要在公开代码中暴露 API endpoint
- 使用 HTTPS 而不是 HTTP（除非是本地测试）
- 定期轮换 API Key
- 使用代理时，确保服务商可信

---

需要帮助？查看主 README.md 或提交 Issue。

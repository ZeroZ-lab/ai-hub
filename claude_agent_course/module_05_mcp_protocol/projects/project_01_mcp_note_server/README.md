# MCP Note Server - 笔记服务

> **难度**: 🌟🌟 中级
> **预计时间**: 60-90 分钟

---

## 项目背景
MCP Server 能将工具能力从客户端剥离为可复用服务。本项目通过“笔记服务”展示 MCP Server 的基本结构与调用方式。

---

## 学习目标
- [ ] 定义 MCP Server 与工具
- [ ] 在客户端启用 mcp_servers
- [ ] 设计稳定的输出格式
- [ ] 处理错误与边界条件

---

## 功能需求

### 必做功能
1. **新增笔记**
   - 输入：标题、内容
   - 输出：写入结果

2. **列出笔记**
   - 输出：笔记列表（id、标题、时间）

3. **搜索笔记**
   - 输入：关键词
   - 输出：匹配结果

---

## 技术要点
- 工具通过 `@tool` 装饰器定义
- 使用 `create_sdk_mcp_server` 创建 MCP Server
- 客户端通过 `mcp_servers` 注册服务

---

## 实现步骤

### 第一步：实现 MCP Server
在 `src/server.py` 中实现：
- `add_note`
- `list_notes`
- `search_notes`

### 第二步：实现 Agent
在 `src/agent.py` 中：
- 配置 `ClaudeAgentOptions`
- 启用 MCP Server
- 实现 `add_note` / `list_notes` / `search_notes`

### 第三步：实现 CLI
在 `src/main.py` 中实现交互命令。

---

## 测试方法
```bash
cd claude_agent_course/module_05_mcp_protocol/projects/project_01_mcp_note_server
uv sync
uv run python src/main.py
```

### 示例
```
> add Onboarding | Setup dev environment
> list
> search environment
```

---

## 项目结构
```
project_01_mcp_note_server/
├── README.md
├── pyproject.toml
├── .env.example
├── data/
│   └── notes.json
├── src/
│   ├── __init__.py
│   ├── server.py
│   ├── agent.py
│   └── main.py
└── solution/
    ├── server.py
    ├── agent.py
    ├── main.py
    └── output_example.md
```

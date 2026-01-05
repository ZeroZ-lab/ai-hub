# MCP Filesystem Agent - 文件系统助手

> **难度**: 🌟🌟 中级
> **预计时间**: 60-90 分钟

---

## 项目背景
MCP Filesystem Server 提供安全的文件操作能力。本项目通过客户端调用 MCP Filesystem 工具，实现目录检索、文件读取与简单分析。

---

## 学习目标
- [ ] 了解 Filesystem MCP 服务的能力
- [ ] 使用 MCP 工具读取与搜索文件
- [ ] 输出稳定的结果格式

---

## 功能需求

### 必做功能
1. **列出目录内容**
2. **读取文件内容（只读）**
3. **搜索关键字**

---

## 技术要点
- MCP Server: Filesystem (官方参考)
- 客户端配置 `mcp_servers` 与 `allowed_tools`

---

## 实现步骤

### 第一步：准备 MCP Server
参考官方 Filesystem MCP Server 说明，启动本地服务。

### 第二步：实现 Agent
在 `src/agent.py` 中：
- 配置 MCP Server
- 实现 `list_dir` / `read_file` / `search`

### 第三步：实现 CLI
在 `src/main.py` 中解析命令。

---

## 测试方法
```bash
cd claude_agent_course/module_05_mcp_protocol/projects/project_02_mcp_filesystem_agent
uv sync
uv run python src/main.py
```

---

## 项目结构
```
project_02_mcp_filesystem_agent/
├── README.md
├── pyproject.toml
├── .env.example
├── samples/
│   └── sample_dir/
├── src/
│   ├── __init__.py
│   ├── agent.py
│   └── main.py
└── solution/
    ├── agent.py
    ├── main.py
    └── output_example.md
```

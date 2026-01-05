# MCP Git Inspector - 仓库分析助手

> **难度**: 🌟🌟 中级
> **预计时间**: 60-90 分钟

---

## 项目背景
Git MCP Server 提供仓库级检索能力。本项目构建一个 Git 分析助手，支持提交搜索与变更摘要。

---

## 学习目标
- [ ] 使用 Git MCP Server
- [ ] 查询提交记录
- [ ] 输出变更摘要

---

## 功能需求

### 必做功能
1. **列出最近提交**
2. **按关键词搜索提交**
3. **查看指定提交信息**

---

## 实现步骤

### 第一步：准备 MCP Server
参考官方 Git MCP Server 说明，启动本地服务。

### 第二步：实现 Agent
在 `src/agent.py` 中实现：
- `recent_commits`
- `search_commits`
- `show_commit`

### 第三步：实现 CLI
在 `src/main.py` 中解析命令。

---

## 测试方法
```bash
cd claude_agent_course/module_05_mcp_protocol/projects/project_03_mcp_git_inspector
uv sync
uv run python src/main.py
```

---

## 项目结构
```
project_03_mcp_git_inspector/
├── README.md
├── pyproject.toml
├── .env.example
├── samples/
│   └── repo_path.txt
├── src/
│   ├── __init__.py
│   ├── agent.py
│   └── main.py
└── solution/
    ├── agent.py
    ├── main.py
    └── output_example.md
```

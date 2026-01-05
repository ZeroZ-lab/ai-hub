# MCP SQLite Analyst - 本地数据库分析

> **难度**: 🌟🌟 中级
> **预计时间**: 60-90 分钟

---

## 项目背景
SQLite MCP Server 能提供本地数据库查询能力。本项目构建一个分析助手，执行基础查询与汇总。

---

## 学习目标
- [ ] 使用 SQLite MCP Server
- [ ] 运行查询与聚合
- [ ] 输出稳定的查询结果

---

## 功能需求

### 必做功能
1. **列出表结构**
2. **执行查询**
3. **执行统计汇总**

---

## 实现步骤

### 第一步：准备 MCP Server
参考官方 SQLite MCP Server 说明，启动本地服务。

### 第二步：实现 Agent
在 `src/agent.py` 中实现：
- `list_tables`
- `run_query`
- `aggregate`

### 第三步：实现 CLI
在 `src/main.py` 中解析命令。

---

## 测试方法
```bash
cd claude_agent_course/module_05_mcp_protocol/projects/project_04_mcp_sqlite_analyst
uv sync
uv run python src/main.py
```

---

## 项目结构
```
project_04_mcp_sqlite_analyst/
├── README.md
├── pyproject.toml
├── .env.example
├── samples/
│   ├── sample.db
│   └── schema.sql
├── src/
│   ├── __init__.py
│   ├── agent.py
│   └── main.py
└── solution/
    ├── agent.py
    ├── main.py
    └── output_example.md
```

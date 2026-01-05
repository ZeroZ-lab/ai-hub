# News Aggregator - 新闻聚合助手

> **难度**: 🌟🌟🌟 中高级
> **预计时间**: 90-120 分钟

---

## 项目背景
新闻信息来源分散，人工收集和整理效率低。本项目使用**自定义工具**构建新闻聚合助手，支持检索、筛选与摘要。

---

## 学习目标
- [ ] 使用 `@tool` 实现数据检索工具
- [ ] 在 MCP 服务器注册多工具
- [ ] 基于工具结果生成摘要与要点
- [ ] 设计清晰的交互指令

---

## 功能需求

### 必做功能
1. **获取头条**
   - 输入：数量
   - 输出：最新新闻列表

2. **关键词搜索**
   - 输入：关键词
   - 输出：匹配新闻

3. **分类筛选**
   - 输入：分类（如 technology, business）
   - 输出：对应分类的新闻

### 选做功能
- [ ] 生成每日摘要
- [ ] 支持来源筛选
- [ ] 输出简明报告（标题 + 来源 + 摘要）

---

## 技术要点
- 使用本地 `data/articles.json` 作为模拟数据源
- 工具返回 JSON 字符串，Agent 负责组织输出
- 需要处理无结果或异常输入

---

## 实现步骤

### 第一步：实现工具
在 `src/tools.py` 中实现：
- `get_top_headlines`
- `search_news`
- `filter_by_category`
- `list_sources`

### 第二步：实现 Agent
在 `src/agent.py` 中：
- 注册 MCP 服务器
- 配置工具白名单
- 实现 `top`, `search`, `category`, `digest`

### 第三步：实现 CLI
在 `src/main.py` 中实现交互：
- `top 5`
- `search ai chips`
- `category technology`
- `digest ai`

---

## 测试方法
```bash
cd claude_agent_course/module_03_custom_tools/projects/project_05_news_aggregator
uv sync
uv run python src/main.py
```

### 示例
```
> top 3
1) AI Chips Drive Record Earnings - TechWire
2) Energy Storage Prices Fall - GridToday
3) Startup Raises Series B - VentureDaily

> digest ai
- AI chips demand keeps accelerating with new data-center orders (TechWire)
- Research group releases new benchmark for LLM efficiency (ModelWatch)
```

---

## 完成标准
- [ ] 支持头条、搜索、分类
- [ ] 输出结构清晰
- [ ] 能处理无结果场景

---

## 项目结构
```
project_05_news_aggregator/
├── README.md
├── pyproject.toml
├── .env.example
├── data/
│   └── articles.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   └── tools.py
└── solution/
    ├── __init__.py
    ├── main.py
    ├── agent.py
    └── tools.py
```

---

开始构建你的新闻聚合助手！

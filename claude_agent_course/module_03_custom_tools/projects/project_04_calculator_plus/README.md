# Calculator Plus - 高级计算器助手

> **难度**: 🌟🌟 中级
> **预计时间**: 60-90 分钟

---

## 项目背景
普通计算器只能做简单加减乘除，本项目使用**自定义工具**打造一个支持多步运算、统计和函数计算的计算器助手。

---

## 学习目标
- [ ] 使用 `@tool` 定义多个数学工具
- [ ] 在 MCP 服务器中注册工具
- [ ] 让 Agent 根据用户输入选择合适工具
- [ ] 处理异常计算（除零、负数开方等）

---

## 功能需求

### 必做功能
1. **基础运算**
   - 输入：自然语言或表达式（如 `12 / 4`）
   - 输出：计算结果

2. **进阶运算**
   - 支持幂、开方、百分比等

3. **统计运算**
   - 支持均值、求和等简单统计

### 选做功能
- [ ] 支持批量计算
- [ ] 输出计算步骤
- [ ] 支持自定义精度

---

## 技术要点
- 自定义工具必须返回 `{"content": [{"type": "text", "text": "..."}]}`
- 出错时返回 `is_error: True`
- Agent 需要显式调用工具完成计算

---

## 实现步骤

### 第一步：实现工具
在 `src/tools.py` 中实现：
- `add` / `subtract` / `multiply` / `divide`
- `power` / `sqrt`
- `mean`（可选）

### 第二步：实现 Agent
在 `src/agent.py` 中：
- 创建 MCP 服务器
- 配置 `ClaudeAgentOptions`
- 实现 `calculate` 方法

### 第三步：实现 CLI
在 `src/main.py` 中处理用户输入：
- `calc <expression>`
- `stats mean 1,2,3`

---

## 测试方法
```bash
cd claude_agent_course/module_03_custom_tools/projects/project_04_calculator_plus
uv sync
uv run python src/main.py
```

### 示例
```
> calc (3 + 5) * 2
结果: 16

> stats mean 3,5,9
结果: 5.6667
```

---

## 完成标准
- [ ] 支持基础四则运算
- [ ] 支持至少 2 个进阶功能
- [ ] 能处理常见错误输入

---

## 项目结构
```
project_04_calculator_plus/
├── README.md
├── pyproject.toml
├── .env.example
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

开始构建你的高级计算器吧！

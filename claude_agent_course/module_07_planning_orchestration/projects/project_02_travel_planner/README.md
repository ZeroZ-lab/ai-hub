# Project 2: Travel Planner

> "凡事预则立，不预则废。" —— 孔子 (Context-aware version)

## 🎯 目标
构建一个能够处理长程任务的 Agent。对于"帮我规划去日本的 7 天旅行"这样的请求，直接 ReAct 容易陷入细节（比如第一步就卡在买哪天的机票），导致全局目标丢失。

我们将使用 **Plan-and-Solve** 模式：
1.  **Planner**: 生成一个包含 3-5 个步骤的高层计划。
2.  **Executor**: 逐个执行这些步骤。

## 🛠️ 任务清单
1.  在 `src/tools.py` 中实现模拟工具（search_flights, search_hotels, book_ticket）。
2.  在 `src/planner.py` 中编写 Prompt，让 LLM 输出 JSON 格式的计划列表。
3.  在 `src/executor.py` 中实现执行逻辑，它接收单步指令并调用工具。
4.  在 `src/main.py` 中串联整个流程。

## 🧠 思考题
- 如果 Executor 在第 3 步发现没有酒店了，怎么办？
- 如何实现 **Replanning**（重新规划）？

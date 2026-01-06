# 03. 多 Agent 编排：Orchestrator-Workers

> "如果要造一座摩天大楼，你不能只有一个全能工匠，你需要建筑师、工程师、水电工..."

## 1. 单 Agent 的局限性

随着任务复杂度的增加，单个 Agent 面临以下挑战：
- **Context Window**: 所有复杂的指令、工具定义、中间步骤都塞进一个 Context，容易溢出。
- **注意力分散**: 这里要写代码，那里要搜资料，Agent 容易"忘记"初衷或产生幻觉。
- **工具混淆**: 工具太多，容易选错。

## 2. Orchestrator-Workers 模式

这是一个分层架构：

- **Orchestrator (协调者/经理)**:
    -   **职责**: 负责理解用户的高层意图，分解任务，分派给 Worker，并整合结果。
    -   **工具**: `delegate_task(worker_name, task_description)`。
    -   **特点**: 视野宏观，不关注细节实现。

- **Workers (工作者/专家)**:
    -   **职责**: 专注于特定领域的任务（如 Research, Coding, Writing）。
    -   **工具**: 只有该领域相关的工具（如 Google Search, Python REPL）。
    -   **特点**: 专业性强，Context 干净。

## 3. 工作流示例：研报生成

**User**: "写一份关于 2024 年 AI 硬件市场的分析报告。"

1.  **Orchestrator**:
    -   思考：这是一个大任务。我需要先搜集信息，然后撰写。
    -   行动：调用 `Researcher` Agent。
    -   指令："搜集 2024 AI 硬件（GPU, ASIC）的市场规模、主要玩家和趋势。"

2.  **Worker: Researcher**:
    -   拥有工具：`GoogleSearch`, `WebScraper`。
    -   执行：搜索... 浏览... 整理数据。
    -   返回：一份包含数据和来源的摘要。

3.  **Orchestrator**:
    -   收到 Researcher 的摘要。
    -   行动：调用 `Writer` Agent。
    -   指令："根据这份数据摘要，写一篇 500 字的博客文章，风格专业。"

4.  **Worker: Writer**:
    -   拥有工具：无（纯文本生成）或 `GrammarChecker`。
    -   执行：撰写文章。
    -   返回：文章终稿。

5.  **Orchestrator**:
    -   检查结果，返回给用户。

## 4. 路由 (Routing) vs 编排 (Orchestration)

| | Routing | Orchestration |
| :--- | :--- | :--- |
| **定义** | 将请求转发给最合适的一个 Agent | 动态管理多个 Agent 协同工作 |
| **关系** | 1:1 (User -> Agent A) | 1:N (User -> Orch -> A, B, C) |
| **状态** | 通常无状态 | 维护整个任务的全局状态 |
| **示例** | 客服机器人分类（售后 vs 售前） | 软件开发（PM -> Dev -> QA） |

## 5. 实现挑战

- **通信协议**: Agent 之间怎么说话？（通常是自然语言）。
- **死循环**: Worker A 抛给 Worker B，B 又抛给 A。Orchestrator 需要监控进度。
- **成本**: 多个 Agent 意味着多次 API 调用，成本倍增。

在 **Project 4** 中，我们将实现这个模式，体验像"经理"一样指挥 AI 团队。

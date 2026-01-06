# Project 4: Orchestrator Workers Team

> "一个人走得快，一群人走得远。"

## 🎯 目标
实现这一章的终极形态：多 Agent 协作系统。我们将解决 "生成一份包含最新数据的行业研报" 这一复杂任务。

## 👥 团队成员
1.  **Orchestrator**: 项目经理。负责接收需求，由它调用 Researcher 和 Writer。
2.  **Researcher**: 研究员。拥有 `WikiSearch` 工具。
3.  **Writer**: 作家。没有外部工具，专注于文本生成。

## 🛠️ 任务清单
1.  定义 3 个 Agent 类（或者复用同一个类但给不同的 System Prompt）。
2.  为 Orchestrator 定义特殊工具：`call_researcher`, `call_writer`。
3.  实现 Worker 的返回机制（Worker 完成后将结果返回给 Orchestrator）。
4.  串联整个流程。

## 🧠 思考题
- 如果 Researcher 查不到资料怎么办？Orchestrator 会怎么做？
- 如何共享 Context？还是完全隔离？（推荐隔离，保持 Worker 专注）

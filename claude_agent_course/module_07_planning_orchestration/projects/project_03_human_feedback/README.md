# Project 3: Human-in-the-loop

> "有些按钮，不能让 AI 随便按。"

## 🎯 目标
构建一个处理敏感操作的 Agent。当 Agent 想要执行敏感操作（如 `send_email` 或 `refund_user`）时，系统必须暂停并请求人类批准。

## 🛠️ 任务清单
1.  定义 `send_email` 工具，并在代码中标记为 `sensitive=True`。
2.  实现 `HumanLayer` 类，拦截工具调用。
3.  如果工具是敏感的 -> `input("Approve? (y/n)")`。
4.  如果 `y` -> 执行；如果 `n` -> 将 "User rejected" 作为 Observation 返回给 Agent。

## 🧠 思考题
- 假如用户想修改邮件内容，你的逻辑支持吗？
- 如何设置超时自动拒绝？

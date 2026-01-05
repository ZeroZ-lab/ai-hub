# Module 6: Memory & Context - 记忆与上下文管理

> **Phase 3: 智慧 (Intelligence)**
> 学习如何让 Agent 拥有长期记忆和高效的上下文管理能力

## 📚 学习目标

完成本模块后，你将能够：
- [ ] 理解 Agent 的上下文窗口限制与挑战
- [ ] 掌握 Session 管理与会话持久化
- [ ] 使用 Prompt Caching 优化 API 成本
- [ ] 实现向量数据库记忆系统
- [ ] 设计多轮对话的上下文策略

## 📖 先修知识

- 完成 Module 1-5
- 理解 LLM 的 token 限制
- 熟悉基本的数据库操作（加分项）

## 📂 内容概览

### 文档 (docs/)
1. [01_概念讲解.md](docs/01_概念讲解.md) - 上下文管理的核心概念
2. [02_代码示例.md](docs/02_代码示例.md) - Session 与 Caching 示例
3. [03_最佳实践.md](docs/03_最佳实践.md) - 记忆系统设计模式

### 实战项目 (projects/)
1. [project_01_session_manager](projects/project_01_session_manager/) - 会话管理器
2. [project_02_cached_qa_bot](projects/project_02_cached_qa_bot/) - 使用 Prompt Caching 的问答机器人
3. [project_03_vector_memory](projects/project_03_vector_memory/) - 向量记忆系统
4. [project_04_context_compressor](projects/project_04_context_compressor/) - 上下文压缩器

## ⏱️ 预计学习时间

- 理论学习：2-3 小时
- 实战项目：3-4 小时
- **总计**：5-7 小时

## 🎯 学习路径

```
开始
  ↓
阅读 01_概念讲解.md（理解上下文窗口）
  ↓
阅读 02_代码示例.md（Session 管理）
  ↓
完成 project_01（会话管理器）
  ↓
完成 project_02（Prompt Caching）
  ↓
阅读 03_最佳实践.md（记忆系统设计）
  ↓
完成 project_03（向量记忆）
  ↓
完成 project_04（上下文压缩）
  ↓
✅ 完成 Module 6
```

## 🔑 核心概念

### 1. 上下文窗口
- Token 限制（Claude 3.5 Sonnet: 200K tokens）
- 输入 vs 输出 token 管理
- 长文档处理策略

### 2. Session 管理
- 会话状态持久化
- 历史消息存储
- 会话恢复机制

### 3. Prompt Caching
- 缓存机制原理
- 成本优化策略
- 适用场景分析

### 4. 向量记忆
- Embedding 向量化
- 语义搜索检索
- 长期记忆存储

## 🔗 相关资源

- [Claude API: Prompt Caching](https://docs.anthropic.com/claude/docs/prompt-caching)
- [Claude API: Long Context](https://docs.anthropic.com/claude/docs/long-context-window-tips)
- [Claude Agent SDK: Sessions](https://docs.anthropic.com/agent-sdk/sessions)

## ❓ 常见问题

### Q1: 什么时候应该使用 Prompt Caching？
A: 当你有大量固定的上下文（如文档、代码库）需要重复使用时，Prompt Caching 可以大幅降低成本。

### Q2: 向量记忆和普通数据库有什么区别？
A: 向量记忆基于语义相似度检索，而不是精确匹配。适合处理自然语言查询和长期知识存储。

### Q3: Session 管理如何实现？
A: 通过保存完整的对话历史（messages 数组），在每次 API 调用时传入历史消息，实现上下文连续性。

---

## 下一步

完成本模块后，继续学习：
- **[Module 7: Planning & Orchestration](../module_07_planning_orchestration/)** - 思维链与复杂任务规划

---

**开始学习吧！🚀**

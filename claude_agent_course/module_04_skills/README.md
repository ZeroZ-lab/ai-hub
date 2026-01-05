# Module 4: Agent Skills - 能力扩展

> **Phase 2: 连接 (Connection)**
> 学习如何通过 Skills 为 Agent 注入专业知识和工作流程

## 📚 学习目标

完成本模块后，你将能够：
- [ ] 理解 Skills 与 Slash Commands 的区别
- [ ] 掌握 SKILL.md 的编写规范
- [ ] 创建项目级和个人级 Skills
- [ ] 在 Claude Agent SDK 中启用和使用 Skills

## 📖 先修知识

- 完成 Module 1-3
- 理解 Agent 的工具调用机制
- 熟悉 YAML 语法（加分项）

## 📂 内容概览

### 文档 (docs/)
1. [01_概念讲解.md](docs/01_概念讲解.md) - Skills 是什么？如何自动触发？
2. [02_代码示例.md](docs/02_代码示例.md) - SKILL.md 编写与配置
3. [03_最佳实践.md](docs/03_最佳实践.md) - 复杂 Skill 设计模式

### 实战项目 (projects/)
1. [project_01_code_reviewer](projects/project_01_code_reviewer/) - 创建代码审查 Skill

## ⏱️ 预计学习时间

- 理论学习：1-2 小时
- 实战项目：2-3 小时
- **总计**：3-5 小时

## 🎯 学习路径

```
开始
  ↓
阅读 01_概念讲解.md（理解 Skills 机制）
  ↓
阅读 02_代码示例.md（SKILL.md 编写）
  ↓
完成 project_01（代码审查 Skill）
  ↓
阅读 03_最佳实践.md（高级设计模式）
  ↓
✅ 完成 Module 4
```

## 🔗 相关资源

- [Claude Code Skills 文档](https://docs.anthropic.com/claude-code/skills)
- [Claude Agent SDK Skills 配置](https://docs.anthropic.com/agent-sdk/skills)

## ❓ 常见问题

### Q1: Skills 和 Slash Commands 有什么区别？
A:
- **Slash Commands**：用户手动触发（如 `/commit`）
- **Skills**：Claude 根据上下文自动发现和触发

### Q2: Skills 放在哪里？
A:
- 项目级：`.claude/skills/<skill-name>/SKILL.md`
- 个人级：`~/.claude/skills/<skill-name>/SKILL.md`

### Q3: SDK 中如何启用 Skills？
A: 需要在选项中配置 `setting_sources` 和 `allowed_tools`:
```python
options = ClaudeAgentOptions(
    setting_sources=["user", "project"],
    allowed_tools=["Skill", ...]
)
```

---

## 下一步

完成本模块后，继续学习：
- **[Module 5: MCP 协议](../module_05_mcp_protocol/)** - Model Context Protocol 深度解析

---

**开始学习吧！🚀**

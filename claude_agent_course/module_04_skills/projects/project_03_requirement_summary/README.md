# Requirement Summary - 需求摘要技能

> **难度**: 🌟 初级
> **预计时间**: 30-45 分钟

---

## 项目背景
需求文档通常篇幅长、信息散。本项目将“需求摘要”固化为 Skill，快速提炼范围、约束与风险。

---

## 学习目标
- [ ] 编写精准的触发描述
- [ ] 输出结构化需求要点
- [ ] 识别风险与未决问题

---

## 功能需求

### 必做功能
1. **总结需求目标**
2. **输出功能与非功能约束**
3. **列出风险和问题**

---

## 实现步骤

### 第一步：完善 SKILL.md
编辑 `.claude/skills/requirement-summary/SKILL.md`。

### 第二步：准备输入
使用 `samples/requirement.md`。

### 第三步：在 SDK 中调用
在 `src/main.py` 中调用技能（本项目提供 TODO 框架）。

---

## 测试方法
```bash
cd claude_agent_course/module_04_skills/projects/project_03_requirement_summary
uv sync
uv run python src/main.py samples/requirement.md
```

---

## 项目结构
```
project_03_requirement_summary/
├── README.md
├── pyproject.toml
├── .env.example
├── .claude/skills/requirement-summary/SKILL.md
├── samples/
│   └── requirement.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
└── solution/
    └── output_example.md
```

# PR Description Generator - PR 描述生成技能

> **难度**: 🌟 初级
> **预计时间**: 30-45 分钟

---

## 项目背景
PR 描述通常写得不统一。本项目将 PR 描述格式固化为 Skill，保证标题、变更与测试信息完整。

---

## 学习目标
- [ ] 设计清晰的 PR 输出模板
- [ ] 从变更描述中提取重点
- [ ] 输出可直接粘贴的 PR 描述

---

## 功能需求

### 必做功能
1. **生成 PR 标题与摘要**
2. **列出主要变更**
3. **列出测试信息**

---

## 实现步骤

### 第一步：完善 SKILL.md
编辑 `.claude/skills/pr-description-generator/SKILL.md`。

### 第二步：准备输入
使用 `samples/change_notes.txt`。

### 第三步：在 SDK 中调用
在 `src/main.py` 中调用技能（本项目提供 TODO 框架）。

---

## 测试方法
```bash
cd claude_agent_course/module_04_skills/projects/project_04_pr_description_generator
uv sync
uv run python src/main.py samples/change_notes.txt
```

---

## 项目结构
```
project_04_pr_description_generator/
├── README.md
├── pyproject.toml
├── .env.example
├── .claude/skills/pr-description-generator/SKILL.md
├── samples/
│   └── change_notes.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
└── solution/
    └── output_example.md
```

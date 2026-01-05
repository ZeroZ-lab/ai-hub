# Meeting Notes Summarizer - 会议纪要技能

> **难度**: 🌟 初级
> **预计时间**: 30-45 分钟

---

## 项目背景
会议记录往往冗长且结构混乱。本项目将“会议纪要总结”固化为 Skill，输出统一的决议与行动项格式。

---

## 学习目标
- [ ] 编写精简的 `SKILL.md`
- [ ] 设计结构化输出格式
- [ ] 练习使用项目级 Skills

---

## 功能需求

### 必做功能
1. **总结会议要点**
2. **提取决议与行动项**
3. **输出结构化格式**

---

## 实现步骤

### 第一步：完善 SKILL.md
编辑 `.claude/skills/meeting-notes-summarizer/SKILL.md`，确认触发描述与输出格式。

### 第二步：准备输入
使用 `samples/meeting_notes.txt` 作为测试输入。

### 第三步：在 SDK 中调用
在 `src/main.py` 中调用技能（本项目提供了 TODO 框架）。

---

## 测试方法
```bash
cd claude_agent_course/module_04_skills/projects/project_02_meeting_notes_summarizer
uv sync
uv run python src/main.py samples/meeting_notes.txt
```

---

## 项目结构
```
project_02_meeting_notes_summarizer/
├── README.md
├── pyproject.toml
├── .env.example
├── .claude/skills/meeting-notes-summarizer/SKILL.md
├── samples/
│   └── meeting_notes.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
└── solution/
    └── output_example.md
```

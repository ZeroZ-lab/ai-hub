# Release Notes - 发布说明技能

> **难度**: 🌟🌟 中级
> **预计时间**: 45-60 分钟

---

## 项目背景
发布说明往往风格不统一。本项目将 Release Notes 的结构与分组规则固化为 Skill。

---

## 学习目标
- [ ] 按类别归纳变更
- [ ] 关注用户可感知变化
- [ ] 生成简洁的发布说明

---

## 功能需求

### 必做功能
1. **分类输出 Added / Changed / Fixed**
2. **标注版本与日期**
3. **指出破坏性变更**

---

## 实现步骤

### 第一步：完善 SKILL.md
编辑 `.claude/skills/release-notes/SKILL.md`。

### 第二步：准备输入
使用 `samples/changelog.txt`。

### 第三步：在 SDK 中调用
在 `src/main.py` 中调用技能（本项目提供 TODO 框架）。

---

## 测试方法
```bash
cd claude_agent_course/module_04_skills/projects/project_06_release_notes
uv sync
uv run python src/main.py samples/changelog.txt
```

---

## 项目结构
```
project_06_release_notes/
├── README.md
├── pyproject.toml
├── .env.example
├── .claude/skills/release-notes/SKILL.md
├── samples/
│   └── changelog.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
└── solution/
    └── output_example.md
```

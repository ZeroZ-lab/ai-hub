# Test Checklist - 测试清单技能

> **难度**: 🌟🌟 中级
> **预计时间**: 45-60 分钟

---

## 项目背景
测试计划常常不完整。本项目将测试清单整理流程固化为 Skill，覆盖单测、集成与回归。

---

## 学习目标
- [ ] 输出分层测试清单
- [ ] 覆盖边界与异常情况
- [ ] 保持测试描述可执行

---

## 功能需求

### 必做功能
1. **单测清单**
2. **集成测试清单**
3. **回归/负向测试清单**

---

## 实现步骤

### 第一步：完善 SKILL.md
编辑 `.claude/skills/test-checklist/SKILL.md`。

### 第二步：准备输入
使用 `samples/feature_spec.md`。

### 第三步：在 SDK 中调用
在 `src/main.py` 中调用技能（本项目提供 TODO 框架）。

---

## 测试方法
```bash
cd claude_agent_course/module_04_skills/projects/project_05_test_checklist
uv sync
uv run python src/main.py samples/feature_spec.md
```

---

## 项目结构
```
project_05_test_checklist/
├── README.md
├── pyproject.toml
├── .env.example
├── .claude/skills/test-checklist/SKILL.md
├── samples/
│   └── feature_spec.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
└── solution/
    └── output_example.md
```

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Claude Agent SDK 实战课程** - An educational project teaching developers to build autonomous AI agents through hands-on projects.

**Teaching Method**: Concept + Code + Project (概念+代码+项目)

---

## Package Management: uv

This project uses `uv` for dependency management:

```bash
# Install deps
uv sync

# Add package
uv add package-name

# Run code
uv run python script.py
```

---

## Repository Structure

```
claude_agent_course/
├── module_01_foundations/      # ✅ Agent basics
├── module_02_core_tools/       # 🚧 File & Bash
├── module_03_custom_tools/     # 🚧 Function calling
├── module_04_mcp_protocol/     # 🚧 MCP
├── module_05_memory_context/   # 🚧 Memory
├── module_06_planning/         # 🚧 CoT & ReAct
└── module_07_capstone/         # 🚧 DevMate project

templates/                      # 📝 Content creation templates
```

### Module Structure

```
module_XX_name/
├── README.md                  # Overview
├── docs/
│   ├── 01_概念讲解.md         # Concepts
│   ├── 02_代码示例.md         # Examples
│   └── 03_最佳实践.md         # Best practices
└── projects/
    └── project_01_name/
        ├── pyproject.toml     # uv config
        ├── src/
        ├── tests/
        └── solution/          # Reference
```

---

## For Contributors

### Creating Content

1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Use templates in `templates/`
3. Follow naming:
   - Modules: `module_XX_topic`
   - Projects: `project_XX_name`
   - Docs: `XX_中文名称.md`

### Workflow

```bash
# Create module
mkdir -p claude_agent_course/module_XX_name/{docs,projects}

# Copy templates
cp templates/docs_template_*.md claude_agent_course/module_XX_name/docs/

# Create project
cd claude_agent_course/module_XX_name/projects
mkdir project_01 && cd project_01
uv init --no-readme
uv add anthropic python-dotenv
```

---

## Quality Standards

- **Code**: Python 3.10+, type hints, PEP 8, docstrings
- **Docs**: Tested examples, clear explanations, Chinese (Simplified)
- **Projects**: Runnable, complete config, reference solution

---

## Tech Stack

- Python 3.10+
- `anthropic` (Claude API)
- `uv` (package manager)
- Model Context Protocol (MCP)

---

## Key Projects

- Module 2: News aggregator
- Module 3: Resume analyzer
- Module 4: Text-to-SQL
- Module 6: Code refactoring assistant
- Module 7: DevMate (GitHub automation)

---

## Links

- [README.md](README.md) - For learners
- [CONTRIBUTING.md](CONTRIBUTING.md) - For contributors

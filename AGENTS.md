# Repository Guidelines

## Project Structure & Module Organization
- Course content lives in `claude_agent_course/` with modules named `module_XX_topic/`.
- Each module typically contains:
  - `README.md`
  - `docs/` with `01_概念讲解.md`, `02_代码示例.md`, `03_最佳实践.md`
  - `projects/project_XX_name/` containing `pyproject.toml`, `src/`, `tests/`, and `solution/`.
- `templates/` holds reusable docs and project templates (e.g., `project_README_template.md`).
- Contributor info is in `README.md` and `CONTRIBUTING.md`.

## Build, Test, and Development Commands
Run commands inside a specific project directory (e.g., `claude_agent_course/module_01_foundations/projects/project_01_hello_agent/`).

```bash
# Install dependencies
uv sync

# Run a module script
uv run python src/main.py

# Run tests
uv run pytest tests/

# Add deps
uv add anthropic python-dotenv
uv add --dev pytest black ruff
```

## Coding Style & Naming Conventions
- Python 3.10+, PEP 8, type hints, and docstrings are expected.
- Indentation: 4 spaces; keep examples runnable and documented.
- Naming:
  - Modules: `module_XX_topic`
  - Projects: `project_XX_name`
  - Docs: `XX_中文名称.md`
  - Tests: `tests/test_*.py`

## Testing Guidelines
- Use `pytest` for project tests.
- Keep tests close to each project under `tests/` and follow the `test_*.py` pattern.
- Ensure example code in docs and `README.md` stays runnable.

## Commit & Pull Request Guidelines
- Git history uses Conventional Commit-style messages (e.g., `feat: add module structure`). Keep the subject short and imperative.
- PRs should include a clear description, link related issues, and attach test evidence (screenshots or output logs) when applicable.
- Follow the contributor flow in `CONTRIBUTING.md` (branch per change, templates for new content).

## Security & Configuration Tips
- Use `.env.example` as the reference for environment variables; keep secrets in a local `.env` that is not committed.
- When creating new projects, copy templates from `templates/` to ensure consistent structure.

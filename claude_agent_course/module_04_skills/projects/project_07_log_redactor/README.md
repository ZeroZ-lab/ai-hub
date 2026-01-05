# Log Redactor - Log Sanitization Skill

> Difficulty: Beginner
> Estimated time: 30-45 minutes

---

## Project background
Logs often contain secrets or PII that must be removed before sharing. This project builds a Skill that uses a bundled script to redact sensitive data and then summarize safely.

---

## Learning goals
- [ ] Add a script to a Skill bundle
- [ ] Reference scripts from SKILL.md
- [ ] Keep redaction deterministic and reproducible

---

## Requirements

### Must have
1. Redact emails, phone numbers, and API keys
2. Preserve log structure while masking values
3. Provide a concise summary if requested

---

## Steps

### Step 1: Review SKILL.md
Edit `.claude/skills/log-redactor/SKILL.md` and confirm the workflow and output format.

### Step 2: Run the redaction script
Use the bundled script on sample logs:
```bash
python .claude/skills/log-redactor/scripts/redact_logs.py \
  --input samples/raw.log \
  --output samples/redacted.log
```

### Step 3: Use the Skill
In `src/main.py`, load the log and ask for a redacted output (TODO scaffold provided).

---

## Test
```bash
cd claude_agent_course/module_04_skills/projects/project_07_log_redactor
uv sync
uv run python src/main.py samples/raw.log
```

---

## Structure
```
project_07_log_redactor/
├── README.md
├── pyproject.toml
├── .env.example
├── .claude/skills/log-redactor/
│   ├── SKILL.md
│   └── scripts/redact_logs.py
├── samples/
│   ├── raw.log
│   └── redacted.log
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
└── solution/
    └── output_example.md
```

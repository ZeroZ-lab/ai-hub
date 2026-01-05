# Data Converter - Data Format Conversion Assistant

> Difficulty: Intermediate
> Estimated time: 60-90 minutes

---

## Project background
Data often arrives in CSV or JSON, and teams lose time converting formats by hand. In this project you will build a data conversion assistant that detects input format and converts between CSV and JSON using custom tools.

---

## Learning goals
- [ ] Define custom tools with `@tool`
- [ ] Register tools with `create_sdk_mcp_server`
- [ ] Convert CSV to JSON and JSON to CSV reliably
- [ ] Handle parsing errors and empty input gracefully

---

## Functional requirements

### Required
1. **Detect input format**
   - Input: raw text
   - Output: `csv` or `json`

2. **Convert CSV to JSON**
   - Input: CSV text
   - Output: JSON array of objects

3. **Convert JSON to CSV**
   - Input: JSON object or array
   - Output: CSV text with a header row

### Optional
- [ ] Allow selecting a subset of fields
- [ ] Write output to a file when provided
- [ ] Add format validation with clear error messages

---

## Technical focus
- Use Python standard libraries (`csv`, `json`, `io`).
- Tools must return `{"content": [{"type": "text", "text": "..."}]}` and set `is_error` when needed.
- Agent should call tools explicitly and return only the converted data.

---

## Implementation steps

### Step 1: Implement tools
Edit `src/tools.py` and implement:
- `detect_format`
- `csv_to_json`
- `json_to_csv`

### Step 2: Implement the agent
Edit `src/agent.py`:
- Create an MCP server with the tools.
- Configure `ClaudeAgentOptions` with allowed tool names.
- Implement `detect_format` and `convert` methods.

### Step 3: Wire the CLI
Edit `src/main.py` to connect user commands to the agent.

---

## Run and test
```bash
cd claude_agent_course/module_03_custom_tools/projects/project_03_data_converter
uv sync
uv run python src/main.py
```

### Sample commands
```text
detect data/sample.csv
convert data/sample.csv json data/converted.json
convert data/sample.json csv data/converted.csv
```

---

## Completion checklist
- [ ] Detects CSV or JSON correctly
- [ ] Converts both directions without data loss
- [ ] Handles invalid input with clear errors
- [ ] CLI works with sample data files

---

## Project structure
```
project_03_data_converter/
├── README.md
├── pyproject.toml
├── .env.example
├── data/
│   ├── sample.csv
│   └── sample.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   └── tools.py
└── solution/
    ├── __init__.py
    ├── main.py
    ├── agent.py
    └── tools.py
```

---

Start by implementing the tools, then connect the agent, and finally wire up the CLI.

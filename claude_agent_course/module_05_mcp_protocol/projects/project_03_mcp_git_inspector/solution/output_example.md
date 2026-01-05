Example:

> recent /path/to/repo 3
[
  {"hash": "abc123", "message": "feat: add mcp module", "author": "you", "date": "2024-06-30"},
  {"hash": "def456", "message": "docs: update module 4", "author": "you", "date": "2024-06-29"}
]

> search /path/to/repo mcp
[
  {"hash": "abc123", "message": "feat: add mcp module"}
]

> show /path/to/repo abc123
{"hash": "abc123", "files": ["README.md", "src/main.py"], "summary": "add mcp module"}

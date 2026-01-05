---
name: pr-description-generator
description: Generate a PR description from change notes, commit lists, or diff summaries. Use when the user asks for PR description/PR 模板/PR 说明 or needs a structured PR summary.
---

# PR Description Generator

## Workflow
1. Identify the main change and motivation.
2. Summarize user-facing impact and internal changes separately.
3. List tests that were run or should be run.
4. Call out breaking changes or migration steps if mentioned.

## Output format
Title:
- ...

Summary:
- ...

Changes:
- ...

Impact:
- ...

Tests:
- ...

Breaking changes:
- ...

## Notes
- Keep it concise and ready to paste into a PR template.
- If tests are not provided, add "Not run (specify)".

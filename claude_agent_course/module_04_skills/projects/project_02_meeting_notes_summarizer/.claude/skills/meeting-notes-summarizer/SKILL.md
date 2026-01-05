---
name: meeting-notes-summarizer
description: Summarize meeting notes into decisions, action items, owners, and deadlines. Use when the user asks for meeting minutes/notes/会议纪要/会议总结 or wants structured meeting outcomes.
---

# Meeting Notes Summarizer

## Workflow
1. Identify the meeting topic, date, and participants if present.
2. Extract decisions and unresolved questions.
3. Extract action items with owner and due date when available.
4. Note risks, blockers, or dependencies.
5. Keep outputs concise and actionable.

## Output format
Summary:
- Topic:
- Date:
- Participants:

Decisions:
- ...

Action items:
- [Owner] task (due: YYYY-MM-DD or TBC)

Open questions:
- ...

Risks/Dependencies:
- ...

## Notes
- If owners or dates are missing, mark as TBC.
- Do not invent facts; only use provided content.

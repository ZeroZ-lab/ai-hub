import json
from .base import BaseAgent

PLANNER_SYSTEM_PROMPT = """
You are a Senior Technical Planner. 
Your goal is to break down a complex software development task into clear, actionable steps.

Analyze the user request and the provided project context (file structure).
Create a JSON list of steps. Each step should be for an 'Engineer' agent to execute.

Response Format:
{
  "thought": "Analysis of the task...",
  "plan": [
    "Step 1: Description...",
    "Step 2: Description..."
  ]
}

Keep steps atomic. For example, 'Create file x' and 'Implement function y' can be separate steps if complex.
"""

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Planner")

    def create_plan(self, task: str, project_tree: str) -> dict:
        user_message = f"""
Task: {task}

Project Structure:
{project_tree}

Provide your plan in JSON.
"""
        response = self._call_claude(
            system=PLANNER_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}]
        )
        
        try:
            content = response.content[0].text
            # Simple heuristic to extract JSON if there is extra text
            start_idx = content.find('{')
            end_idx = content.rfind('}') + 1
            if start_idx != -1 and end_idx != -1:
                json_str = content[start_idx:end_idx]
                return json.loads(json_str)
            return {"thought": "Failed to parse", "plan": [task]}
        except Exception as e:
            return {"thought": f"Error parsing plan: {e}", "plan": [task]}

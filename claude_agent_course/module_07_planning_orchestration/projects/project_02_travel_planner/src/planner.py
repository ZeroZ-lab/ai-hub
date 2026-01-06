import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

PLANNER_PROMPT = """
You are a Travel Planner. Given a user request, create a step-by-step plan.
Return the plan as a JSON list of strings.

Example:
Request: "Plan a trip to Paris"
Response: ["Search for flights to Paris", "Search for hotels in Paris", "Book the flight", "Book the hotel"]

User Request: {request}
"""

class Planner:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def create_plan(self, request: str):
        print("🤔 Thinking about the plan...")
        
        # 1. 调用 LLM 生成计划
        # 2. 解析 JSON
        # (简化起见，这里假设 LLM 很听话返回纯 JSON，实际需要更强的解析)
        
        # TODO: Implement LLM call
        # response = self.client.messages.create(...)
        # plan = json.loads(response.content[0].text)
        
        # Dummy plan for scaffolding
        return [
            f"Search for flights for: {request}",
            "Search for hotels"
        ]

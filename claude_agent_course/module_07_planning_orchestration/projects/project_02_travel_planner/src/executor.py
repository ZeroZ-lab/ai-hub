import os
from anthropic import Anthropic
from .tools import TOOLS_MAP

EXECUTOR_SYS_PROMPT = """
You are a helper. You will be given a SINGLE step of a plan, and previous history.
Execute the step using available tools.

Tools:
{tools_desc}
"""

class Executor:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def execute_step(self, step: str, context: str):
        print(f"▶️ Executing Step: {step}")
        
        # 这里可以使用我们在 Project 1 中做的 ReAct 循环，或者简单的 Function Calling
        # 为了演示，我们假设 LLM 决定调用哪个工具
        
        # TODO: Implement execution logic
        # 1. Construct prompt with current step + context
        # 2. LLM decides tool
        # 3. Call tool
        # 4. Return result
        
        return "Simulated Result: Done."

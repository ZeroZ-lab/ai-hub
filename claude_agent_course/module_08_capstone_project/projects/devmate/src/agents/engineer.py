from typing import Any
from .base import BaseAgent
from ..core.files import FileManager
from ..core.shell import ShellRunner

ENGINEER_SYSTEM_PROMPT = """
You are a Senior Software Engineer.
You will be given a specific sub-task to execute.
You have access to files and shell commands.

You MUST use the provided tools to verify your work.
For example, if you write a file, you might want to try running it or reading it back.

Process:
1. Think about how to solve the task.
2. Use tools (read_file, write_file, run_command) to implement solution.
3. Validate your changes.
4. When you are done, describe what you did.
"""

class EngineerAgent(BaseAgent):
    def __init__(self, file_manager: FileManager, shell_runner: ShellRunner):
        super().__init__("Engineer")
        self.files = file_manager
        self.shell = shell_runner
        
        self.tool_definitions = [
            {
                "name": "read_file",
                "description": "Read the content of a file",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Relative path to file"}
                    },
                    "required": ["path"]
                }
            },
            {
                "name": "write_file",
                "description": "Write content to a file. Overwrites if exists!",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Relative path to file"},
                        "content": {"type": "string", "description": "Full content of the file"}
                    },
                    "required": ["path", "content"]
                }
            },
            {
                "name": "run_command",
                "description": "Run a shell command",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "Shell command to run"}
                    },
                    "required": ["command"]
                }
            }
        ]

    def execute_step(self, step: str) -> str:
        messages = [{"role": "user", "content": f"Task: {step}"}]
        
        # ReAct-like loop (simplified: max 5 turns)
        for _ in range(5):
            response = self._call_claude(
                system=ENGINEER_SYSTEM_PROMPT,
                messages=messages,
                tools=self.tool_definitions
            )
            
            # Add assistant message to history
            messages.append({"role": "assistant", "content": response.content})
            
            # Check for tool usage
            tool_use = None
            for block in response.content:
                if block.type == "tool_use":
                    tool_use = block
                    break
            
            if tool_use:
                # Execute tool
                tool_name = tool_use.name
                tool_input = tool_use.input
                tool_result = ""
                
                print(f"  🛠️  Engineer Tool: {tool_name} ({tool_input})")
                
                if tool_name == "read_file":
                    tool_result = self.files.read_file(tool_input["path"])
                elif tool_name == "write_file":
                    tool_result = self.files.write_file(tool_input["path"], tool_input["content"])
                elif tool_name == "run_command":
                    tool_result = self.shell.run_command(tool_input["command"])
                
                # Add tool result to history
                messages.append({
                    "role": "user",
                    "content": [{
                        "type": "tool_result",
                        "tool_use_id": tool_use.id,
                        "content": str(tool_result)
                    }]
                })
            else:
                # No tool use means Agent is done or asking question
                # We assume done for this simple step execution
                return response.content[0].text

        return "Execution stopped (max turns reached)."

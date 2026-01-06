import re
import os
from dotenv import load_dotenv
from anthropic import Anthropic
from ..src.tools import TOOLS
from ..src.prompts import REACT_SYSTEM_PROMPT

load_dotenv()

class ReActAgent:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.max_steps = 10

    def run(self, question: str):
        print(f"🧩 Question: {question}")
        
        prompt = f"{REACT_SYSTEM_PROMPT}\nQuestion: {question}\n"
        
        for i in range(self.max_steps):
            # 1. 调用 LLM
            # 注意：实际生产中 context 可能很长，这里简化处理，直接拼接 string
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
                stop_sequences=["Observation:"] 
            )
            
            output = response.content[0].text
            # 补上被 stop_sequences 截断的换行符（如果有的话），保持美观
            print(f"---\nStep {i+1} Output:\n{output.strip()}")
            
            prompt += output
            
            # 2. 检查是否结束
            if "Final Answer:" in output:
                final_answer = output.split("Final Answer:")[-1].strip()
                print(f"\n✅ Result: {final_answer}")
                return final_answer

            # 3. 解析 Action
            # 正则匹配 Action: xxx \n Action Input: xxx
            # 允许 Action Input 跨行
            match = re.search(r"Action: ([\w_]+).*?Action Input: (.*)", output, re.DOTALL)
            
            if not match:
                # 容错：如果格式不对，告诉 LLM 重试
                print("⚠️  Warning: Failed to parse action. Asking LLM to correct.")
                prompt += "\nObservation: Invalid format. Please use 'Action:' followed by 'Action Input:'.\n"
                continue
                
            action_name = match.group(1).strip()
            action_input = match.group(2).strip()
            
            # 4. 执行工具
            if action_name not in TOOLS:
                result = f"Error: Tool '{action_name}' not found."
            else:
                try:
                    print(f"🛠️  Executing: {action_name}({action_input})")
                    result = TOOLS[action_name](action_input)
                except Exception as e:
                    result = f"Error executing tool: {str(e)}"
            
            print(f"🔍 Observation: {result}")
            
            # 5. 更新 Prompt
            prompt += f"\nObservation: {result}\n"
            
        print("❌ Reached max steps without final answer.")
        return None

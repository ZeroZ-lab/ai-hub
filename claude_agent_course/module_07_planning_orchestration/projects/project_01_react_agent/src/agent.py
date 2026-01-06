import re
import os
from dotenv import load_dotenv
from anthropic import Anthropic
from .tools import TOOLS
from .prompts import REACT_SYSTEM_PROMPT

load_dotenv()

class ReActAgent:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.max_steps = 10

    def run(self, question: str):
        print(f"🧩 Question: {question}")
        
        # 初始化 Prompt
        prompt = f"{REACT_SYSTEM_PROMPT}\nQuestion: {question}\n"
        
        for i in range(self.max_steps):
            # 1.调用 LLM
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
                stop_sequences=["Observation:"] # 🛑 关键：让模型在 Observation 前停下来
            )
            
            output = response.content[0].text
            print(f"---\nStep {i+1} LLM Output:\n{output}")
            
            # 将 LLM 的输出（Thought + Action）拼接到 Prompt 中
            prompt += output
            
            # 2. 解析 Action
            # TODO: 实现解析逻辑
            # 需要提取 action_name 和 action_input
            # 如果包含 "Final Answer:"，则返回结果并结束循环
            
            # 伪代码：
            # if "Final Answer:" in output:
            #     return output.split("Final Answer:")[1]
            
            # action_name, action_input = parse(output)
            
            # 3. 执行工具
            # result = TOOLS[action_name](action_input)
            # print(f"🔍 Observation: {result}")
            
            # 4. 更新 Prompt
            # prompt += f"Observation: {result}\n"
            
            # --- delete below when implementing ---
            print("❌ 你需要完成 agent.py 中的循环逻辑！")
            break 
            
        return "Agent failed to find an answer."

if __name__ == "__main__":
    agent = ReActAgent()
    # 这里的 prompt 包含了 history，实际使用时 history 越来越长

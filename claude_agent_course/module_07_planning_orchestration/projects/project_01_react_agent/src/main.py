from .agent import ReActAgent

def main():
    agent = ReActAgent()
    
    # 测试案例 1: 需要计算
    # question = "What is 15 * 12 + 4?"
    # agent.run(question)
    
    # 测试案例 2: 需要组合工具 (Word Length + Calculation)
    question = "Calculate the length of the word 'Anthropic' multiplied by 5."
    agent.run(question)

if __name__ == "__main__":
    main()

from .agent import ReActAgent

def main():
    agent = ReActAgent()
    question = "Calculate the length of the word 'Anthropic' multiplied by 5."
    agent.run(question)

if __name__ == "__main__":
    main()

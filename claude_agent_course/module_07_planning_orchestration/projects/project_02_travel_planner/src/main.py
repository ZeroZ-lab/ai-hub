from .planner import Planner
from .executor import Executor

def main():
    request = "Book a 3-day trip to Tokyo next Monday."
    
    # 1. Plan
    planner = Planner()
    plan = planner.create_plan(request)
    print(f"📋 Plan: {plan}")
    
    # 2. Execute
    executor = Executor()
    context = "" # 用来在步骤间传递信息（比如航班号）
    
    for i, step in enumerate(plan):
        print(f"\n--- Step {i+1}/{len(plan)} ---")
        result = executor.execute_step(step, context)
        
        # 将结果累积到上下文，供下一步参考
        context += f"\nStep: {step}\nResult: {result}\n"
        print(f"✅ Result: {result}")

    print("\n🎉 Trip Planning Completed!")

if __name__ == "__main__":
    main()

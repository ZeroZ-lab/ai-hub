"""
Resume Analyzer Solution Entry Point
"""

import asyncio
import os
from solution.agent import ResumeAnalyzer

async def main():
    """主函数"""
    print("=" * 60)
    print("📄 Resume Analyzer - 简历分析助手")
    print("=" * 60)
    print("\n命令: analyze <file>, match <file>, exit")
    print("=" * 60)

    try:
        async with ResumeAnalyzer() as agent:
            print("✅ 已连接到 Claude\n")

            while True:
                try:
                    user_input = input("\n💬 你: ").strip()
                    if not user_input:
                        continue
                    if user_input.lower() in ['exit', 'quit']:
                        break

                    parts = user_input.split(maxsplit=1)
                    command = parts[0].lower()
                    file_path = parts[1] if len(parts) > 1 else "data/sample_resume.txt"

                    if not os.path.exists(file_path):
                        print(f"❌ 文件不存在: {file_path}")
                        continue

                    with open(file_path, "r") as f:
                        resume_text = f.read()

                    print()
                    if command == "analyze":
                        print(f"🔍 分析: {file_path}\n")
                        await agent.analyze(resume_text)
                    elif command == "match":
                        reqs = input("职位要求技能（逗号分隔）: ").split(",")
                        reqs = [r.strip() for r in reqs if r.strip()]
                        print()
                        await agent.match_job(resume_text, reqs)
                    else:
                        print(f"未知命令: {command}")

                except KeyboardInterrupt:
                    print("\n\n⏸️ 中断...")
                    break

    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()

    print("\n👋 再见！")


if __name__ == "__main__":
    asyncio.run(main())

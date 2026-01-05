"""
Resume Analyzer - 主程序

Author: Claude Agent Course
"""

import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# TODO: 导入你实现的 ResumeAnalyzer
# from agent import ResumeAnalyzer


async def main():
    """主函数"""
    print("=" * 60)
    print("📄 Resume Analyzer - 简历分析助手")
    print("=" * 60)
    print("\n命令:")
    print("  analyze <file>  - 分析简历文件")
    print("  match <file>    - 匹配职位要求")
    print("  report <file>   - 生成分析报告")
    print("  exit            - 退出程序")
    print("=" * 60)

    # TODO: 初始化 ResumeAnalyzer
    # agent = ResumeAnalyzer()

    while True:
        try:
            user_input = input("\n💬 你: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 再见！")
                break

            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            file_path = parts[1] if len(parts) > 1 else "data/sample_resume.txt"

            # 读取简历文件
            if not os.path.exists(file_path):
                print(f"❌ 文件不存在: {file_path}")
                continue
            
            with open(file_path, "r") as f:
                resume_text = f.read()

            if command == "analyze":
                print(f"\n🔍 分析简历: {file_path}\n")
                # TODO: result = await agent.analyze(resume_text)
                print("⚠️ 请实现 analyze 方法")

            elif command == "match":
                print(f"\n🎯 匹配职位: {file_path}\n")
                requirements = input("请输入职位要求技能（逗号分隔）: ").split(",")
                # TODO: result = await agent.match_job(resume_text, requirements)
                print("⚠️ 请实现 match_job 方法")

            elif command == "report":
                print(f"\n📊 生成报告: {file_path}\n")
                # TODO: result = await agent.generate_report(resume_text)
                print("⚠️ 请实现 generate_report 方法")

            else:
                print(f"❓ 未知命令: {command}")

        except KeyboardInterrupt:
            print("\n\n👋 再见！")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")


if __name__ == "__main__":
    asyncio.run(main())

"""
Resume Analyzer - 参考答案 (简化版)

使用自定义工具分析简历。
注意：此版本移除了 can_use_tool 以简化运行。

Author: Claude Agent Course
"""

import asyncio
import os
import re
from dotenv import load_dotenv
from claude_agent_sdk import (
    tool,
    query,
    ClaudeAgentOptions,
    create_sdk_mcp_server
)

load_dotenv()


# ============ 自定义工具 ============

@tool("extract_contact", "Extract contact info from text", {"text": str})
async def extract_contact(args):
    text = args.get("text", "")
    
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    phone_pattern = r'1[3-9]\d{9}'
    
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    
    result = f"邮箱: {emails[0] if emails else '未找到'}\n"
    result += f"电话: {phones[0] if phones else '未找到'}"
    
    return {"content": [{"type": "text", "text": result}]}


@tool("extract_skills", "Extract skills from resume", {"text": str})
async def extract_skills(args):
    text = args.get("text", "").lower()
    
    skill_keywords = [
        "python", "javascript", "java", "go", "rust", "c++",
        "react", "vue", "angular", "node.js", "django", "flask",
        "docker", "kubernetes", "aws", "azure", "gcp",
        "sql", "mongodb", "redis", "postgresql",
        "git", "linux", "agile", "scrum"
    ]
    
    found_skills = [s for s in skill_keywords if s in text]
    return {"content": [{"type": "text", "text": f"技能: {', '.join(found_skills)}"}]}


@tool("calculate_match", "Calculate match score", {"skills": str, "requirements": str})
async def calculate_match(args):
    skills = set(s.strip().lower() for s in args.get("skills", "").split(",") if s.strip())
    requirements = set(r.strip().lower() for r in args.get("requirements", "").split(",") if r.strip())
    
    if not requirements:
        return {"content": [{"type": "text", "text": "未提供要求"}], "is_error": True}
    
    matched = skills & requirements
    score = len(matched) / len(requirements) * 100
    
    return {"content": [{"type": "text", "text": f"匹配度: {score:.0f}%，匹配: {', '.join(matched)}"}]}


class ResumeAnalyzer:
    """简历分析器 - 简化版"""

    def __init__(self):
        self.server = create_sdk_mcp_server(
            name="resume",
            version="1.0.0",
            tools=[extract_contact, extract_skills, calculate_match]
        )
        
        # 简化配置，不使用 can_use_tool
        self.options = ClaudeAgentOptions(
            mcp_servers={"resume": self.server},
            allowed_tools=[
                "mcp__resume__extract_contact",
                "mcp__resume__extract_skills",
                "mcp__resume__calculate_match"
            ]
        )

    async def analyze(self, resume_text: str) -> str:
        prompt = f"分析这份简历，提取关键信息：\n\n{resume_text}"
        
        result = []
        async for msg in query(prompt=prompt, options=self.options):
            if hasattr(msg, 'text'):
                result.append(msg.text)
            elif hasattr(msg, 'tool_name'):
                print(f"  🔧 {msg.tool_name}...")
        
        return "\n".join(result) if result else "分析失败"

    async def match_job(self, resume_text: str, requirements: list) -> str:
        prompt = f"""
        分析匹配度：
        简历：{resume_text[:500]}...
        要求：{', '.join(requirements)}
        """
        
        result = []
        async for msg in query(prompt=prompt, options=self.options):
            if hasattr(msg, 'text'):
                result.append(msg.text)
        return "\n".join(result)


async def main():
    print("=" * 60)
    print("📄 Resume Analyzer - 简历分析助手")
    print("=" * 60)
    print("\n命令: analyze <file>, match <file>, exit")
    print("=" * 60)

    agent = ResumeAnalyzer()

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

            if command == "analyze":
                print(f"\n🔍 分析: {file_path}\n")
                result = await agent.analyze(resume_text)
                print(result)
            elif command == "match":
                reqs = input("职位要求技能（逗号分隔）: ").split(",")
                result = await agent.match_job(resume_text, reqs)
                print(result)
            else:
                print(f"未知命令: {command}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")

    print("\n👋 再见！")


if __name__ == "__main__":
    asyncio.run(main())

"""
Resume Analyzer Tools
"""

import re
from claude_agent_sdk import tool

@tool("extract_contact", "Extract contact info from text", {"text": str})
async def extract_contact(args):
    """提取联系方式"""
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
    """提取技能列表"""
    text = args.get("text", "").lower()
    
    skill_keywords = [
        "python", "javascript", "java", "go", "rust", "c++",
        "react", "vue", "angular", "node.js", "django", "flask",
        "docker", "kubernetes", "aws", "azure", "gcp",
        "sql", "mongodb", "redis", "postgresql",
        "git", "linux", "agile", "scrum"
    ]
    
    found_skills = [s for s in skill_keywords if s in text]
    return {"content": [{"type": "text", "text": f"技能: {', '.join(found_skills) if found_skills else '未识别到'}"}]}


@tool("calculate_match", "Calculate match score", {"skills": str, "requirements": str})
async def calculate_match(args):
    """计算匹配度"""
    skills = set(s.strip().lower() for s in args.get("skills", "").split(",") if s.strip())
    requirements = set(r.strip().lower() for r in args.get("requirements", "").split(",") if r.strip())
    
    if not requirements:
        return {"content": [{"type": "text", "text": "未提供要求"}], "is_error": True}
    
    matched = skills & requirements
    score = len(matched) / len(requirements) * 100 if requirements else 0
    
    return {"content": [{"type": "text", "text": f"匹配度: {score:.0f}%，匹配: {', '.join(matched) if matched else '无'}"}]}

"""
Resume Analyzer - 自定义工具

TODO: 实现简历分析相关的自定义工具

Author: Claude Agent Course
"""

from claude_agent_sdk import tool


# TODO: 实现 extract_contact 工具
@tool("extract_contact", "Extract contact information from text", {"text": str})
async def extract_contact(args):
    """提取联系方式
    
    TODO: 使用正则表达式提取邮箱、电话等
    """
    text = args.get("text", "")
    
    # 示例实现 - 你可以改进它
    import re
    
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    phone_pattern = r'1[3-9]\d{9}'
    
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    
    result = f"邮箱: {emails[0] if emails else '未找到'}\n"
    result += f"电话: {phones[0] if phones else '未找到'}"
    
    return {"content": [{"type": "text", "text": result}]}


# TODO: 实现 extract_skills 工具
@tool("extract_skills", "Extract skills from resume text", {"text": str})
async def extract_skills(args):
    """提取技能列表
    
    TODO: 识别常见技能关键词
    """
    text = args.get("text", "").lower()
    
    # 常见技能关键词
    skill_keywords = [
        "python", "javascript", "java", "go", "rust", "c++",
        "react", "vue", "angular", "node.js", "django", "flask",
        "docker", "kubernetes", "aws", "azure", "gcp",
        "sql", "mongodb", "redis", "postgresql",
        "git", "linux", "agile", "scrum"
    ]
    
    found_skills = [s for s in skill_keywords if s in text]
    
    if found_skills:
        return {"content": [{"type": "text", "text": f"技能: {', '.join(found_skills)}"}]}
    else:
        return {"content": [{"type": "text", "text": "未识别到技能关键词"}]}


# TODO: 实现 calculate_match 工具
@tool("calculate_match", "Calculate match score between resume and requirements", 
      {"skills": str, "requirements": str})
async def calculate_match(args):
    """计算匹配度
    
    TODO: 计算简历技能与职位要求的匹配程度
    """
    skills = set(args.get("skills", "").lower().split(","))
    requirements = set(args.get("requirements", "").lower().split(","))
    
    skills = {s.strip() for s in skills if s.strip()}
    requirements = {r.strip() for r in requirements if r.strip()}
    
    if not requirements:
        return {"content": [{"type": "text", "text": "未提供职位要求"}], "is_error": True}
    
    matched = skills & requirements
    score = len(matched) / len(requirements) * 100
    
    result = f"匹配度: {score:.1f}%\n"
    result += f"匹配的技能: {', '.join(matched) if matched else '无'}\n"
    result += f"缺少的技能: {', '.join(requirements - skills) if requirements - skills else '无'}"
    
    return {"content": [{"type": "text", "text": result}]}


# 导出工具列表
TOOLS = [extract_contact, extract_skills, calculate_match]

"""
Resume Analyzer - Agent 实现

TODO: 实现 ResumeAnalyzer 类

Author: Claude Agent Course
"""

from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    create_sdk_mcp_server
)

from tools import TOOLS


# 结构化输出 Schema
RESUME_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "description": "候选人姓名"},
        "email": {"type": "string", "description": "邮箱地址"},
        "phone": {"type": "string", "description": "电话号码"},
        "skills": {
            "type": "array",
            "items": {"type": "string"},
            "description": "技能列表"
        },
        "experience_years": {"type": "integer", "description": "工作年限"},
        "education": {"type": "string", "description": "最高学历"},
        "summary": {"type": "string", "description": "简历摘要"}
    },
    "required": ["name", "skills"]
}


class ResumeAnalyzer:
    """简历分析 Agent"""

    def __init__(self):
        """初始化 Agent"""
        # TODO: 创建工具服务器
        self.server = create_sdk_mcp_server(
            name="resume",
            version="1.0.0",
            tools=TOOLS
        )
        
        # TODO: 配置选项
        self.options = ClaudeAgentOptions(
            mcp_servers={"resume": self.server},
            allowed_tools=[
                "mcp__resume__extract_contact",
                "mcp__resume__extract_skills",
                "mcp__resume__calculate_match"
            ]
        )
        
        # 结构化输出选项
        self.structured_options = ClaudeAgentOptions(
            mcp_servers={"resume": self.server},
            allowed_tools=[
                "mcp__resume__extract_contact",
                "mcp__resume__extract_skills"
            ],
            output_format={
                "type": "json_schema",
                "schema": RESUME_SCHEMA
            },
            max_turns=3
        )

    async def analyze(self, resume_text: str) -> dict:
        """分析简历，返回结构化数据
        
        Args:
            resume_text: 简历文本
            
        Returns:
            结构化的简历信息
        """
        prompt = f"""
        请分析以下简历，提取关键信息：
        
        {resume_text}
        
        使用提供的工具提取联系方式和技能，然后返回结构化结果。
        """
        
        result = {}
        async for msg in query(prompt=prompt, options=self.structured_options):
            if hasattr(msg, 'structured_output'):
                result = msg.structured_output
            elif hasattr(msg, 'text'):
                print(f"Agent: {msg.text}")
            elif hasattr(msg, 'tool_name'):
                print(f"  🔧 {msg.tool_name}...")
        
        return result

    async def match_job(self, resume_text: str, requirements: list) -> str:
        """匹配职位要求
        
        Args:
            resume_text: 简历文本
            requirements: 职位要求技能列表
            
        Returns:
            匹配分析结果
        """
        req_str = ", ".join(requirements)
        
        prompt = f"""
        请分析以下简历与职位要求的匹配程度：
        
        ## 简历
        {resume_text}
        
        ## 职位要求技能
        {req_str}
        
        步骤：
        1. 使用 extract_skills 工具提取简历中的技能
        2. 使用 calculate_match 工具计算匹配度
        3. 给出招聘建议
        """
        
        result = []
        async for msg in query(prompt=prompt, options=self.options):
            if hasattr(msg, 'text'):
                result.append(msg.text)
            elif hasattr(msg, 'tool_name'):
                print(f"  🔧 {msg.tool_name}...")
        
        return "\n".join(result)

    async def generate_report(self, resume_text: str) -> str:
        """生成分析报告
        
        Args:
            resume_text: 简历文本
            
        Returns:
            Markdown 格式的分析报告
        """
        prompt = f"""
        请为以下简历生成一份详细的分析报告：
        
        {resume_text}
        
        报告格式：
        
        # 候选人分析报告
        
        ## 基本信息
        - 姓名:
        - 联系方式:
        
        ## 技能分析
        - 核心技能:
        - 技能等级评估:
        
        ## 综合评价
        - 优势:
        - 建议:
        
        请使用工具提取信息，然后生成报告。
        """
        
        result = []
        async for msg in query(prompt=prompt, options=self.options):
            if hasattr(msg, 'text'):
                result.append(msg.text)
        
        return "\n".join(result)

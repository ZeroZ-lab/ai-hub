"""
File Analyzer - Agent 实现

TODO: 实现 FileAnalyzer 类

学习要点：
1. 使用 ClaudeAgentOptions 配置工具
2. 使用 query() 发送请求
3. 处理工具调用结果

Author: Claude Agent Course
Date: 2024-01-04
"""

from claude_agent_sdk import query, ClaudeAgentOptions


class FileAnalyzer:
    """文件分析器 Agent
    
    使用 Read 和 Bash 工具分析项目文件结构。
    """

    def __init__(self):
        """初始化 Agent"""
        # TODO: 配置 ClaudeAgentOptions
        # 提示：启用 Read 和 Bash 工具
        self.options = ClaudeAgentOptions(
            allowed_tools=["Read", "Bash"],
            permission_mode='acceptEdits'
        )

    async def scan_directory(self, path: str = ".") -> str:
        """扫描目录结构
        
        Args:
            path: 要扫描的目录路径
            
        Returns:
            目录结构描述
        """
        # TODO: 实现目录扫描
        # 提示：
        # 1. 构造 prompt，让 Agent 使用 Bash 执行 find 或 ls 命令
        # 2. 使用 async for 遍历 query() 的结果
        # 3. 收集并返回 Agent 的回复
        
        prompt = f"""
        请分析目录 {path} 的结构：
        1. 使用 ls -la 或 find 命令列出所有文件
        2. 按文件类型分类（目录、Python、Markdown 等）
        3. 返回结构化的文件列表
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
        
        return "\n".join(result)

    async def count_lines(self, path: str = ".") -> str:
        """统计代码行数
        
        Args:
            path: 要统计的目录路径
            
        Returns:
            代码行数统计
        """
        # TODO: 实现代码行数统计
        # 提示：使用 wc -l 命令
        
        prompt = f"""
        统计 {path} 目录下的代码行数：
        1. 找出所有代码文件 (.py, .js, .ts, .go 等)
        2. 使用 wc -l 统计每个文件的行数
        3. 按语言类型汇总
        4. 返回统计结果
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
        
        return "\n".join(result)

    async def generate_report(self, path: str = ".") -> str:
        """生成项目报告
        
        Args:
            path: 要分析的目录路径
            
        Returns:
            Markdown 格式的项目报告
        """
        # TODO: 实现项目报告生成
        # 提示：综合使用 Read 和 Bash 工具
        
        prompt = f"""
        为 {path} 生成一份 Markdown 格式的项目报告：
        
        1. 首先使用 ls -la 查看目录结构
        2. 读取 README.md（如果存在）了解项目概述
        3. 统计代码文件行数
        4. 生成包含以下内容的报告：
        
        ## 项目概述
        （根据 README.md 或目录结构推断）
        
        ## 目录结构
        （文件列表）
        
        ## 代码统计
        （按语言统计行数）
        
        ## 主要文件说明
        （解释关键文件的作用）
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
        
        return "\n".join(result)

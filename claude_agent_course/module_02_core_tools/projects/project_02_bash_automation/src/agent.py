"""
Bash Automation - Agent 实现

TODO: 实现 BashAutomation 类

学习要点：
1. 使用 Bash 工具执行命令
2. 实现安全检查阻止危险命令
3. 解析命令输出

Author: Claude Agent Course
Date: 2024-01-04
"""

from claude_agent_sdk import (
    query, 
    ClaudeAgentOptions,
    PermissionResultAllow,
    PermissionResultDeny
)

# 安全配置
ALLOWED_COMMANDS = [
    "git", "ls", "cat", "head", "tail", "wc", "grep",
    "pwd", "echo", "date", "which", "uname",
    "python", "node", "npm", "docker"
]

DANGEROUS_PATTERNS = [
    "rm -rf", "rm -r", "sudo", "chmod 777",
    "mkfs", "dd if=", "> /dev", "eval"
]


class BashAutomation:
    """Bash 自动化助手 Agent
    
    使用 Bash 工具执行和自动化开发任务。
    """

    def __init__(self):
        """初始化 Agent"""
        self.options = ClaudeAgentOptions(
            allowed_tools=["Bash"],
            permission_mode='acceptEdits',
            can_use_tool=self.security_check
        )
        self.command_history = []

    async def security_check(self, tool_name: str, tool_input: dict, context):
        """安全检查
        
        TODO: 实现安全检查逻辑
        提示：
        1. 检查命令是否在白名单
        2. 检查是否包含危险模式
        """
        if tool_name != "Bash":
            return PermissionResultAllow(behavior="allow")
        
        command = tool_input.get("command", "")
        
        # 检查危险模式
        for pattern in DANGEROUS_PATTERNS:
            if pattern in command:
                print(f"⚠️ 阻止危险命令: {command}")
                return PermissionResultDeny(
                    behavior="deny",
                    message=f"命令包含危险模式: {pattern}"
                )
        
        # 检查白名单（宽松模式）
        allowed = any(command.startswith(cmd) for cmd in ALLOWED_COMMANDS)
        if not allowed:
            # 对于版本检查命令也允许
            if "--version" in command or "-v" in command:
                return PermissionResultAllow(behavior="allow")
            
            print(f"⚠️ 命令不在白名单: {command}")
            return PermissionResultDeny(
                behavior="deny",
                message="命令不在白名单中"
            )
        
        # 记录命令历史
        self.command_history.append(command)
        return PermissionResultAllow(behavior="allow")

    async def run_git_command(self, git_args: str) -> str:
        """执行 Git 命令并解读结果"""
        # TODO: 实现 Git 命令执行
        
        prompt = f"""
        执行以下 Git 命令并解读结果：
        git {git_args}
        
        请：
        1. 执行命令
        2. 用中文解读输出内容
        3. 如果有需要注意的地方，给出建议
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
        
        return "\n".join(result)

    async def check_environment(self) -> str:
        """检查开发环境"""
        # TODO: 实现环境检查
        
        prompt = """
        检查当前开发环境，执行以下检查：
        
        1. python --version 或 python3 --version
        2. node --version (如果有)
        3. npm --version (如果有)
        4. git --version
        5. docker --version (如果有)
        
        对于每个工具：
        - 如果存在，显示版本号 ✅
        - 如果不存在，标记为 ❌ 未安装
        
        最后给出环境总结。
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
        
        return "\n".join(result)

    async def analyze_logs(self, log_file: str) -> str:
        """分析日志文件"""
        # TODO: 实现日志分析
        
        prompt = f"""
        分析日志文件 {log_file}：
        
        1. 使用 tail -100 {log_file} 查看最近的日志
        2. 使用 grep -c "ERROR" {log_file} 统计错误数量
        3. 使用 grep -c "WARN" {log_file} 统计警告数量
        
        生成分析报告：
        - 错误数量
        - 警告数量
        - 最近的几条错误信息
        - 建议
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
        
        return "\n".join(result)

    async def execute_command(self, command: str) -> str:
        """执行自定义命令"""
        # TODO: 实现命令执行
        
        prompt = f"""
        执行以下命令：
        {command}
        
        请：
        1. 执行命令
        2. 显示输出
        3. 简要解释结果
        """
        
        result = []
        async for message in query(prompt=prompt, options=self.options):
            if hasattr(message, 'text'):
                result.append(message.text)
        
        return "\n".join(result)

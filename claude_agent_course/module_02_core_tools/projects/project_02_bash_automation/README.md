# Bash Automation - Bash 自动化助手

> **难度**: 🌟🌟 中级
> **预计时间**: 60-90 分钟

---

## 项目背景

本项目是 Module 2 的第二个实战项目，你将学习如何使用 Claude Agent SDK 的 **Bash** 工具来自动化常见的开发任务。

**示例场景**：
> 作为开发者，你经常需要执行重复性的命令（检查 Git 状态、查看日志、运行测试）。你让 Agent 帮你自动化这些任务。

---

## 学习目标

完成本项目后，你将能够：
- [ ] 使用 `Bash` 工具执行系统命令
- [ ] 解析命令输出并提取关键信息
- [ ] 实现命令安全检查，阻止危险操作
- [ ] 创建自动化工作流

---

## 功能需求

### 必做功能 (Core)

#### 1. Git 助手
- 输入：Git 相关指令
- 输出：执行结果和解读
- 示例：
  ```
  你: git status
  Agent: 仓库状态：
  - 分支: main
  - 未暂存的更改: 2 个文件
  - 未跟踪的文件: 1 个
  建议: 运行 git add 添加更改
  ```

#### 2. 环境检查
- 输入：检查环境命令
- 输出：环境信息汇总
- 示例：
  ```
  你: check env
  Agent: 开发环境检查：
  ✅ Python: 3.11.5
  ✅ Node.js: 18.17.0
  ✅ Git: 2.42.0
  ⚠️ Docker: 未安装
  ```

#### 3. 日志分析
- 输入：日志文件路径
- 输出：错误和警告统计
- 示例：
  ```
  你: analyze logs server.log
  Agent: 日志分析结果：
  - 错误 (ERROR): 12 条
  - 警告 (WARN): 45 条
  - 最近错误: "Database connection timeout"
  ```

### 选做功能 (Advanced)

- [ ] **进阶 1**：批量执行命令序列
- [ ] **进阶 2**：定时任务调度
- [ ] **进阶 3**：生成执行报告

---

## 技术要点

### 使用的工具
```python
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    allowed_tools=["Bash"],  # 只启用 Bash 工具
    permission_mode='acceptEdits'
)
```

### 安全检查（重点）
```python
# 阻止危险命令
DANGEROUS_COMMANDS = [
    "rm -rf", "rm -r", "sudo",
    "chmod 777", "mkfs", "dd if="
]

async def can_use_tool(tool_name, tool_input, context):
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        for pattern in DANGEROUS_COMMANDS:
            if pattern in command:
                return PermissionResultDeny(...)
    return PermissionResultAllow(...)
```

---

## 实现步骤

### 第一步：创建 BashAutomation 类

```python
class BashAutomation:
    def __init__(self):
        self.options = ClaudeAgentOptions(
            allowed_tools=["Bash"],
            can_use_tool=self.security_check
        )
    
    async def security_check(self, tool_name, tool_input, context):
        """安全检查"""
        pass
    
    async def run_git_command(self, command: str) -> str:
        """执行 Git 命令"""
        pass
    
    async def check_environment(self) -> str:
        """检查开发环境"""
        pass
    
    async def analyze_logs(self, log_file: str) -> str:
        """分析日志文件"""
        pass
```

### 第二步：实现安全检查

```python
ALLOWED_COMMANDS = [
    "git", "ls", "cat", "head", "tail", "wc",
    "pwd", "echo", "date", "python --version",
    "node --version", "npm --version"
]

async def security_check(self, tool_name, tool_input, context):
    command = tool_input.get("command", "")
    
    # 检查是否在白名单
    allowed = any(command.startswith(cmd) for cmd in ALLOWED_COMMANDS)
    if not allowed:
        return PermissionResultDeny(
            behavior="deny",
            message="命令不在白名单中"
        )
    
    return PermissionResultAllow(behavior="allow")
```

### 第三步：实现 Git 助手

```python
async def run_git_command(self, command: str) -> str:
    prompt = f"""
    执行以下 Git 命令并解读结果：
    {command}
    
    请：
    1. 执行命令
    2. 用中文解读输出
    3. 如有需要，给出后续建议
    """
    # TODO: 实现
```

---

## 测试方法

### 运行项目
```bash
cd claude_agent_course/module_02_core_tools/projects/project_02_bash_automation
uv sync
uv run python src/main.py
```

### 测试用例

#### 测试 1：Git 状态
```
你: git status
预期: 显示仓库状态并解读
```

#### 测试 2：环境检查
```
你: check
预期: 显示开发环境版本信息
```

#### 测试 3：安全拦截
```
你: rm -rf /
预期: 命令被拦截，显示警告
```

---

## 完成标准

### ✅ 基础版（60 分）
- [ ] 能执行基本的系统命令
- [ ] 实现了命令安全检查
- [ ] Git 助手基本功能

### ✅ 良好版（80 分）
- [ ] 基础版 + 环境检查功能
- [ ] 命令输出有清晰的解读
- [ ] 代码有注释

### ✅ 优秀版（100 分）
- [ ] 良好版 + 日志分析功能
- [ ] 支持命令历史记录
- [ ] 有完整的用户交互

---

## 项目结构

```
project_02_bash_automation/
├── README.md
├── pyproject.toml
├── .env.example
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
├── tests/
│   └── test_agent.py
└── solution/
    └── main.py
```

---

## 参考资源

- [Module 2 概念讲解](../../docs/01_概念讲解.md)
- [Module 2 代码示例](../../docs/02_代码示例.md)
- [Module 2 最佳实践](../../docs/03_最佳实践.md)

---

**开始构建你的 Bash 自动化助手吧！💻**

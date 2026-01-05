# File Analyzer - 文件分析器

> **难度**: 🌟🌟 中级
> **预计时间**: 60-90 分钟

---

## 项目背景

本项目是 Module 2 的第一个实战项目，你将学习如何使用 Claude Agent SDK 的 **Read** 工具来分析项目文件结构和代码。

**示例场景**：
> 作为开发者，你想快速了解一个新项目的结构。你让 Agent 扫描目录、分析代码文件、生成项目报告。

---

## 学习目标

完成本项目后，你将能够：
- [ ] 使用 `Read` 工具读取文件内容
- [ ] 使用 `Bash` 工具执行目录扫描命令
- [ ] 实现权限控制，保护敏感文件
- [ ] 生成结构化的分析报告

---

## 功能需求

### 必做功能 (Core)

#### 1. 目录扫描
- 输入：目录路径
- 输出：文件列表（文件名、类型、大小）
- 示例：
  ```
  你: 扫描当前目录
  Agent: 发现 12 个文件：
  - main.py (Python, 2.3KB)
  - README.md (Markdown, 1.1KB)
  - src/ (目录, 5 个文件)
  ...
  ```

#### 2. 代码统计
- 输入：目录路径
- 输出：代码行数统计
- 示例：
  ```
  代码统计：
  - Python: 450 行 (3 个文件)
  - JavaScript: 120 行 (2 个文件)
  - 总计: 570 行
  ```

#### 3. 项目报告
- 输入：目录路径
- 输出：Markdown 格式的项目报告
- 包含：项目结构树、文件统计、主要文件描述

### 选做功能 (Advanced)

- [ ] **进阶 1**：识别项目类型（Python/Node/Go 等）
- [ ] **进阶 2**：分析代码复杂度
- [ ] **进阶 3**：生成依赖关系图

---

## 技术要点

### 使用的工具
```python
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    allowed_tools=["Read", "Bash"],  # 读取文件 + 执行命令
    permission_mode='acceptEdits'
)
```

### 核心 Bash 命令
```bash
# 列出文件
find . -type f -name "*.py"

# 统计行数
wc -l *.py

# 显示目录结构
tree -L 2
```

---

## 实现步骤

### 第一步：创建基础 Agent

在 `src/agent.py` 中实现 `FileAnalyzer` 类：

```python
# TODO: 实现 FileAnalyzer 类
class FileAnalyzer:
    def __init__(self):
        self.options = ClaudeAgentOptions(
            allowed_tools=["Read", "Bash"]
        )
    
    async def scan_directory(self, path: str) -> str:
        """扫描目录结构"""
        pass
    
    async def count_lines(self, path: str) -> dict:
        """统计代码行数"""
        pass
    
    async def generate_report(self, path: str) -> str:
        """生成项目报告"""
        pass
```

### 第二步：实现目录扫描

```python
async def scan_directory(self, path: str) -> str:
    prompt = f"""
    请分析目录 {path} 的结构：
    1. 使用 find 或 ls 命令列出所有文件
    2. 按文件类型分类
    3. 返回结构化的文件列表
    """
    # TODO: 实现
```

### 第三步：实现代码统计

```python
async def count_lines(self, path: str) -> dict:
    prompt = f"""
    统计 {path} 目录下的代码行数：
    1. 找出所有代码文件 (.py, .js, .go 等)
    2. 使用 wc -l 统计每个文件
    3. 按语言汇总并返回
    """
    # TODO: 实现
```

### 第四步：生成报告

```python
async def generate_report(self, path: str) -> str:
    prompt = f"""
    为 {path} 生成一份 Markdown 格式的项目报告：
    
    报告应包含：
    ## 项目概述
    ## 目录结构
    ## 代码统计
    ## 主要文件说明
    """
    # TODO: 实现
```

---

## 测试方法

### 运行项目
```bash
cd claude_agent_course/module_02_core_tools/projects/project_01_file_analyzer
uv sync
uv run python src/main.py
```

### 测试用例

#### 测试 1：目录扫描
```
你: scan .
预期: 显示当前目录的文件列表
```

#### 测试 2：代码统计
```
你: count
预期: 显示代码行数统计
```

#### 测试 3：生成报告
```
你: report
预期: 生成 Markdown 报告并保存
```

---

## 完成标准

### ✅ 基础版（60 分）
- [ ] 能扫描目录并列出文件
- [ ] 能统计代码行数
- [ ] 代码有基本错误处理

### ✅ 良好版（80 分）
- [ ] 基础版 + 生成 Markdown 报告
- [ ] 实现了权限控制（保护 .env 等敏感文件）
- [ ] 代码结构清晰，有注释

### ✅ 优秀版（100 分）
- [ ] 良好版 + 至少一个进阶功能
- [ ] 有完整的用户交互界面
- [ ] 有测试用例

---

## 项目结构

```
project_01_file_analyzer/
├── README.md              # 本文件
├── pyproject.toml         # 依赖配置
├── .env.example           # 环境变量示例
├── src/
│   ├── __init__.py
│   ├── main.py           # 主程序入口
│   └── agent.py          # FileAnalyzer 实现
├── tests/
│   └── test_agent.py     # 测试
└── solution/
    ├── main.py           # 参考答案
    └── agent.py
```

---

## 参考资源

- [Module 2 概念讲解](../../docs/01_概念讲解.md)
- [Module 2 代码示例](../../docs/02_代码示例.md)
- [Module 2 最佳实践](../../docs/03_最佳实践.md)

---

**开始构建你的文件分析器吧！📂**

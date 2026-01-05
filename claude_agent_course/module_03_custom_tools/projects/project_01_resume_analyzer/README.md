# Resume Analyzer - 简历分析助手

> **难度**: 🌟🌟🌟 中高级
> **预计时间**: 90-120 分钟

---

## 项目背景

使用**自定义工具**和**结构化输出**构建一个简历分析助手，能够解析简历文本并提取关键信息。

---

## 学习目标

- [ ] 使用 `@tool` 装饰器创建自定义工具
- [ ] 使用 `create_sdk_mcp_server` 注册工具
- [ ] 配置 JSON Schema 获取结构化输出
- [ ] 实现完整的简历分析流程

---

## 功能需求

### 必做功能

#### 1. 解析简历
- 输入：简历文本
- 输出：结构化 JSON（姓名、邮箱、技能、经验）

#### 2. 技能匹配
- 输入：简历 + 职位要求
- 输出：匹配度评分

#### 3. 生成报告
- 生成候选人分析报告

---

## 技术要点

### 自定义工具

```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("extract_contact", "Extract contact info", {"text": str})
async def extract_contact(args):
    # 提取联系方式
    ...

@tool("extract_skills", "Extract skills", {"text": str})
async def extract_skills(args):
    # 提取技能
    ...

server = create_sdk_mcp_server(
    name="resume",
    version="1.0.0",
    tools=[extract_contact, extract_skills]
)
```

### 结构化输出

```python
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "skills": {"type": "array", "items": {"type": "string"}},
        "experience_years": {"type": "integer"}
    },
    "required": ["name", "skills"]
}

options = ClaudeAgentOptions(
    output_format={"type": "json_schema", "schema": schema}
)
```

---

## 实现步骤

### 第一步：创建自定义工具

在 `src/tools.py` 中定义工具：

```python
# TODO: 实现以下工具
# - extract_contact: 提取联系方式
# - extract_skills: 提取技能列表
# - calculate_match: 计算匹配度
```

### 第二步：创建 Agent

在 `src/agent.py` 中：

```python
class ResumeAnalyzer:
    def __init__(self):
        # TODO: 创建工具服务器
        # TODO: 配置选项
        pass
    
    async def analyze(self, resume_text: str) -> dict:
        # TODO: 分析简历
        pass
    
    async def match(self, resume: dict, requirements: list) -> float:
        # TODO: 计算匹配度
        pass
```

### 第三步：添加结构化输出

配置 JSON Schema 确保输出格式统一。

---

## 测试方法

```bash
cd claude_agent_course/module_03_custom_tools/projects/project_01_resume_analyzer
uv sync
uv run python src/main.py
```

### 测试用例

```
你: analyze data/sample_resume.txt
Agent: {
  "name": "张三",
  "email": "zhangsan@example.com",
  "skills": ["Python", "JavaScript"],
  "experience_years": 5
}
```

---

## 完成标准

### ✅ 基础版（60 分）
- [ ] 实现至少 2 个自定义工具
- [ ] 能解析简历基本信息

### ✅ 良好版（80 分）
- [ ] 实现结构化输出
- [ ] 有技能匹配功能

### ✅ 优秀版（100 分）
- [ ] 完整的分析报告
- [ ] 代码结构清晰

---

## 项目结构

```
project_01_resume_analyzer/
├── README.md
├── pyproject.toml
├── .env.example
├── data/
│   └── sample_resume.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   └── tools.py
└── solution/
    └── main.py
```

---

**开始构建你的简历分析助手！📄**

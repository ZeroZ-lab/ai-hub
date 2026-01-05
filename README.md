# Claude Agent SDK 实战课程

一个通过**循序渐进 (Step-by-Step)** 的方式，教你从零掌握 Claude Agent SDK 的实战课程。

---

## 🚀 快速开始

### 新手入门（5分钟）

1. **查看课程大纲**：[课程结构](#课程结构)
2. **准备开发环境**：[环境配置](#环境配置)
3. **开始学习**：从 [Module 1](claude_agent_course/module_01_foundations/) 开始

### 内容创作者

- 📖 **阅读开发指南**：[CONTRIBUTING.md](CONTRIBUTING.md)
- 🎨 **使用模板创建内容**：[templates/](templates/)

---

## 📚 课程结构

### Phase 1: 觉醒 (Awakening) - 基础与原理

#### [Module 1: Agent 思维导论](claude_agent_course/module_01_foundations/) ✅ 进行中
- 🎯 理解 Agent 核心概念
- 🛠️ 搭建开发环境
- 💻 运行第一个 Hello World
- 📁 **项目**: Hello Agent、智能对话助手

#### [Module 2: 基础工具](claude_agent_course/module_02_core_tools/) ✅ 进行中
- 📂 文件系统操作
- 💻 Bash 命令执行
- 🌐 Web 工具（搜索、抓取）
- 📁 **项目**: 文件分析器、Bash 自动化助手

---

### Phase 2: 连接 (Connection) - 工具与协议

#### [Module 3: 自定义工具](claude_agent_course/module_03_custom_tools/) ✅ 进行中
- ⚙️ Function Calling 原理
- 📊 结构化输出
- 🔧 自定义工具开发
- 📁 **项目**: 简历分析助手

#### [Module 4: MCP 协议](claude_agent_course/module_04_mcp_protocol/) 🚧 待开发
- 🔌 Model Context Protocol 架构
- 🗄️ 数据库连接
- 📁 **项目**: Text-to-SQL 自然语言数据分析

---

### Phase 3: 智慧 (Intelligence) - 复杂工作流

#### [Module 5: 记忆与上下文](claude_agent_course/module_05_memory_context/) 🚧 待开发
- 💾 Session 管理
- ⚡ Prompt Caching
- 🧠 长期记忆（RAG 初探）
- 📁 **项目**: 带记忆的 Agent

#### [Module 6: 规划与编排](claude_agent_course/module_06_planning_orchestration/) 🚧 待开发
- 🤔 Chain of Thought (CoT)
- 🔄 ReAct 模式
- 👥 Human-in-the-loop
- 📁 **项目**: 交互式代码重构助手

---

### Phase 4: 飞升 (Ascension) - 综合大项目

#### [Module 7: Capstone Project](claude_agent_course/module_07_capstone_project/) 🚧 待开发
- 🚀 全栈研发助手 "DevMate"
- 📁 **功能**: GitHub Issue 监控、代码理解、自动修复、PR 生成

---

## 🛠️ 环境配置

### 前置要求
- **Python**: 3.10 或更高版本
- **包管理器**: `uv`（推荐）或 `pip`

### 快速配置（使用 uv）

```bash
# 1. 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 克隆仓库
git clone https://github.com/your-repo/ai-hub.git
cd ai-hub

# 3. 进入任意模块
cd claude_agent_course/module_01_foundations

# 4. 安装依赖
uv sync

# 5. 配置 API Key
cp .env.example .env
# 编辑 .env，填入 ANTHROPIC_API_KEY

# 6. 运行示例
uv run python examples/hello.py
```

**详细说明**: 查看 [CONTRIBUTING.md](CONTRIBUTING.md#环境配置)

---

## 📖 学习路径

### 推荐顺序
```
Module 1 → Module 2 → Module 3 → Module 4 → Module 5 → Module 6 → Module 7
```

### 跳过式学习
- 只想快速上手：**Module 1 + Module 2**
- 想做数据分析：**Module 1 → Module 4**
- 想做复杂应用：**Module 1 → Module 6 → Module 7**

---

## 🎯 适用人群

- ✅ 希望提升开发效率的软件工程师
- ✅ 想构建垂直领域 AI 助手的创业者
- ✅ 对 AI Agent 架构感兴趣的技术爱好者

### 先修知识
- Python 基础语法
- 了解 API 的基本概念
- 基本的命令行操作

---

## 💡 技术栈

- **语言**: Python 3.10+
- **核心库**: `anthropic` (Claude API)
- **协议**: Model Context Protocol (MCP)
- **包管理**: `uv`（推荐）

---

## 📂 项目结构

```
ai-hub/
├── README.md                    # 本文件
├── CONTRIBUTING.md              # 开发指南（创建内容必读）
├── .gitignore
│
├── templates/                   # 📝 模板文件（创建新内容时使用）
│   ├── docs_template_*.md
│   ├── project_README_template.md
│   ├── pyproject.toml
│   └── ...
│
└── claude_agent_course/         # 📚 课程内容
    ├── module_01_foundations/
    ├── module_02_core_tools/
    ├── ...
    └── module_07_capstone_project/
```

---

## 🤝 贡献指南

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解：

- 如何创建新模块
- 如何添加实战项目
- 代码规范和质量标准
- 使用 uv 的工作流程

---

## 📜 许可证

[MIT License](LICENSE)

---

## 🔗 相关资源

- [Anthropic 官方文档](https://docs.anthropic.com)
- [Claude API 参考](https://docs.anthropic.com/claude/reference)
- [uv 包管理器文档](https://docs.astral.sh/uv/)

---

## ❓ 常见问题

### Q: 需要付费吗？
A: 课程内容免费，但使用 Claude API 需要 Anthropic 账号和 API 额度（有免费试用）。

### Q: 完成课程需要多久？
A:
- 快速通关：20-30 小时（只完成核心功能）
- 深度学习：40-60 小时（包含所有进阶项目）

### Q: 遇到问题怎么办？
A:
1. 查看模块中的 `docs/03_最佳实践.md`
2. 查看项目的 `solution/` 参考答案
3. 提交 [GitHub Issue](https://github.com/your-repo/ai-hub/issues)

---

**开始你的 AI Agent 开发之旅吧！🚀**

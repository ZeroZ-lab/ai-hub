# Module 02 - Core Tools (核心工具)

## 模块概述

本模块深入讲解如何让 AI Agent 使用**核心工具**（Core Tools）来与系统交互，包括文件操作和 Bash 命令执行。这些是构建实用 Agent 的基础能力。

## 学习目标

完成本模块后，你将能够：

1. ✅ 理解 Claude Agent SDK 的工具系统架构
2. ✅ 让 Agent 读取、写入、搜索文件
3. ✅ 让 Agent 执行 Bash 命令并处理输出
4. ✅ 实现文件分析器和自动化脚本
5. ✅ 掌握工具调用的最佳实践和安全考虑

## 核心概念

### 1. 工具系统 (Tool System)

Claude Agent SDK 提供了一套工具系统，让 Agent 能够：
- **感知环境**：读取文件、列出目录
- **修改环境**：写入文件、执行命令
- **获取反馈**：解析命令输出、处理错误

### 2. 内置核心工具

- **File Tools**：`read_file`, `write_file`, `list_directory`, `search_files`
- **Bash Tools**：`execute_bash`
- **Utility Tools**：`get_current_time`, `get_environment_variable`

### 3. 工具调用流程

```
用户请求 → Agent 思考 → 调用工具 → 获取结果 → Agent 处理 → 返回响应
```

## 模块结构

```
module_02_core_tools/
├── README.md                          # 本文件
├── docs/
│   ├── 01_概念讲解.md                 # 工具系统详解
│   ├── 02_代码示例.md                 # 实用代码示例
│   └── 03_最佳实践.md                 # 安全性和最佳实践
└── projects/
    ├── project_01_file_analyzer/      # 项目 1：文件分析器
    └── project_02_bash_automation/    # 项目 2：Bash 自动化助手
```

## 项目介绍

### Project 01 - File Analyzer (文件分析器)

**功能**：
- 递归扫描目录结构
- 分析代码文件统计（行数、文件类型）
- 生成项目结构报告
- 搜索特定内容

**学习重点**：
- 使用 `read_file` 和 `list_directory` 工具
- 处理多文件操作
- 生成结构化输出

### Project 02 - Bash Automation (Bash 自动化助手)

**功能**：
- 执行系统命令并解析输出
- 自动化常见开发任务（git、npm、docker）
- 错误处理和重试机制
- 生成执行报告

**学习重点**：
- 使用 `execute_bash` 工具
- 解析命令输出
- 错误处理和安全考虑

## 学习路径

```
1. 阅读 docs/01_概念讲解.md
   ↓
2. 学习 docs/02_代码示例.md
   ↓
3. 实践 Project 01 (文件分析器)
   ↓
4. 实践 Project 02 (Bash 自动化)
   ↓
5. 阅读 docs/03_最佳实践.md
```

## 前置要求

- 完成 Module 01 (Foundations)
- 熟悉 Python 异步编程
- 了解基本的 Bash 命令
- 安装 `claude-agent-sdk>=0.1.0`

## 开始学习

```bash
# 1. 阅读概念讲解
cat claude_agent_course/module_02_core_tools/docs/01_概念讲解.md

# 2. 进入第一个项目
cd claude_agent_course/module_02_core_tools/projects/project_01_file_analyzer

# 3. 安装依赖
uv sync

# 4. 开始编码！
```

## 相关资源

- [Claude Agent SDK - Tools Documentation](https://docs.anthropic.com/agent-sdk/tools)
- [Function Calling Guide](https://docs.anthropic.com/claude/docs/functions-external-tools)
- [Best Practices for Tool Use](https://docs.anthropic.com/claude/docs/tool-use-best-practices)

## 下一步

完成本模块后，继续学习：
- **Module 03**: Custom Tools (自定义工具)
- **Module 04**: MCP Protocol (模型上下文协议)

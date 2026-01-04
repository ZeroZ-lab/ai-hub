# 开发指南 / Contributing Guide

本文档面向课程内容创作者，介绍如何创建新模块、添加项目和维护课程质量。

---

## 📋 目录

- [快速开始](#快速开始)
- [环境配置](#环境配置)
- [模块结构规范](#模块结构规范)
- [使用模板创建内容](#使用模板创建内容)
- [uv 工作流程](#uv-工作流程)
- [代码质量标准](#代码质量标准)
- [开发进度追踪](#开发进度追踪)

---

## 快速开始

### 创建新模块的流程

```bash
# 1. 创建模块目录
mkdir -p claude_agent_course/module_XX_name/{docs,projects}

# 2. 复制模板
cp templates/docs_template_01_概念讲解.md claude_agent_course/module_XX_name/docs/01_概念讲解.md
cp templates/docs_template_02_代码示例.md claude_agent_course/module_XX_name/docs/02_代码示例.md
cp templates/docs_template_03_最佳实践.md claude_agent_course/module_XX_name/docs/03_最佳实践.md

# 3. 创建模块 README（参考 module_01_foundations/README.md）

# 4. 根据实际内容修改模板
```

---

## 环境配置

### 安装 uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 验证
uv --version
```

### 初始化项目

```bash
# 创建新项目
uv init project_name
cd project_name

# 添加依赖
uv add anthropic python-dotenv

# 添加开发依赖
uv add --dev pytest black ruff
```

### 运行代码

```bash
# 运行脚本
uv run python src/main.py

# 运行测试
uv run pytest tests/

# 代码格式化
uv run black src/
```

**详细 uv 使用指南**: 查看根目录的 `uv-quickref.md`

---

## 模块结构规范

### 标准目录结构

```
module_XX_name/
├── README.md                    # 模块概览
├── docs/
│   ├── 01_概念讲解.md           # 理论讲解
│   ├── 02_代码示例.md           # 可运行示例
│   └── 03_最佳实践.md           # 避坑指南
└── projects/
    └── project_01_name/
        ├── README.md            # 项目需求
        ├── pyproject.toml       # uv 配置
        ├── .env.example
        ├── src/
        │   └── main.py
        ├── tests/
        │   └── test_main.py
        └── solution/            # 参考答案
            └── main.py
```

### 文件命名规范

- **模块**: `module_XX_topic` (XX为两位数字)
- **项目**: `project_XX_name` (简短描述性名称)
- **文档**: `XX_中文名称.md` (数字前缀保证顺序)

---

## 使用模板创建内容

### 文档模板

所有模板位于 `templates/` 目录：

| 模板 | 用途 | 关键章节 |
|------|------|----------|
| `docs_template_01_概念讲解.md` | 核心概念讲解 | 为什么 → 是什么 → 如何工作 |
| `docs_template_02_代码示例.md` | 可运行代码 | Hello World → 完整示例 → API 参考 |
| `docs_template_03_最佳实践.md` | 经验总结 | 常见陷阱 → 优化 → 安全 |
| `project_README_template.md` | 项目说明 | 背景 → 需求 → 步骤 → 测试 |

### 使用步骤

1. **复制模板**到目标位置
2. **替换占位符**:
   - `[模块编号]` → 实际模块号
   - `[概念名称]` → 实际概念
   - `[描述]` / `[说明]` → 具体内容
3. **删除**不需要的章节
4. **填充**实际内容
5. **检查**链接和格式

### 示例：创建项目

```bash
# 进入模块的 projects 目录
cd claude_agent_course/module_XX_name/projects

# 创建项目结构
mkdir -p project_01_name/{src,tests,solution}

# 使用 uv 初始化
cd project_01_name
uv init --no-readme

# 添加依赖
uv add anthropic python-dotenv

# 复制模板
cp ../../../templates/project_README_template.md README.md
cp ../../../templates/.env.example .env.example

# 创建代码文件
touch src/__init__.py src/main.py src/agent.py
touch tests/__init__.py tests/test_agent.py
touch solution/main.py
```

---

## uv 工作流程

### 项目依赖管理

#### pyproject.toml 示例

```toml
[project]
name = "project-name"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "anthropic>=0.18.1",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.3",
    "black>=23.12.1",
    "ruff>=0.1.9",
]
```

### 常用命令

```bash
# 安装所有依赖
uv sync

# 添加新依赖
uv add package-name

# 添加开发依赖
uv add --dev package-name

# 移除依赖
uv remove package-name

# 运行脚本
uv run python script.py

# 运行测试
uv run pytest tests/
```

### 为什么使用 uv？

- ⚡ 比 pip 快 10-100 倍
- 🔒 自动锁定依赖版本 (`uv.lock`)
- 🎯 无需手动管理虚拟环境
- 📦 统一的 `pyproject.toml` 配置

---

## 代码质量标准

### Python 代码规范

#### 基础要求
- Python 3.10+ 语法
- 使用 Type Hints
- 遵循 PEP 8
- 详细的 Docstrings

#### 代码模板示例

```python
"""
模块说明：简短描述

Author: Your Name
Date: 2024-01-04
"""

from typing import List, Dict, Optional
from anthropic import Anthropic


class MyAgent:
    """Agent 类说明

    Attributes:
        client: Anthropic 客户端
        model: 模型名称
    """

    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20241022"):
        """初始化

        Args:
            api_key: API 密钥
            model: Claude 模型
        """
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def process(self, input_text: str) -> str:
        """处理输入

        Args:
            input_text: 输入文本

        Returns:
            处理结果
        """
        # 实现代码...
        pass
```

### 质量检查清单

#### 文档质量
- [ ] 所有占位符已替换
- [ ] 代码块有语法高亮
- [ ] 链接都可点击
- [ ] 中英文间有空格

#### 代码质量
- [ ] 所有代码可运行
- [ ] 有详细注释
- [ ] 包含错误处理
- [ ] 提供参考答案

#### 项目质量
- [ ] README 描述清晰
- [ ] 有明确的成功标准
- [ ] 测试用例完整
- [ ] 难度符合模块定位

---

## 开发进度追踪

### 模块开发流程

#### 1. 规划阶段 (30分钟)
- [ ] 明确核心概念（1-3个）
- [ ] 确定实战项目（至少1个）
- [ ] 列出技术要点

#### 2. 文档编写 (2-3小时)
- [ ] 01_概念讲解.md
- [ ] 02_代码示例.md
- [ ] 03_最佳实践.md

#### 3. 项目开发 (3-5小时/项目)
- [ ] 创建项目框架
- [ ] 实现参考答案
- [ ] 编写项目 README
- [ ] 测试完整流程

#### 4. 质量检查 (30分钟)
- [ ] 运行所有代码
- [ ] 检查拼写格式
- [ ] 确保链接正确
- [ ] Review 难度

### 优先级

#### 高优先级 🔴
1. Module 1-2（基础模块）
2. 每个模块的概念讲解
3. 至少1个实战项目

#### 中优先级 🟡
1. 代码示例文档
2. 最佳实践文档
3. 进阶项目

#### 低优先级 🟢
1. 图表配图
2. 视频教程
3. 社区功能

---

## 渐进式难度设计

### 初级项目 (Module 1-2)
- 单文件实现
- 50-100 行代码
- 直接 API 调用
- 重点：理解基础

### 中级项目 (Module 3-4)
- 多文件结构
- 150-300 行代码
- 引入错误处理
- 重点：工程化

### 高级项目 (Module 5-7)
- 完整应用架构
- 500+ 行代码
- 包含测试、配置
- 重点：生产级

---

## 常见问题

### Q: 模板太复杂怎么办？
A: 模板是完整结构参考，实际使用时可以：
- 删除不需要的章节
- 合并相似内容
- 根据模块特点调整

### Q: 如何确保代码质量？
A:
1. 本地运行验证
2. 虚拟环境测试依赖
3. 详细错误处理
4. 注释解释关键步骤

### Q: 如何平衡理论和实践？
A: 推荐比例：
- 概念讲解：30%
- 代码示例：40%
- 实战项目：30%

---

## 贡献流程

1. Fork 仓库
2. 创建分支 (`git checkout -b feature/new-module`)
3. 使用模板创建内容
4. 运行质量检查
5. 提交 PR 并附测试截图

---

**感谢你的贡献！🎉**

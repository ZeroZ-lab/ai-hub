# DevMate

**DevMate** 是一个自主的 AI 研发助手，旨在协助开发者完成从规划、编码到测试的全流程任务。

## 🚀 特性

- **全栈能力**: 能够规划任务、编写代码、修复 Bug 和运行测试。
- **安全**: 关键操作（文件写入、命令执行）需人工确认。
- **上下文感知**: 自动读取 `.gitignore`，理解项目结构。
- **美观**: 基于 `Rich` 的现代化 CLI 界面。

## 📦 安装

```bash
cd projects/devmate
pip install -e .
```

## 🎮 使用

1.  **初始化** (在你的项目根目录下):
    ```bash
    devmate init
    ```

2.  **执行任务**:
    ```bash
    devmate do "给 src/utils.py 增加一个计算斐波那契数列的函数，并写一个测试用例"
    ```

3.  **交互模式**:
    ```bash
    devmate chat
    ```

## 🏗️ 架构

详见 `../../docs/01_系统设计.md`。

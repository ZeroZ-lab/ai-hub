# Project 2: Cached QA Bot - 带缓存的问答机器人

> 学习使用 Prompt Caching 优化成本

## 📚 项目简介

本项目实现一个基于大型文档的问答机器人，使用 Prompt Caching 大幅降低API成本。

## 🎯 学习目标

1. 理解 Prompt Caching 的工作原理
2. 实现缓存标记和管理
3. 测量成本节省效果
4. 处理大文档的问答场景

## 📋 功能特性

- ✅ 加载大型文档作为知识库
- ✅ 自动缓存文档内容
- ✅ 多轮问答（复用缓存）
- ✅ 显示 token使用统计和成本对比

## 🚀 快速开始

```bash
cd projects/project_02_cached_qa_bot
pip install -e .
cp .env.example .env

# 运行问答机器人
python -m solution.main data/sample_doc.md
```

## 📊 成本对比示例

假设文档 10,000 tokens，回答 50 个问题：

| 方案 | Input Tokens | 成本 | 节省 |
|------|-------------|------|------|
| 无缓存 | 500,000 | $1.50 | - |
| 有缓存 | 60,000 | $0.20 | 87% |

## 实现要点

1. 使用 `cache_control` 标记文档
2. 追踪 `cache_read_input_tokens`
3. 计算成本节省比例

详见 `solution/` 目录的完整实现。

# Project 3: Vector Memory - 向量记忆系统

> 使用向量数据库实现长期记忆

## 📚 项目简介

实现基于向量数据库的语义记忆系统，支持长期知识存储和智能检索。

## 🎯 学习目标

1. 理解 Embedding 和向量相似度
2. 使用 ChromaDB 存储向量
3. 实现语义搜索检索
4. 构建 RAG (Retrieval-Augmented Generation) 系统

## 📋 功能特性

- ✅ 向量化文本并存储
- ✅ 语义相似度搜索
- ✅ 持久化向量记忆
- ✅ Agent 集成长期记忆

## 🚀 快速开始

```bash
cd projects/project_03_vector_memory
pip install -e .
cp .env.example .env

# 运行记忆Agent
python -m solution.main
```

## 核心组件

1. **Embedder**: 生成文本向量
2. **VectorStore**: ChromaDB 封装
3. **MemoryAgent**: 带记忆的 Agent

详见 `solution/` 目录。

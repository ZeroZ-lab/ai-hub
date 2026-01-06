# Project 4: Context Compressor - 上下文压缩器

> 智能压缩对话历史，突破上下文限制

## 📚 项目简介

实现多种上下文压缩策略，在保持对话质量的同时控制 token 使用。

## 🎯 学习目标

1. 实现滑动窗口策略
2. 使用 LLM 进行智能摘要
3. 重要性评分机制
4. 混合压缩策略

## 📋 压缩策略

1. **Sliding Window**: 保留最近N条消息
2. **Summarization**: AI总结旧对话
3. **Importance Scoring**: 保留重要消息
4. **Hybrid**: 组合多种策略

## 🚀 快速开始

```bash
cd projects/project_04_context_compressor
pip install -e .

# 测试不同压缩策略
python -m solution.main --strategy sliding
python -m solution.main --strategy summarization
python -m solution.main --strategy hybrid
```

## 性能对比

| 策略 | 压缩率 | 信息保留 | 计算成本 |
|------|--------|---------|---------|
| Sliding | 80% | 低 | 低 |
| Summarization | 95% | 高 | 中 |
| Hybrid | 90% | 中 | 中 |

详见 `solution/` 完整实现。

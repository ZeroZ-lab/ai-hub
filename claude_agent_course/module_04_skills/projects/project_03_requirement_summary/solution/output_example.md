Goal:
- 当库存低于阈值时自动通知运营与仓储团队

Functional requirements:
- 支持为每个 SKU 设置预警阈值
- 阈值命中后发送飞书消息
- 支持每日汇总低库存列表

Non-functional constraints:
- 预警延迟不超过 5 分钟
- 可用性 99.9%

Out of scope:
- 只支持中国区仓库
- 不涉及采购流程联动

Risks/Assumptions:
- 假设飞书通知通道可用且稳定

Open questions:
- 阈值是否支持分仓配置
- 是否需要短信提醒

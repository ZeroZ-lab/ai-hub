"""
Weather Assistant tools
"""

import json
from claude_agent_sdk import tool

# ============ 模拟数据 ============

MOCK_WEATHER = {
    "北京": {"temp": 15, "humidity": 45, "condition": "晴", "city": "北京"},
    "上海": {"temp": 22, "humidity": 70, "condition": "多云", "city": "上海"},
    "广州": {"temp": 28, "humidity": 80, "condition": "阵雨", "city": "广州"},
    "深圳": {"temp": 30, "humidity": 85, "condition": "暴雨", "city": "深圳"},
    "Beijing": {"temp": 15, "humidity": 45, "condition": "Sunny", "city": "Beijing"},
    "Shanghai": {"temp": 22, "humidity": 70, "condition": "Cloudy", "city": "Shanghai"},
}


# ============ 自定义工具 ============

@tool("get_weather", "Get current weather for a city", {"city": str})
async def get_weather(args):
    """获取城市天气"""
    city = args.get("city", "")
    # 简单的模糊匹配
    data = None
    for k, v in MOCK_WEATHER.items():
        if city in k or k in city:
            data = v
            break
            
    if data:
        return {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False)}]}
    else:
        return {"content": [{"type": "text", "text": f"未找到 {city} 的天气数据，请尝试：北京、上海、广州、深圳"}]}


@tool("get_clothing_advice", "Get clothing advice based on temperature", {"temperature": float})
async def get_clothing_advice(args):
    """穿衣建议"""
    temp = float(args.get("temperature", 0))
    if temp < 10:
        advice = "建议穿厚外套、围巾，注意保暖。"
    elif temp < 20:
        advice = "建议穿薄外套或毛衣，早晚温差较大。"
    elif temp < 28:
        advice = "建议穿短袖、轻便衣物，舒适宜人。"
    else:
        advice = "天气炎热，建议穿清凉透气衣物，注意防晒。"
    
    return {"content": [{"type": "text", "text": advice}]}


@tool("check_weather_alert", "Check for severe weather alerts", {"condition": str})
async def check_weather_alert(args):
    """天气预警检查"""
    condition = args.get("condition", "")
    alerts = []
    
    if "雨" in condition:
        alerts.append("⚠️ 雨天路滑，请携带雨具，注意出行安全。")
    if "暴雨" in condition:
        alerts.append("⛔️ 暴雨预警：建议减少户外活动，注意防涝。")
    if "雪" in condition:
        alerts.append("⚠️ 雪天路滑，注意防寒保暖。")
    if "晴" in condition and "Sunny" not in condition: # 简单区分中英文
        alerts.append("☀️ 紫外线较强，请注意防晒。")
        
    if not alerts:
        alerts.append("✅ 无特殊气象预警，适宜出行。")
        
    return {"content": [{"type": "text", "text": "\n".join(alerts)}]}

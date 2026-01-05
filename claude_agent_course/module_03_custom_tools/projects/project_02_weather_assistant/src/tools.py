"""
天气查询工具定义

TODO: 实现以下工具
- get_weather: 获取城市天气
- get_clothing_advice: 穿衣建议
- check_weather_alert: 检查天气预警
"""

# 模拟天气数据
MOCK_WEATHER = {
    "北京": {"temp": 15, "humidity": 45, "condition": "晴"},
    "上海": {"temp": 22, "humidity": 70, "condition": "多云"},
    "广州": {"temp": 28, "humidity": 80, "condition": "阵雨"},
    "深圳": {"temp": 27, "humidity": 75, "condition": "多云"},
    "杭州": {"temp": 20, "humidity": 65, "condition": "晴"},
}


# TODO: 使用 @tool 装饰器实现 get_weather
async def get_weather(args: dict) -> dict:
    """获取城市天气"""
    pass


# TODO: 使用 @tool 装饰器实现 get_clothing_advice
async def get_clothing_advice(args: dict) -> dict:
    """根据温度给出穿衣建议"""
    pass


# TODO: 使用 @tool 装饰器实现 check_weather_alert
async def check_weather_alert(args: dict) -> dict:
    """检查天气预警"""
    pass

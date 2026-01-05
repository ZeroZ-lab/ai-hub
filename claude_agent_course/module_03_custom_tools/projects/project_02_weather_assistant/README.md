# Weather Assistant - 天气查询助手

> **难度**: 🌟🌟 中级
> **预计时间**: 60-90 分钟

---

## 项目背景

使用**自定义工具**构建一个天气查询助手，能够查询城市天气、提供穿衣建议和天气预警。

---

## 学习目标

- [ ] 使用 `@tool` 装饰器封装外部 API
- [ ] 处理工具调用中的错误情况
- [ ] 实现多工具协作（查询 + 分析）

---

## 功能需求

### 必做功能

#### 1. 查询当前天气
- 输入：城市名称
- 输出：温度、湿度、天气状况

#### 2. 穿衣建议
- 根据温度给出穿衣建议

#### 3. 天气预警
- 检测极端天气（高温、低温、暴雨等）

---

## 技术要点

### 自定义工具

```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("get_weather", "Get current weather for a city", {"city": str})
async def get_weather(args):
    city = args["city"]
    # 调用天气 API 或模拟数据
    weather_data = fetch_weather(city)
    return {
        "content": [{"type": "text", "text": json.dumps(weather_data)}]
    }

@tool("get_clothing_advice", "Get clothing advice based on temperature", {"temperature": float})
async def get_clothing_advice(args):
    temp = args["temperature"]
    if temp < 10:
        advice = "建议穿厚外套、围巾"
    elif temp < 20:
        advice = "建议穿薄外套或毛衣"
    else:
        advice = "建议穿短袖、轻便衣物"
    return {"content": [{"type": "text", "text": advice}]}

server = create_sdk_mcp_server(
    name="weather",
    version="1.0.0",
    tools=[get_weather, get_clothing_advice]
)
```

### 模拟天气数据

```python
MOCK_WEATHER = {
    "北京": {"temp": 15, "humidity": 45, "condition": "晴"},
    "上海": {"temp": 22, "humidity": 70, "condition": "多云"},
    "广州": {"temp": 28, "humidity": 80, "condition": "阵雨"},
}
```

---

## 实现步骤

### 第一步：创建天气工具

在 `src/tools.py` 中定义：

```python
# TODO: 实现以下工具
# - get_weather: 获取城市天气
# - get_clothing_advice: 穿衣建议
# - check_weather_alert: 检查天气预警
```

### 第二步：创建 Agent

在 `src/agent.py` 中：

```python
class WeatherAssistant:
    def __init__(self):
        # TODO: 创建工具服务器
        pass

    async def query(self, city: str) -> str:
        # TODO: 查询天气并给出建议
        pass
```

### 第三步：添加交互循环

在 `src/main.py` 中实现用户交互。

---

## 测试方法

```bash
cd claude_agent_course/module_03_custom_tools/projects/project_02_weather_assistant
uv sync
uv run python src/main.py
```

### 测试用例

```
你: 北京今天天气怎么样？
Agent: 北京当前天气：晴，温度 15°C，湿度 45%。
      建议穿薄外套或毛衣。

你: 广州天气如何？需要带伞吗？
Agent: 广州当前天气：阵雨，温度 28°C，湿度 80%。
      ⚠️ 天气预警：有阵雨，建议携带雨具。
```

---

## 完成标准

### ✅ 基础版（60 分）
- [ ] 实现天气查询工具
- [ ] 能返回基本天气信息

### ✅ 良好版（80 分）
- [ ] 添加穿衣建议功能
- [ ] 处理未知城市的错误

### ✅ 优秀版（100 分）
- [ ] 实现天气预警
- [ ] 支持多日天气预报

---

## 项目结构

```
project_02_weather_assistant/
├── README.md
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   └── tools.py
├── data/
│   └── mock_weather.json
└── solution/
    └── main.py
```

---

## 扩展挑战

- 接入真实天气 API（如 OpenWeatherMap）
- 添加空气质量查询
- 支持语音播报天气

---

**开始构建你的天气助手！🌤️**

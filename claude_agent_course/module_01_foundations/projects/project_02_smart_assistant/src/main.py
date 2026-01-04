"""智能助手 SSE 服务器 (Starlette/Uvicorn)"""

import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse
from sse_starlette.sse import EventSourceResponse
from dotenv import load_dotenv
from assistant import SmartAssistant

# 加载环境变量
load_dotenv()

# TODO: 1. 创建全局助手实例
# assistant = ...
pass

async def chat_endpoint(request: Request):
    """处理 SSE 聊天请求"""
    # TODO: 2. 获取用户消息
    # user_message = ...
    pass

    async def event_generator():
        """生成 SSE 事件"""
        # TODO: 3. 调用助手流式接口并 yield 数据
        # async for chunk in assistant.chat_stream(user_message):
        #     yield {"data": chunk}
        pass

    # TODO: 4. 返回 EventSourceResponse
    # return EventSourceResponse(...)
    pass

# 定义路由
routes = [
    Route("/chat", chat_endpoint, methods=["GET"]),
    # 可以添加其他路由，如 /clear
]

# 创建应用
app = Starlette(debug=True, routes=routes)

def main():
    """启动服务器"""
    print("🚀 启动智能助手 SSE 服务器...")
    print("📡 监听地址: http://0.0.0.0:8000")
    print("💡 测试命令: curl -N 'http://127.0.0.1:8000/chat?message=Hello'")
    
    # TODO: 5. 启动 Uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    pass

if __name__ == "__main__":
    main()

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

# 创建全局助手实例 (以便维持 session_id 状态)
# 注意：在多用户生产环境中，应该为每个会话创建新的助手实例，或者使用 session_id 管理
assistant = SmartAssistant()

async def chat_endpoint(request: Request):
    """处理 SSE 聊天请求"""
    user_message = request.query_params.get("message")
    
    if not user_message:
        return JSONResponse({"error": "Missing 'message' query parameter"}, status_code=400)

    async def event_generator():
        """生成 SSE 事件"""
        try:
            # 调用助手的流式接口
            async for chunk in assistant.chat_stream(user_message):
                # SSE 格式: data: <content>\n\n
                # sse-starlette 会自动处理 dict 或 string
                # 这里我们发送 JSON 数据以便前端解析，或者直接发送文本
                # 为了简单演示，发送文本
                yield {"data": chunk}
            
            # 可以在结束后发送一个特定事件表示完成，或者直接关闭流
            # yield {"event": "done", "data": "[DONE]"}
            
        except Exception as e:
            yield {"event": "error", "data": str(e)}

    return EventSourceResponse(event_generator())

async def clear_history(request: Request):
    """清空历史"""
    assistant.clear_history()
    return JSONResponse({"status": "success", "message": "History cleared"})

# 定义路由
routes = [
    Route("/chat", chat_endpoint, methods=["GET"]),
    Route("/clear", clear_history, methods=["POST", "GET"])
]

# 创建应用
app = Starlette(debug=True, routes=routes)

def main():
    """启动服务器"""
    print("🚀 启动智能助手 SSE 服务器...")
    print("📡 监听地址: http://0.0.0.0:8000")
    print("💡 测试命令: curl -N 'http://127.0.0.1:8000/chat?message=Hello'")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

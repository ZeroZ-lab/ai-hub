def send_email(to: str, subject: str, body: str) -> str:
    """发送邮件（敏感操作）"""
    # 实际逻辑中这会真的发邮件
    return f"Email sent to {to}"

def get_user_info(user_id: str) -> str:
    """获取用户信息（只读操作）"""
    return f"User {user_id}: Name=Alice, Email=alice@example.com"

# 在这里配置哪些工具是敏感的
SENSITIVE_TOOLS = ["send_email"]

TOOLS = {
    "send_email": send_email,
    "get_user_info": get_user_info
}

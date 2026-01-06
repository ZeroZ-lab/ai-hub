def calculate(expression: str) -> str:
    """
    一个安全的计算器工具。
    支持加减乘除。
    示例输入: "2 + 2"
    """
    try:
        # ⚠️ 注意：在生产环境中 eval 是危险的，这里仅作演示
        # 限制只能使用数字和操作符
        for char in expression:
            if char not in "0123456789+-*/. ()":
                return f"Error: 非法字符 '{char}'"
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

def get_word_length(word: str) -> str:
    """
    计算单词的长度。
    示例输入: "apple"
    """
    return str(len(word.strip()))

# 工具注册表
TOOLS = {
    "calculate": calculate,
    "get_word_length": get_word_length
}

def get_tools_description():
    """生成工具描述字符串给 Prompt 使用"""
    desc = ""
    for name, func in TOOLS.items():
        desc += f"{name}: {func.__doc__.strip()}\n"
    return desc.strip()

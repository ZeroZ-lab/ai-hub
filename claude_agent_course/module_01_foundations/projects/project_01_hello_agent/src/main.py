"""
Hello Agent - 主程序

这是项目的主程序入口文件。

Author: Your Name
Date: 2024-01-04
"""

import sys
import os


def show_environment():
    """显示环境信息"""
    # TODO: 实现显示 Python 版本和当前目录
    pass


def main():
    """主函数"""
    print("=" * 60)
    print("Hello Agent - 文件查看助手")
    print("=" * 60)

    # TODO: 1. 显示环境信息
    # show_environment()

    # TODO: 2. 创建 FileAgent 实例

    # TODO: 3. 实现交互循环
    print("\n命令:")
    print("  ls    - 列出当前目录文件")
    print("  stat  - 统计文件类型")
    print("  exit  - 退出程序")
    print("=" * 60)

    while True:
        user_input = input("\n你: ").strip()

        if user_input.lower() in ['exit', 'quit', '退出']:
            print("\n再见！👋")
            break

        # TODO: 处理用户命令


if __name__ == "__main__":
    main()

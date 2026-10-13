"""
第一个练手脚本。

改一改这里的文字，然后走一遍：
    git add .
    git commit -m "docs: 改了问候语"
    git push
"""

from datetime import datetime


def greet(name: str = "World") -> str:
    """生成一句问候。"""
    hour = datetime.now().hour
    if hour < 6:
        period = "凌晨好"
    elif hour < 12:
        period = "早上好"
    elif hour < 18:
        period = "下午好"
    else:
        period = "晚上好"
    return f"{period}，{name}！"


def main() -> None:
    print(greet("xiaobai44C"))
    print("这是你的第一个 GitHub 仓库 🎉")
    print("当前时间：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    main()

"""Pythonを用いた関数型プログラミング
参照透過である関数

[説明ページ]
https://tech.nkhn37.net/python-functional-programming/#i-6
"""


def square(x):
    """値を2乗する"""
    return x**2


if __name__ == "__main__":
    print(square(2))
    print(square(2))
    print(square(3))
    print(square(3))

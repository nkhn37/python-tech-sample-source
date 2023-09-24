"""Pythonを用いた関数型プログラミング
参照透過ではない関数

[説明ページ]
https://tech.nkhn37.net/python-functional-programming/#i-6
"""
global_value = 0


def func():
    global global_value
    global_value += 1

    return global_value


if __name__ == "__main__":
    print(func())
    print(func())
    print(func())

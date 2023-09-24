"""Pythonを用いた関数型プログラミング
関数型での書き方例

[説明ページ]
https://tech.nkhn37.net/python-functional-programming/#i-4
"""
from functools import reduce


def add_nums(x, y):
    """値を足し算する"""
    return x + y


def square(x):
    """値を2乗する"""
    return x**2


target = [1, 2, 3, 4, 5]

# 関数で書く場合
sum_value = reduce(add_nums, map(square, target))
print(sum_value)

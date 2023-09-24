"""reduce関数の使い方の基本
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-reduce-basic/#i
"""
from functools import reduce


def add_nums(x, y):
    """値を足し算する"""
    return x + y


def multiply_nums(x, y):
    """値を掛け算する"""
    return x * y


if __name__ == "__main__":
    tmp_list = [1, 2, 3, 4, 5]

    # reduce関数でadd_nums関数を適用する
    result = reduce(add_nums, tmp_list)
    print(result)

    # reduce関数でmultiply_nums関数を適用する
    result = reduce(multiply_nums, tmp_list)
    print(result)

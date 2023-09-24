"""filter関数の使い方の基本
リストやタプルで結果を取得する場合

[説明ページ]
https://tech.nkhn37.net/python-filter-basic/#i-2
"""


def is_even(num):
    """数値が偶数か判定する"""
    return num % 2 == 0


if __name__ == "__main__":
    tmp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # filter関数を適用し、リストで取得
    result = list(filter(is_even, tmp_list))
    print(result)

    # filter関数を適用し、タプルで取得
    result = tuple(filter(is_even, tmp_list))
    print(result)

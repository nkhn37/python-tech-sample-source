"""filter関数の使い方の基本
基本的な使い方 (イテレータで取得する)

[説明ページ]
https://tech.nkhn37.net/python-filter-basic/#i
"""


def is_even(num):
    """数値が偶数か判定する"""
    return num % 2 == 0


if __name__ == "__main__":
    tmp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # filter関数を適用し、イテレータを取得
    result = filter(is_even, tmp_list)
    print(result, "\n")

    # nextで1要素ずつ結果データを取得
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))

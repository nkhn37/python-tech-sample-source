"""map関数の使い方の基本
リストやタプルで結果を取得する場合

[説明ページ]
https://tech.nkhn37.net/python-map-basic/#i-2
"""


def square(x):
    """値を2乗する"""
    return x**2


if __name__ == "__main__":
    tmp_list = [1, 2, 3, 4, 5]

    # map関数を適用し、リストで取得
    result_list = list(map(square, tmp_list))
    print(result_list)

    # map関数を適用し、タプルで取得
    result_tuple = tuple(map(square, tmp_list))
    print(result_tuple)

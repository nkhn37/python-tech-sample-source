"""map関数の使い方の基本
基本的な使い方 (イテレータで取得する)

[説明ページ]
https://tech.nkhn37.net/python-map-basic/#i
"""


def square(x):
    """値を2乗する"""
    return x**2


if __name__ == "__main__":
    tmp_list = [1, 2, 3, 4, 5]

    # map関数を適用し、イテレータを取得
    result = map(square, tmp_list)
    print(result, "\n")

    # nextで1要素ずつ結果データを取得
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))

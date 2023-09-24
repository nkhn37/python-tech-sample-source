"""map関数の使い方の基本
異なる長さの複数イテラブルを指定する場合

[説明ページ]
https://tech.nkhn37.net/python-map-basic/#i-4
"""


def make_variable_set(x, y, z):
    """各引数を並べたタプルを返却する"""
    return x, y, z


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6, 7, 8, 9]
    nums3 = [10, 11, 12, 13, 14]

    # map関数で複数のイテラブルを渡す
    # 最も短いイテラブルが消費されたら終了
    result = list(map(make_variable_set, nums1, nums2, nums3))
    print(result)

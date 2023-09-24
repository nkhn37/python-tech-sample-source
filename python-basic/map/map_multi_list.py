"""map関数の使い方の基本
複数イテラブルを指定する場合

[説明ページ]
https://tech.nkhn37.net/python-map-basic/#i-3
"""


def make_variable_set(x, y, z):
    """各引数を並べたタプルを返却する"""
    return x, y, z


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    nums3 = [7, 8, 9]

    # map関数で複数のイテラブルを渡す
    # 関数側もイテラブルの数だけの引数を受け取れる必要がある
    result = list(map(make_variable_set, nums1, nums2, nums3))
    print(result)

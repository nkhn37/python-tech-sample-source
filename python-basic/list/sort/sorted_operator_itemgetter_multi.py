"""リスト基礎
複数keyを指定してソートする場合
(operatorモジュール関数のitemgetterを使用)

listのリストデータ

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#i-10
"""
from operator import itemgetter

data = [
    [3, 20, "b"],
    [1, 20, "b"],
    [2, 10, "a"],
    [1, 10, "a"],
    [2, 20, "b"],
    [3, 10, "a"],
    [1, 30, "c"],
    [3, 30, "c"],
    [2, 30, "c"],
]

# ===== 複数keyを指定してソートする (sort関数)
sorted_data = sorted(data, key=itemgetter(0, 1))
print(f"sorted data: {sorted_data}")

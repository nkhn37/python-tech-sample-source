"""リスト基礎
keyを指定してソートする場合
(operatorモジュール関数のitemgetterを使用)

listのリストデータ

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#_itemgetter-3
"""
from operator import itemgetter

data = [
    ["ID002", "john", 70],
    ["ID001", "mike", 20],
    ["ID005", "jane", 1],
    ["ID004", "aiko", 50],
    ["ID003", "taro", 5],
]

# ===== keyを指定してソートする (sorted関数)
# 0列目でソートする場合
sorted_data = sorted(data, key=itemgetter(0))
print(f"sorted_data: {sorted_data}")
# 1列目でソートする場合
sorted_data = sorted(data, key=itemgetter(1))
print(f"sorted_data: {sorted_data}")
# 2列目でソートする場合
sorted_data = sorted(data, key=itemgetter(2))
print(f"sorted_data: {sorted_data}")

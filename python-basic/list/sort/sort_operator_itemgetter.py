"""リスト基礎
keyを指定してソートする場合
(operatorモジュール関数のitemgetterを使用)

listのリストデータ

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#_itemgetter
"""
from operator import itemgetter

data = [
    ["ID002", "john", 70],
    ["ID001", "mike", 20],
    ["ID005", "jane", 1],
    ["ID004", "aiko", 50],
    ["ID003", "taro", 5],
]

# ===== keyを指定してソートする (sortメソッド)
# 0列目でソートする場合
data.sort(key=itemgetter(0))
print(f"data: {data}")
# 1列目でソートする場合
data.sort(key=itemgetter(1))
print(f"data: {data}")
# 2列目でソートする場合
data.sort(key=itemgetter(2))
print(f"data: {data}")

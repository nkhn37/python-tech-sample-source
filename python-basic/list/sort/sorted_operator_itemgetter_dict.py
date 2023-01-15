"""リスト基礎
keyを指定してソートする場合
(operatorモジュール関数のitemgetterを使用)

dictのリストデータ

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#_itemgetter-4
"""
from operator import itemgetter

data = [
    {"id": "ID002", "name": "john", "value": 70},
    {"id": "ID001", "name": "mike", "value": 20},
    {"id": "ID005", "name": "jane", "value": 1},
    {"id": "ID004", "name": "aiko", "value": 50},
    {"id": "ID003", "name": "taro", "value": 5},
]

# ===== keyを指定してソートする (sortdメソッド)
# idでソートする場合
sorted_data = sorted(data, key=itemgetter("id"))
print(f"sorted_data: {sorted_data}")
# nameでソートする場合
sorted_data = sorted(data, key=itemgetter("name"))
print(f"sorted_data: {sorted_data}")
# valueでソートする場合
sorted_data = sorted(data, key=itemgetter("value"))
print(f"sorted_data: {sorted_data}")

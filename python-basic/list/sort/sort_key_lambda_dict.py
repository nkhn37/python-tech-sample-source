"""リスト基礎
keyを指定してソートする場合
(sortメソッドでlambdaを使用)

dictのリストデータ

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#i-2
"""
data = [
    {"id": "ID002", "name": "john", "value": 70},
    {"id": "ID001", "name": "mike", "value": 20},
    {"id": "ID005", "name": "jane", "value": 1},
    {"id": "ID004", "name": "aiko", "value": 50},
    {"id": "ID003", "name": "taro", "value": 5},
]

# ===== keyを指定してソートする (sortメソッド)
# idでソートする場合
data.sort(key=lambda d: d["id"])
print(f"data: {data}")
# nameでソートする場合
data.sort(key=lambda d: d["name"])
print(f"data: {data}")
# valueでソートする場合
data.sort(key=lambda d: d["value"])
print(f"data: {data}")

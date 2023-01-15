"""リスト基礎
keyを指定してソートする場合
(sorted関数でlambdaを使用)

dictのリストデータ

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#i-6
"""
data = [
    {"id": "ID002", "name": "john", "value": 70},
    {"id": "ID001", "name": "mike", "value": 20},
    {"id": "ID005", "name": "jane", "value": 1},
    {"id": "ID004", "name": "aiko", "value": 50},
    {"id": "ID003", "name": "taro", "value": 5},
]

# ===== keyを指定してソートする (sortdメソッド)
# idでソートする場合
sorted_data = sorted(data, key=lambda d: d["id"])
print(f"sorted_data: {sorted_data}")
# nameでソートする場合
sorted_data = sorted(data, key=lambda d: d["name"])
print(f"sorted_data: {sorted_data}")
# valueでソートする場合
sorted_data = sorted(data, key=lambda d: d["value"])
print(f"sorted_data: {sorted_data}")

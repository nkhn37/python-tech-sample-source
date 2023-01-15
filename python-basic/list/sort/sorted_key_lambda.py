"""リスト基礎
keyを指定してソートする場合
(sorted関数でlambdaを使用)

listのリストデータ

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#i-5
"""
data = [
    ["ID002", "john", 70],
    ["ID001", "mike", 20],
    ["ID005", "jane", 1],
    ["ID004", "aiko", 50],
    ["ID003", "taro", 5],
]

# ===== keyを指定してソートする (sorted関数)
# 0列目でソートする場合
sorted_data = sorted(data, key=lambda d: d[0])
print(f"sorted_data: {sorted_data}")
# 1列目でソートする場合
sorted_data = sorted(data, key=lambda d: d[1])
print(f"sorted_data: {sorted_data}")
# 2列目でソートする場合
sorted_data = sorted(data, key=lambda d: d[2])
print(f"sorted_data: {sorted_data}")

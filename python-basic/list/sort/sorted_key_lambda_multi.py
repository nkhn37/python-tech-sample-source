"""リスト基礎
複数keyを指定してソートする場合
(sorted関数でlambdaを使用)

listのリストデータ

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#i-8
"""
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

# ===== 複数keyを指定してソートする (sorted関数)
sorted_data = sorted(data, key=lambda d: (d[0], d[1]))
print(f"sorted data: {sorted_data}")

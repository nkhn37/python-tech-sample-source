"""リスト基礎
リストの要素位置を返すindexメソッドの使い方
（リストの検索開始位置、終了位置を指定する方法）

[説明ページ]
https://tech.nkhn37.net/python-list-index/#i
"""
# 開始位置と終了位置を指定する。
data = ["A", "B", "C", "A", "B", "C", "D"]

idx = data.index("B", 2, 5)
print(f"idx: {idx}, data[idx]: {data[idx]}")

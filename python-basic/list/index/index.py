"""リスト基礎
リストの要素位置を返すindexメソッドの使い方（基本）

[説明ページ]
https://tech.nkhn37.net/python-list-index/#index
"""
# リスト内の特定要素の位置を確認する
data = ["A", "B", "C", "A", "B", "C", "D"]

idx = data.index("B")
print(f"idx: {idx}, data[idx]: {data[idx]}")

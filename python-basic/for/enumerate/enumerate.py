"""for文基礎
enumerateを用いたfor文の使い方
（基本的な使い方）

[説明ページ]
https://tech.nkhn37.net/python-for-enumerate/#for
"""
data = ["A", "B", "C", "D", "E"]

# enumerateでインデックス番号と値を取り出して処理
for idx, dt in enumerate(data):
    print(f"idx: {idx}, dt: {dt}")

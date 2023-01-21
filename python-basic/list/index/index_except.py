"""リスト基礎
リストの要素位置を返すindexメソッドの使い方
（indexメソッドの例外処理）

[説明ページ]
https://tech.nkhn37.net/python-list-index/#index-2
"""
# 要素が含まれていない場合の処理
data = ["A", "B", "C", "A", "B", "C", "D"]

try:
    idx = data.index("Z")
except ValueError as ex:
    print("Error:", ex)

"""リスト基礎
sortメソッドを使用する場合（降順）

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#sort-2
"""
# リストのデータそのものを降順でソートする。（sortメソッド、reverse）
data = [15, 5, 20, 1, 10, 25]
data.sort(reverse=True)
print(f"data: {data}")

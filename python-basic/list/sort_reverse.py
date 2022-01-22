"""リスト基礎
sort関数を使用する場合（降順）

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#list-2
"""
# リストのデータそのものを逆順でソートする。（sortメソッド、reverse）
data = [15, 5, 20, 1, 10, 25]
data.sort(reverse=True)
print(f'data: {data}')

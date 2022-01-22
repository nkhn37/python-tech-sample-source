"""リスト基礎
sorted関数を使用する場合（降順）

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#list-2
"""
# リストを降順に並べ替えたリストを返却する。（sortedメソッド、reverse）
data = [15, 5, 20, 1, 10, 25]
sorted_data = sorted(data, reverse=True)
print(f'sorted_data: {sorted_data}')
print(f'data: {data}')

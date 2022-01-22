"""リスト基礎
*演算子を用いたリストの拡張方法（注意事項）

・*演算子でリスト等のミュータブル（mutable）な要素を持つリストで拡張した場合は、
参照がコピーされるため元の要素への変更がそのまま反映されることに注意しましょう。

[説明ページ]
https://tech.nkhn37.net/python-list-extend/#i-2
"""
data = [['A', 'B'], ['C', 'D']]
data *= 3
print(f'data: {data}')
# 要素に変更を加える
data[0].append('Z')
print(f'append後 data: {data}')

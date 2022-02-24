"""Collectionsモジュール
名前付きタプル namedtuple
_replaceで一部の値を変更した新しいnamedtupleを作成する

[説明ページ]
https://tech.nkhn37.net/python-collections-namedtuple/#_replacenamedtuple
"""
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)

# p1のxの値を置き換える
print(p1._replace(x=50))
# p1の値が書き換わるわけではないので注意
print(p1)

# 値を書き換えた場合は別のインスタンスに代入する
p2 = p1._replace(x=50)
print(f'p1 = {p1}')
print(f'p2 = {p2}')

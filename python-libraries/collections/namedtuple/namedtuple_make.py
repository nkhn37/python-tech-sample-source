"""Collectionsモジュール
名前付きタプル namedtuple
_makeで新しいnamedtupleを作成する

[説明ページ]
https://tech.nkhn37.net/python-collections-namedtuple/#_makenamedtuple
"""
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

data = [10, 20]
p_data = Point._make(data)
print(f'p_data = {p_data}')
print(p_data.x, p_data.y)

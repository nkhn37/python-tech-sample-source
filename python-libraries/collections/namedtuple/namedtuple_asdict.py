"""Collectionsモジュール
名前付きタプル namedtuple
_asdictで辞書としてnamedtupleの情報を取得する

[説明ページ]
https://tech.nkhn37.net/python-collections-namedtuple/#_asdictnamedtuple
"""
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)
p_dict = p1._asdict()

print(type(p_dict))
print(p_dict)
print(p_dict['x'])
print(p_dict['y'])

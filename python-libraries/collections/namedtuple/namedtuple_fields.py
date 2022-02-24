"""Collectionsモジュール
名前付きタプル namedtuple
_fieldsによりフィールド名を取得する

[説明ページ]
https://tech.nkhn37.net/python-collections-namedtuple/#_fields
"""
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)
print(p1._fields)

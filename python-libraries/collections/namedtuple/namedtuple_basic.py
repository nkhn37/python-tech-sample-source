"""Collectionsモジュール
名前付きタプル namedtupleの定義と使い方

[説明ページ]
https://tech.nkhn37.net/python-collections-namedtuple/#namedtuple
"""
import collections

# named tupleの定義
Point = collections.namedtuple("Point", ["x", "y"])

# インスタンス化
p1 = Point(10, 20)
p2 = Point(x=30, y=40)
print(f"p1 = {p1}")
print(f"p2 = {p2}")

# フィールド名で値へアクセス
print(f"p1.x = {p1.x}, p1.y = {p1.y}")
print(f"p2.x = {p2.x}, p1.y = {p2.y}")

# アンパック代入
x1, y1 = p1
x2, y2 = p2
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")

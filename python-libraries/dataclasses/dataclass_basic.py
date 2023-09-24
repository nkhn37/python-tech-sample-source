"""dataclassの使い方の基本
dataclassクラスデコレータの基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-dataclass-basics/#i-2
"""
from dataclasses import dataclass


@dataclass
class Point:
    """位置クラス"""

    x: int
    y: int

    def __add__(self, other):
        """+演算子"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """-演算子"""
        return Point(self.x - other.x, self.y - other.y)


if __name__ == "__main__":
    point1 = Point(1, 1)
    point2 = Point(2, 2)
    point3 = Point(1, 1)

    print(point1)
    print(point2)
    print(point1 + point2)
    print(point1 - point2)
    print(point1 == point3)

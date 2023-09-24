"""dataclassの使い方の基本
一般的なデータクラスの定義方法

[説明ページ]
https://tech.nkhn37.net/python-dataclass-basics/#i
"""


class Point:
    """位置クラス"""

    def __init__(self, x, y):
        """コンストラクタ"""
        self.x = x
        self.y = y

    def __repr__(self):
        """位置のテキスト表現を返す"""
        return f"Point(x={self.x}, y={self.y})"

    def __add__(self, other):
        """+演算子"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """-演算子"""
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """等価比較"""
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    point1 = Point(1, 1)
    point2 = Point(2, 2)
    point3 = Point(1, 1)

    print(point1)
    print(point2)
    print(point1 + point2)
    print(point1 - point2)
    print(point1 == point3)

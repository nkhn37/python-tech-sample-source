"""構造的パターンマッチ (match case) の使い方
クラスパターン(Class Patterns)の場合
dataclassクラスデコレータを使わない場合、__match_args__が必要

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#Class_Patterns
"""


class Point:
    """位置クラス"""

    # 属性の順序を__match_args__に追加する必要がある
    __match_args__ = ("x", "y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


def where_is(point):
    match point:
        case Point(0, 0):
            print(f"原点: {point}")
        case Point(0, y):
            print(f"Y={y}: {point}")
        case Point(x, 0):
            print(f"X={x}: {point}")
        case Point():
            print(point)
        case _:
            print("Pointではない")


if __name__ == "__main__":
    pt1 = Point(0, 0)
    where_is(pt1)

    print("---")
    pt2 = Point(0, 5)
    where_is(pt2)

    print("---")
    pt3 = Point(5, 0)
    where_is(pt3)

    print("---")
    pt4 = Point(10, 10)
    where_is(pt4)

    print("---")
    pt5 = (20, 20)
    where_is(pt5)

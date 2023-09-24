"""構造的パターンマッチ (match case) の使い方
クラスパターン(Class Patterns)の場合
位置引数でパターンマッチ

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#Class_Patterns
"""
from dataclasses import dataclass


@dataclass
class Point:
    """位置クラス"""

    x: int
    y: int


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

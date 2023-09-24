"""構造的パターンマッチの基本
ifガードを使用する場合

[説明ページ]

"""
from dataclasses import dataclass


@dataclass
class Point:
    """位置クラス"""

    x: int
    y: int


def compare_xy(point):
    match point:
        case Point() if point.x == point.y:
            print("x == y")
        case Point() if point.x < point.y:
            print("x < y")
        case Point() if point.x > point.y:
            print("x > y")
        case _:
            print("対象外")


if __name__ == "__main__":
    pt1 = Point(1, 1)
    compare_xy(pt1)

    print("---")
    pt2 = Point(0, 10)
    compare_xy(pt2)

    print("---")
    pt3 = Point(10, 0)
    compare_xy(pt3)

    print("---")
    pt4 = (1, 1)
    compare_xy(pt4)

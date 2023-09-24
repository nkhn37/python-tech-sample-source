"""構造的パターンマッチ (match case) の使い方
ASパターン(AS Patterns)の場合

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#ASAS_Patterns
"""
from dataclasses import dataclass


@dataclass
class Point:
    """位置クラス"""

    x: int
    y: int


def show(points):
    match points:
        case (Point() as p1, Point() as p2):
            print(p1)
            print(p2)
        case _:
            print("対象外")


if __name__ == "__main__":
    target = [Point(0, 0), Point(10, 10)]
    show(target)

    print("---")
    target = Point(20, 20)
    show(target)

"""構造的パターンマッチ (match case) の使い方
値パターン(Value Patterns)の場合

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#Value_Patterns
"""
from enum import Enum, auto


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLO = auto()


def check(target):
    match target:
        case Color.RED:
            print("赤")
        case Color.GREEN:
            print("緑")
        case Color.BLUE:
            print("青")
        case _:
            print("一致はありません")


if __name__ == "__main__":
    color = Color.RED
    check(color)

    print("---")
    color = Color.GREEN
    check(color)

    print("---")
    color = Color.BLUE
    check(color)

    print("---")
    color = Color.YELLO
    check(color)

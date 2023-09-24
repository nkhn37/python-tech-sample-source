"""列挙型 enumの使い方の基本
列挙型が一意であることの保証 unique

[説明ページ]
https://tech.nkhn37.net/python-enum-basics/#_unique
"""
from enum import Enum, unique


# 要素が一意であることを保証する場合にはuniqueデコレータをつける
@unique
class Weekday(Enum):
    """曜日列挙クラス"""

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    # ↓の行はエラーとなる
    SATURDAY = 0


if __name__ == "__main__":
    print(Weekday.SUNDAY, Weekday.SUNDAY.name, Weekday.SUNDAY.value)
    print(Weekday.MONDAY, Weekday.MONDAY.name, Weekday.MONDAY.value)
    print(Weekday.TUESDAY, Weekday.TUESDAY.name, Weekday.TUESDAY.value)
    print(Weekday.WEDNESDAY, Weekday.WEDNESDAY.name, Weekday.WEDNESDAY.value)
    print(Weekday.THURSDAY, Weekday.THURSDAY.name, Weekday.THURSDAY.value)
    print(Weekday.FRIDAY, Weekday.FRIDAY.name, Weekday.FRIDAY.value)
    print(Weekday.SATURDAY, Weekday.SATURDAY.name, Weekday.SATURDAY.value)

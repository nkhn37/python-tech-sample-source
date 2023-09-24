"""列挙型 enumの使い方の基本
数値と比較したい場合 (IntEnum)

[説明ページ]
https://tech.nkhn37.net/python-enum-basics/#_IntEnum
"""
from enum import Enum, IntEnum, auto


class Weekday(Enum):
    """曜日列挙クラス Enumで定義"""

    SUNDAY = 0
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()


class WeekdayInt(IntEnum):
    """曜日列挙クラス IntEnumで定義"""

    SUNDAY = 0
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()


if __name__ == "__main__":
    # 水曜日を想定して3を設定
    day_of_week = 3

    # Enumを使うと数値との比較はできない
    if day_of_week == Weekday.WEDNESDAY:
        print("Enum")

    # IntEnumを使うと数値と比較が可能
    if day_of_week == WeekdayInt.WEDNESDAY:
        print("IntEnum")

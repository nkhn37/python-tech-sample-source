"""列挙型 enumの使い方の基本
auto()で初期値を指定する方法

[説明ページ]
https://tech.nkhn37.net/python-enum-basics/#auto-3
"""
from enum import Enum, auto


class Weekday(Enum):
    """曜日列挙クラス auto()で自動設定"""

    SUNDAY = 100
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()


if __name__ == "__main__":
    print(Weekday.SUNDAY, Weekday.SUNDAY.name, Weekday.SUNDAY.value)
    print(Weekday.MONDAY, Weekday.MONDAY.name, Weekday.MONDAY.value)
    print(Weekday.TUESDAY, Weekday.TUESDAY.name, Weekday.TUESDAY.value)
    print(Weekday.WEDNESDAY, Weekday.WEDNESDAY.name, Weekday.WEDNESDAY.value)
    print(Weekday.THURSDAY, Weekday.THURSDAY.name, Weekday.THURSDAY.value)
    print(Weekday.FRIDAY, Weekday.FRIDAY.name, Weekday.FRIDAY.value)
    print(Weekday.SATURDAY, Weekday.SATURDAY.name, Weekday.SATURDAY.value)

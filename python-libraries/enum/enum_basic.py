"""列挙型 enumの使い方の基本
Enumを継承した列挙型の定義

[説明ページ]
https://tech.nkhn37.net/python-enum-basics/#Enum
"""
from enum import Enum


class Weekday(Enum):
    """曜日列挙クラス"""

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


if __name__ == "__main__":
    print(Weekday.SUNDAY, Weekday.SUNDAY.name, Weekday.SUNDAY.value)
    print(Weekday.MONDAY, Weekday.MONDAY.name, Weekday.MONDAY.value)
    print(Weekday.TUESDAY, Weekday.TUESDAY.name, Weekday.TUESDAY.value)
    print(Weekday.WEDNESDAY, Weekday.WEDNESDAY.name, Weekday.WEDNESDAY.value)
    print(Weekday.THURSDAY, Weekday.THURSDAY.name, Weekday.THURSDAY.value)
    print(Weekday.FRIDAY, Weekday.FRIDAY.name, Weekday.FRIDAY.value)
    print(Weekday.SATURDAY, Weekday.SATURDAY.name, Weekday.SATURDAY.value)

    # 列挙型は判定等で使用することが可能
    day_of_week = Weekday.WEDNESDAY
    match day_of_week:
        case Weekday.SUNDAY:
            print("日曜日")
        case Weekday.MONDAY:
            print("月曜日")
        case Weekday.TUESDAY:
            print("火曜日")
        case Weekday.WEDNESDAY:
            print("水曜日")
        case Weekday.THURSDAY:
            print("木曜日")
        case Weekday.FRIDAY:
            print("金曜日")
        case Weekday.SATURDAY:
            print("土曜日")
        case _:
            print("曜日ではありません")

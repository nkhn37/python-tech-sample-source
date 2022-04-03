"""カレンダーを作成する方法 calendarモジュール
最初の曜日を指定する setfirstweekday

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#_month
"""
import calendar

# setfirstweekdayでカレンダーの最初になる曜日を指定する。（デフォルトは月曜）
# 0:月 1:火 2:水 3:木 4:金 5:土 6:日

# 日曜を最初に設定する
calendar.setfirstweekday(6)
print(calendar.month(2022, 1, 4))

# （あまり使う機会はないかもしれないが）火曜を最初に設定する
calendar.setfirstweekday(1)
print(calendar.month(2022, 1, 4))

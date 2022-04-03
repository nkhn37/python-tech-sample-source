"""カレンダーを作成する方法 calendarモジュール
指定した期間の閏年の回数を返す

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#_leapdays
"""
import calendar

# 閏年の回数を調べる
print(calendar.leapdays(2000, 2022))

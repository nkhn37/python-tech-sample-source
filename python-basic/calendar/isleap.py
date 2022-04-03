"""カレンダーを作成する方法 calendarモジュール
閏年か判定する isleap

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#_isleap
"""
import calendar

# 閏年を判定する
print(calendar.isleap(2020))
print(calendar.isleap(2022))

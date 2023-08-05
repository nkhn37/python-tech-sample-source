"""カレンダーを作成する方法 calendarモジュール
年間カレンダーの生成 calendarの引数指定

m:1行に表示する月数
c:月と月の間の幅
w:列幅
l:行幅

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#1
"""
import calendar

# 年間カレンダーを出力する　1行の月数や各種幅を指定
print(calendar.calendar(2023, m=2, c=5, w=3, l=2))

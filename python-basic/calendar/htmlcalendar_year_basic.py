"""カレンダーを作成する方法 calendarモジュール
年間カレンダーをHTMLで取得 HTMLCalendar

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#HTML-4
"""
import calendar

# HTMLCalendarオブジェクトを生成
html_calendar = calendar.HTMLCalendar()

# 年間カレンダーをHTMLで取得
print(html_calendar.formatyear(2023))

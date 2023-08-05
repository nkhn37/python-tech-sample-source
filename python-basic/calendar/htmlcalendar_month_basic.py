"""カレンダーを作成する方法 calendarモジュール
月間カレンダーをHTMLで取得 HTMLCalendar

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#HTML-2
"""
import calendar

# HTMLCalendarオブジェクトを生成
html_calendar = calendar.HTMLCalendar()

# 月間カレンダーをHTMLで取得
print(html_calendar.formatmonth(2023, 1))

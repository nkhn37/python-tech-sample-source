"""カレンダーを作成する方法 calendarモジュール
年間カレンダーをHTMLで取得 HTMLCalendar
1行に表示する月数を指定

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#HTML1
"""
import calendar

# HTMLCalendarオブジェクトを生成
html_calendar = calendar.HTMLCalendar()

# n年間カレンダーをHTMLで取得(1行に表示する月数を指定)
print(html_calendar.formatyear(2023, width=2))

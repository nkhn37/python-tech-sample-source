"""カレンダーを作成する方法 calendarモジュール
月間カレンダーをHTMLで取得 HTMLCalendar
最初の曜日を指定する firstweekday引数

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#HTML-3
"""
import calendar

# HTMLCalendarオブジェクトを生成
# firstweekday引数でカレンダーの最初になる曜日を指定する。（デフォルトは月曜）
# 0:月 1:火 2:水 3:木 4:金 5:土 6:日
html_calendar = calendar.HTMLCalendar(firstweekday=6)

# 日曜を最初に設定する
print(html_calendar.formatmonth(2023, 1))

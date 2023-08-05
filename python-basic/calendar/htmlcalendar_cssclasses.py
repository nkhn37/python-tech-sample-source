"""カレンダーを作成する方法 calendarモジュール
CSSクラスの設定 cssclasses

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#CSS
"""
import calendar

# HTMLCalendarオブジェクトを生成
html_calendar = calendar.HTMLCalendar()

# CSSクラスを取得
print(html_calendar.cssclasses)
# python3.7から用意されたCSSクラス名
print(html_calendar.cssclass_year)
print(html_calendar.cssclass_month)
print(html_calendar.cssclass_noday, "\n")

# CSSクラスを設定
html_calendar.cssclasses = [
    "mon",
    "tue",
    "wed",
    "thu_1",
    "fri_1",
    "sat_1",
    "sun_1",
]

# 月間カレンダーをHTMLで取得
print(html_calendar.formatyear(2023))

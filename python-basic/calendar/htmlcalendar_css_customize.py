"""カレンダーを作成する方法 calendarモジュール
HTML出力でcssをカスタマイズする例 (公式ドキュメントから引用)

[calendar公式ドキュメント]
https://docs.python.org/ja/3/library/calendar.html#module-calendar

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#CSS
"""
import calendar


class CustomHTMLCal(calendar.HTMLCalendar):
    cssclasses = [
        style + " text-nowrap" for style in calendar.HTMLCalendar.cssclasses
    ]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"


if __name__ == "__main__":
    # カスタムHTMLCalendarオブジェクトを生成
    custom_html_calendar = CustomHTMLCal()

    # 月間カレンダーをHTMLで取得
    print(custom_html_calendar.formatmonth(2023, 1))

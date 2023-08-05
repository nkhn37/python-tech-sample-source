"""カレンダーを作成する方法 calendarモジュール
月間カレンダーをリストで取得する monthcalendar

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#_monthcalendar
"""
import calendar

# monthcalendar関数でカレンダーをリストとして取得する
calendar_list = calendar.monthcalendar(2022, 1)
print(calendar_list)

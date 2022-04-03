"""カレンダーを作成する方法 calendarモジュール
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-calendar-basic/#_month
"""
import calendar

# カレンダー形式で出力する
# (第1引数：「年」、第2引数：「月」、第3引数：「1日を表現する文字幅」)
print(calendar.month(2022, 1, 4))

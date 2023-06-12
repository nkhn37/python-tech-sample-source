"""日付・時刻
timeのみの加算・減算はできない
TypeErrorが発生する例

[説明ページ]
https://tech.nkhn37.net/python-datetime-calculation/#_time
"""
# timeのみの加算、減算はできない
import datetime

t = datetime.time(0, 0, 0)
# 加算する
t_plus = t + datetime.timedelta(hours=1, minutes=30, seconds=30)
# 減算する
t_minus = t - datetime.timedelta(hours=1, minutes=30, seconds=30)

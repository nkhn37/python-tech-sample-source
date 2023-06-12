"""日付・時刻
timeのみの差分計算はできない
TypeErrorが発生する例

[説明ページ]
https://tech.nkhn37.net/python-datetime-calculation/#_time-2
"""
# time同士の差分をとることはできない
import datetime

t1 = datetime.time(12, 30, 30)
t2 = datetime.time(0, 0, 0)
# 差分を求める
t_diff = t1 - t2

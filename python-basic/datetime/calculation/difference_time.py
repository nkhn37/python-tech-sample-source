"""日付・時刻
timeのみの差分計算はできない
回避する方法：timeをdatetimeに変換してから差分を計算

[説明ページ]
https://tech.nkhn37.net/python-datetime-calculation/#time-2
"""
import datetime

# 仮の日付を作成する
dt = datetime.datetime(2022, 1, 1)
# timeをdatetimeに変換する
t1 = datetime.datetime.combine(dt, datetime.time(12, 0, 0))
t2 = datetime.datetime.combine(dt, datetime.time(0, 0, 0))
# 差分を求める
t_diff = t1 - t2

print('=== timeの差分')
print(t_diff)
print(type(t_diff))
print(t_diff.days)
print(t_diff.seconds)

"""日付・時刻
timeのみの加算・減算はできない
回避する方法：timeをdatetimeに変換してからtimedeltaで計算

[説明ページ]
https://tech.nkhn37.net/python-datetime-calculation/#time
"""
import datetime

# 仮の日付を作成する
dt = datetime.datetime(2022, 1, 1)
# timeをdatetimeに変換する
t = datetime.datetime.combine(dt, datetime.time(0, 0, 0))
# 加算する
t_plus = t + datetime.timedelta(hours=1, minutes=30, seconds=30)
# 減算する
t_minus = t - datetime.timedelta(hours=1, minutes=30, seconds=30)

print('=== timeの加算や減算')
# timeクラスとして使用したい場合
print(datetime.time(t.hour, t.minute, t.second))
print(datetime.time(t_plus.hour, t_plus.minute, t_plus.second))
print(datetime.time(t_minus.hour, t_minus.minute, t_minus.second))

# 文字列として時刻を使用する場合
print(t.strftime('%H:%M:%S'))
print(t_plus.strftime('%H:%M:%S'))
print(t_minus.strftime('%H:%M:%S'))

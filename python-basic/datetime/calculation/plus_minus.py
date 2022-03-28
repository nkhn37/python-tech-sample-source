"""日付・時刻
日付・時刻の加算・減算

[説明ページ]
https://tech.nkhn37.net/python-datetime-calculation/#i-2
"""
import datetime

# ===== datetimeの加算や減算
dt = datetime.datetime(2022, 1, 1, 0, 0, 0, 0)
# 加算する
dt_plus = dt + datetime.timedelta(weeks=1, days=5, hours=10)
# 減算する
dt_minus = dt - datetime.timedelta(weeks=1, days=5, hours=10)

print('=== datetimeの加算や減算')
print(dt)
print(dt_plus)
print(dt_minus)

# ===== dateの加算や減算
d = datetime.date(2021, 1, 1)
# 加算する
d_plus = d + datetime.timedelta(weeks=1, days=5)
# 減算する
d_minus = d - datetime.timedelta(weeks=1, days=5)

print('=== dateの加算や減算')
print(d)
print(d_plus)
print(d_minus)

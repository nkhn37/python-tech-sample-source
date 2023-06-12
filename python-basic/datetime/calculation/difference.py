"""日付・時刻
日付・時刻の差分計算

[説明ページ]
https://tech.nkhn37.net/python-datetime-calculation/#i-4
"""
import datetime

# ===== datetimeの差分
dt1 = datetime.datetime(2022, 3, 1, 18, 30, 45, 500)
dt2 = datetime.datetime(2022, 1, 1, 12, 15, 15, 250)
# 差分を求める
dt_diff = dt1 - dt2

print("=== datetimeの差分")
print(dt_diff)
print(type(dt_diff))
print(dt_diff.days)
print(dt_diff.seconds)

# ===== dateの差分
d1 = datetime.date(2022, 3, 1)
d2 = datetime.date(2022, 1, 1)
# 差分を求める
d_diff = d1 - d2

print("=== dateの差分")
print(d_diff)
print(type(d_diff))
print(d_diff.days)
print(d_diff.seconds)

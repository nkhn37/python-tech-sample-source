"""日付・時刻
日付・時刻の比較をする

[説明ページ]
https://tech.nkhn37.net/python-datetime-calculation/#i-5
"""
import datetime

# ===== datetimeの比較
dt1 = datetime.datetime(2022, 1, 1, 0, 0, 0, 0)
dt2 = datetime.datetime(2022, 3, 1, 12, 30, 30, 0)

# 日時を比較する
print("=== datetimeの比較")
print(dt1 < dt2)
print(dt1 > dt2)

# ===== dateの比較
d1 = datetime.date(2021, 2, 1)
d2 = datetime.date(2021, 3, 1)

# 日付を比較する
print("=== dateの比較")
print(d1 < d2)
print(d1 > d2)

# ===== timeの比較
t1 = datetime.time(0, 0, 0)
t2 = datetime.time(12, 30, 30)

# 時刻を比較する
print("=== timeの比較")
print(t1 < t2)
print(t1 > t2)

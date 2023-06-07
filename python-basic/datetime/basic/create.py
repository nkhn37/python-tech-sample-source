"""日付・時刻
日付・時刻を指定してインスタンスを生成する方法

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#i-2
"""
import datetime

# === 日付、時刻を指定して生成する
print(datetime.datetime(2021, 1, 1, 0, 0, 0, 0))
# タイムゾーンを指定する
print(
    datetime.datetime(2021, 1, 1, 0, 0, 0, 0),
    datetime.timezone(datetime.timedelta(hours=9)),
)

# === 日付を指定して生成する ※dateクラスはタイムゾーンを指定できないので注意
print(datetime.date(2021, 1, 1))

# === 時刻を指定して生成する
print(datetime.time(0, 0, 0, 0))
# タイムゾーンを指定する
print(
    datetime.time(0, 0, 0, 0), datetime.timezone(datetime.timedelta(hours=9))
)

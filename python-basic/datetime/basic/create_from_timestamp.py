"""日付・時刻
日付・時刻のタイムスタンプからインスタンスを生成する方法

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#i-4
"""
import datetime

dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
# タイムスタンプを取得する
ts = dt.timestamp()
print(dt)
print(ts)

# タイムスタンプから日付、時刻を取得する
print(datetime.datetime.fromtimestamp(ts))
# タイムゾーンを指定する場合
print(
    datetime.datetime.fromtimestamp(
        ts, datetime.timezone(datetime.timedelta(hours=9))
    )
)
# UTCを指定する場合
print(datetime.datetime.fromtimestamp(ts, datetime.timezone.utc))

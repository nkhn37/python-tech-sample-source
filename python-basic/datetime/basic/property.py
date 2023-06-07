"""日付・時刻
日付・時刻の要素を抽出する方法
プロパティでアクセスする

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#i-7
"""
import datetime

# dt = datetime.datetime.now()
dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
print(dt)

print("===")
# 年を取得する
print(dt.year)
# 月を取得する
print(dt.month)
# 日を取得する
print(dt.day)
# 時を取得する
print(dt.hour)
# 分を取得する
print(dt.minute)
# 秒を取得する
print(dt.second)
# マイクロ秒を取得する
print(dt.microsecond)
# タイムゾーンを取得する
print(dt.tzinfo)

"""日付・時刻
日付・時刻の要素を抽出する方法
メソッドでアクセスする

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#i-8
"""
import datetime

# dt = datetime.datetime.now()
dt = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9)))
print(dt)

print('===')
# dateメソッド
print(dt.date())
# timeメソッド
print(dt.time())
# timetzメソッド
print(dt.timetz())
# timestampメソッド
print(dt.timestamp())
# weekdayメソッド
print(dt.weekday())
# isoweekdayメソッド
print(dt.isoweekday())
# isocalendarメソッド
print(dt.isocalendar())

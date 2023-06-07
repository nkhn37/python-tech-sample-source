"""日付・時刻
datetimeの基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#i
"""
import datetime

# 今日の日時を表示する
print(datetime.datetime.today())

# 今日の日付を表示する
print(datetime.date.today())

# 現在の日時を表示する
print(datetime.datetime.now())

# timezoneを指定する（日本標準時）
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))))

# 標準時を表示する
print(datetime.datetime.utcnow())

# 標準時でtimezoneで指定する
print(datetime.datetime.now(datetime.timezone.utc))

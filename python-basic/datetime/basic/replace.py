"""日付・時刻
日付・時刻の一部を置き換える方法 replace

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#i-5
"""
import datetime

dt = datetime.datetime.now()
print(dt)

print("===")
# 年を変更する
print(dt.replace(year=2020))
# 月を変更する
print(dt.replace(month=1))
# 日を変更する
print(dt.replace(day=1))
# 時を変更する
print(dt.replace(hour=1))
# 分を変更する
print(dt.replace(minute=1))
# 秒を変更する
print(dt.replace(second=1))
# マイクロ秒を変更する
print(dt.replace(microsecond=123))
# タイムゾーンを変更する
print(dt.replace(tzinfo=datetime.timezone.utc))

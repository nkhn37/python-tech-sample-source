"""日付・時刻
日付・時刻の文字列からインスタンスを生成する方法 strptime

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#i-3
"""
import datetime

# 日付フォーマットを指定して文字列から生成する
dt = datetime.datetime.strptime('2022/1/1 01:23:45', '%Y/%m/%d %H:%M:%S')
print(dt)

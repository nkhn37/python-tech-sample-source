"""日付・時刻
日付・時刻を指定してインスタンスを生成する方法
fromisocalendarを使用した方法 (バージョン3.8で追加)

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#ISO_fromisocalendar_38
"""
import datetime

# ISOカレンダーを使って生成する
dt = datetime.datetime.fromisocalendar(2022, 10, 1)
print(dt)

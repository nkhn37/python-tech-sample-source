"""日付・時刻
日付・時刻の文字列からインスタンスを生成する方法
fromisoformatを使用した方法 (バージョン3.7で追加)

[説明ページ]
https://tech.nkhn37.net/python-datetime-basic/#ISO_fromisoformat_37
"""
import datetime

# ISOフォーマットの文字列から生成する
dt = datetime.datetime.fromisoformat("2022-01-01 01:23:45+09:00")
print(dt)

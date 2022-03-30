"""日付・時刻
日付や時刻を整形する strftime, setlocale

[説明ページ]
https://tech.nkhn37.net/python-datetime-strftime-setlocale/#_strftime_setlocale
"""
import datetime
import locale

# ロケール(地域)情報を設定する
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

# 日時情報を設定する
dt = datetime.datetime(2022, 1, 1, 12, 30, 30, 500)

# 日時情報を整形して表示する
print(dt)
print(dt.strftime('%c'))
print(dt.strftime('%x'))
print(dt.strftime('%X'))
print(dt.strftime('%Y年%m月%d日 %H時%M分%S秒'))

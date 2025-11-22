"""文字列基礎
formatやf-stringにおける書式指定の例
(日付の表示)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#_datetime
"""

import datetime

dt = datetime.datetime(2023, 1, 2, 12, 30, 30)

print("----- 日付の表示")
print("format  : {}".format(dt))
print(f"f-string: {dt}")

print("-----日付フォーマットの指定")
print("format  : {:%Y/%m/%d %I:%M:%S, %A, %p}".format(dt))
print(f"f-string: {dt:%Y/%m/%d %I:%M:%S, %A, %p}")

print("----- ISOフォーマットでの表示")
print("format  : {}".format(dt.isoformat()))
print(f"f-string: {dt.isoformat()}")

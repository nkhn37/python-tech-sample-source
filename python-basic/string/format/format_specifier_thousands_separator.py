"""文字列基礎
formatやf-stringにおける書式指定の例
(桁区切りの表示)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-11
"""
num = 1000000.123456

print("----- 桁区切りの表示 (カンマ ,)")
print("format  : {:,}".format(num))
print(f"f-string: {num:,}")

print("----- 桁区切りの表示 (アンダーバー _) ※Python3.6で追加")
print("format  : {:_}".format(num))
print(f"f-string: {num:_}")

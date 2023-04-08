"""文字列基礎
formatやf-stringにおける書式指定の例
(ゼロ埋め)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-12
"""
print("----- ゼロ埋め (正の数)")
num = 100
print("format  : {:0=10}".format(num))
print(f"f-string: {num:0=10}")
# ゼロ埋めの場合=は省略可能
print("format  : {:010}".format(num))
print(f"f-string: {num:010}")

print("----- ゼロ埋め (負の数)")
num = -100
print("format  : {:0=10}".format(num))
print(f"f-string: {num:0=10}")
# ゼロ埋めの場合=は省略可能
print("format  : {:010}".format(num))
print(f"f-string: {num:010}")

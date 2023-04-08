"""文字列基礎
formatやf-stringにおける書式指定の例
(左寄せ、中央寄せ、右寄せ)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-8
"""
num = 100

print("----- 左寄せ")
print("format  : {:<10}".format(num))
print(f"f-string: {num:<10}")

print("----- 中央寄せ")
print("format  : {:^10}".format(num))
print(f"f-string: {num:^10}")

print("----- 右寄せ")
print("format  : {:>10}".format(num))
print(f"f-string: {num:>10}")

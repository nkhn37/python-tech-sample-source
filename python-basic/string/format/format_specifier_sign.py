"""文字列基礎
formatやf-stringにおける書式指定の例
(符号を表示)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-10
"""
num1 = 100
num2 = -100

print("----- 符号(プラスを表示)")
print("format  : {:+}".format(num1))
print(f"f-string: {num1:+}")
print("format  : {:+}".format(num2))
print(f"f-string: {num2:+}")

print("----- 符号 (スペースで符号位置を揃える)")
print("format  : {: }".format(num1))
print(f"f-string: {num1: }")
print("format  : {: }".format(num2))
print(f"f-string: {num2: }")

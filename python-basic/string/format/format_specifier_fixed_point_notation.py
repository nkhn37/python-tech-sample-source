"""文字列基礎
formatやf-stringにおける書式指定の例
(小数点以下の桁数指定 f, F)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-13
"""
num = 0.00000123456

print("----- 値によって自動で指数表記となる")
print("format  : {}".format(num))
print(f"f-string: {num}")

print("----- 固定小数点表記で表示 (デフォルトは小数点以下6桁)")
print("format  : {:f}".format(num))
print(f"f-string: {num:f}")

print("----- 小数点以下の桁数指定 (桁数を指定)")
print("format  : {:.15f}".format(num))
print(f"f-string: {num:.15f}")

num1 = 0.0014
num2 = 0.0015
num3 = 0.0016
print("----- 固定小数点表記で表示 (四捨五入)")
print("format  : {:.3f}".format(num1))
print(f"f-string: {num1:.3f}")
print("format  : {:.3f}".format(num2))
print(f"f-string: {num2:.3f}")
print("format  : {:.3f}".format(num3))
print(f"f-string: {num3:.3f}")

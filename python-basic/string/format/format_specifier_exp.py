"""文字列基礎
formatやf-stringにおける書式指定の例
(指数表記 e, E)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#_e_E
"""
num1 = 0.0000123456
num2 = 123456

print("----- 指数表記 (デフォルトは小数点以下6桁)")
print("format  : {:e}".format(num1))
print(f"f-string: {num1:e}")
print("format  : {:e}".format(num2))
print(f"f-string: {num2:e}")

print("----- 小数点以下の桁数を指定")
print("format  : {:.3e}".format(num1))
print(f"f-string: {num1:.3e}")
print("format  : {:.3e}".format(num2))
print(f"f-string: {num2:.3e}")

print("----- Eとすると表記が大文字になる")
print("format  : {:.3E}".format(num1))
print(f"f-string: {num1:.3E}")
print("format  : {:.3E}".format(num2))
print(f"f-string: {num2:.3E}")

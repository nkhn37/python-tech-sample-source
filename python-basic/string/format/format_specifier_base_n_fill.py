"""文字列基礎
formatやf-stringにおける書式指定の例
(2進数、8進数、16進数 + ゼロ埋め)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#2816-2
"""
num = 255

print("----- 2進数表記")
print("format  : {:0=10b}".format(num))
print(f"f-string: {num:0=10b}")

print("----- 8進数表記")
print("format  : {:0=10o}".format(num))
print(f"f-string: {num:0=10o}")

print("----- 16進数表記 (小文字)")
print("format  : {:0=10x}".format(num))
print(f"f-string: {num:0=10x}")

print("----- 16進数表記 (大文字)")
print("format  : {:0=10X}".format(num))
print(f"f-string: {num:0=10X}")

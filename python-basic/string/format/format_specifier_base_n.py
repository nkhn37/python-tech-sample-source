"""文字列基礎
formatやf-stringにおける書式指定の例
(2進数、8進数、16進数)

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#2816
"""
num = 255

print("----- 2進数表記")
print("format  : {:b}".format(num))
print(f"f-string: {num:b}")

print("----- 8進数表記")
print("format  : {:o}".format(num))
print(f"f-string: {num:o}")

print("----- 16進数表記 (小文字)")
print("format  : {:x}".format(num))
print(f"f-string: {num:x}")

print("----- 16進数表記 (大文字)")
print("format  : {:X}".format(num))
print(f"f-string: {num:X}")

"""文字列基礎
formatやf-stringにおける書式指定の例
(パーセント表記(%))

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-14
"""
num = 0.15

print("----- パーセント表記(%)")
print("format  : {:%}".format(num))
print(f"f-string: {num:%}")

print("----- 小数点以下の桁数を指定")
print("format  : {:.2%}".format(num))
print(f"f-string: {num:.2%}")

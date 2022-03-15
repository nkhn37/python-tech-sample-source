"""文字列基礎
文字列を数値に変換する方法
上付き数字や下付き数字を数値変換したい場合

[説明ページ]
https://tech.nkhn37.net/python-str-num-translation/#unicodedatadigit
"""
import unicodedata

# unicodedata.digitを用いた変換
# 上付き数字／下付き数字の変換
num1 = unicodedata.digit('⁰')
print(num1)
num2 = unicodedata.digit('₁')
print(num2)

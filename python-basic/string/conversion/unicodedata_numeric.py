"""文字列基礎
文字列を数値に変換する方法
上付き数字や下付き数字だけでなく、漢数字やローマ数字も数値変換したい場合

[説明ページ]
https://tech.nkhn37.net/python-str-num-translation/#unicodedatanumeric
"""
import unicodedata

# unicodedata.numericを用いた変換
# 上付き数字／下付き数字の変換
num1 = unicodedata.numeric('⁰')
print(num1)
num2 = unicodedata.numeric('₁')
print(num2)
# 漢数字の変換
num3 = unicodedata.numeric('弐')
print(num3)
# ローマ数字の変換
num4 = unicodedata.numeric('Ⅲ')
print(num4)

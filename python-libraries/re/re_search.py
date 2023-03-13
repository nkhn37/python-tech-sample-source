"""正規表現モジュール re の使い方
searchメソッドを用いた正規表現の抽出

[説明ページ]
https://tech.nkhn37.net/python-re-regular-expression/#search
"""
import re

text1 = "電話番号は、090-1111-2222です。"
text2 = "電話番号は、0123-45-6789です。"

# 正規表現をcompileで準備する
# \を使うのでrのraw文字列として引数に設定する
ptrn = re.compile(r"(\d{2,4})-(\d{2,4})-(\d{4})")

# 文字列を検索し、結果を表示する
result1 = ptrn.search(text1)
print(type(result1))
if result1:
    # 引数なしはヒットした全体を表示。result.group(0)でも同じ
    print(result1.group())
    # 1番目の部分文字列
    print(result1.group(1))
    # 2番目の部分文字列
    print(result1.group(2))
    # 3番目の部分文字列
    print(result1.group(3))
else:
    print("一致なし")

print("=====")
# Python 3.8以降であればセイウチ演算子を使ってもよい
if result2 := ptrn.search(text2):
    print(result2.group())
    print(result2.group(1))
    print(result2.group(2))
    print(result2.group(3))
else:
    print("一致なし")

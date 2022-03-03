"""正規表現モジュール re の使い方
オプション：単一行モードを有効にする (DOTALL)

[説明ページ]
https://tech.nkhn37.net/python-re-options/#DOTALL
"""
import re

text = '単一行モードを使用すると\n' \
       '改行コードを含めて抽出できる'

# 単一行モードを有効にしない場合
ptrn1 = re.compile(r'^.+')

if result1 := ptrn1.search(text):
    print(result1.group())

print('=====')
# 単一行モードを有効にした場合
ptrn2 = re.compile(r'^.+', re.DOTALL)

if result2 := ptrn2.search(text):
    print(result2.group())

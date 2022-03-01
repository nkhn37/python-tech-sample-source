"""正規表現モジュール re の使い方
matchメソッドを用いた正規表現の抽出

[説明ページ]
https://tech.nkhn37.net/python-re-regular-expression/#match
"""
import re

text1 = '090-1111-2222が電話番号です。'
text2 = '電話番号は、0123-45-6789です。'

ptrn = re.compile(r'(\d{2,4})-(\d{2,4})-(\d{4})')

result1 = ptrn.match(text1)
if result1:
    print(result1.group())
    print(result1.group(1))
    print(result1.group(2))
    print(result1.group(3))
else:
    print('一致なし')

print('=====')
if result2 := ptrn.match(text2):
    print(result2.group())
    print(result2.group(1))
    print(result2.group(2))
    print(result2.group(3))
else:
    print('一致なし')

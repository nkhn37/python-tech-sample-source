"""正規表現モジュール re の使い方
finditerメソッドで正規表現に一致する全ての文字列を抽出する

[説明ページ]
https://tech.nkhn37.net/python-re-regular-expression/#finditer
"""
import re

text = '私の電話は0123-45-6789で、携帯は090-1111-2222です。' \
       'Aさんの電話は9876-54-3210で、携帯は080-3333-4444です。'

# パターンを設定
ptrn1 = re.compile(r'(\d{2,4})-(\d{2,4})-(\d{4})')

# マッチする文字列を全て検索
match_texts = ptrn1.finditer(text)
print(type(match_texts))
for match_text in match_texts:
    print('=====')
    print(match_text.group())
    print(match_text.group(1))
    print(match_text.group(2))
    print(match_text.group(3))

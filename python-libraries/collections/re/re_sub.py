"""正規表現モジュール re の使い方
subメソッドを用いた一致文字列の置換

[説明ページ]
https://tech.nkhn37.net/python-re-split-sub/#sub
"""
import re

text = '私の電話は0123-45-6789で、携帯は090-1111-2222です。' \
       'Aさんの電話は9876-54-3210で、携帯は080-3333-4444です。'

# パターンを設定
ptrn1 = re.compile(r'\d{2,4}-\d{2,4}-\d{4}')

# 一致する文字列を置換する
replaced_text1 = ptrn1.sub('XXX-XXXX-XXXX', text)
print(replaced_text1)

print('=====')
text = '私の電話は0123-45-6789で、携帯は090-1111-2222です。' \
       'Aさんの電話は9876-54-3210で、携帯は080-3333-4444です。'

# 置換する数を指定する
replaced_text2 = ptrn1.sub('XXX-XXXX-XXXX', text, 2)
print(replaced_text2)

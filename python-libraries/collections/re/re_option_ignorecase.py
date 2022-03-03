"""正規表現モジュール re の使い方
オプション：大文字／小文字を区別しない (IGNORECASE)

[説明ページ]
https://tech.nkhn37.net/python-re-options/#IGNORECASE
"""
import re

text = 'メールアドレスは、user_01@test.comと' \
       'プライベート用のUSER_02@test.co.jpを使用しています。'

ptrn = re.compile(r'([a-z0-9_.+-]+)@'
                  r'([a-z0-9][a-z0-9-]*[a-z0-9]*\.)+[a-z]{2,}',
                  re.IGNORECASE)

results = ptrn.finditer(text)
for result in results:
    print(result.group())

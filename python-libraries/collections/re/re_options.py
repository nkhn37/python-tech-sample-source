"""正規表現モジュール re の使い方
オプション：複数オプション値を同時に使用する

[説明ページ]
https://tech.nkhn37.net/python-re-options/#i-2
"""
import re

text = 'user_01@test.com: 会社メールアドレス\n' \
       'USER_02@test.co.jp: プライベート用メールアドレス'

ptrn = re.compile(r'^([a-z0-9_.+-]+)@'
                  r'([a-z0-9][a-z0-9-]*[a-z0-9]*\.)+[a-z]{2,}',
                  re.IGNORECASE | re.MULTILINE)

results = ptrn.finditer(text)
for result in results:
    print(result.group())

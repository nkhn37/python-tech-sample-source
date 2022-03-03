"""正規表現モジュール re の使い方
オプション：空行／コメントを付与して正規表現を見やすくする (VERBOSE)

[説明ページ]
https://tech.nkhn37.net/python-re-options/#VERBOSE
"""
import re

text = '私のメールアドレスは、user_01@test.comです。'

ptrn = re.compile(r'''([a-z0-9_.+-]+) #local
                      @ #delimiter
                      ([a-z0-9][a-z0-9-]*[a-z0-9]*\.)+[a-z]{2,} #domain''',
                  re.VERBOSE)

if result := ptrn.search(text):
    print(result.group())


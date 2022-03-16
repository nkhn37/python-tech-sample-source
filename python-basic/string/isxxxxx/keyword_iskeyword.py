"""文字列基礎
予約済み識別子か判定する
keywordモジュールのiskeyword

[説明ページ]
https://tech.nkhn37.net/python-keyword-iskeyword/
"""
import keyword

id_str1 = 'python'
id_str2 = 'class'

print(f'{id_str1}の判定')
print(f'identifier: {id_str1.isidentifier()}')
print(f'iskeyword: {keyword.iskeyword(id_str1)}')
print(f'{id_str2}の判定')
print(f'identifier: {id_str2.isidentifier()}')
print(f'iskeyword: {keyword.iskeyword(id_str2)}')

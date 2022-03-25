"""文字列基礎
フォーマット済み文字列リテラル(f-string)の使い方
※ python 3.6 で追加

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#_Python_36
"""
# フォーマット文字列の使い方
name = '太郎'
sex = '男性'
age = 20

# f-stringで値を埋め込む
print(f'{name}は{age}歳の{sex}です。')
print(f'{name}は{age*2}歳の{sex}です。')

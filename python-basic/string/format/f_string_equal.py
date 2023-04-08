"""文字列基礎
フォーマット済み文字列リテラル(f-string)の使い方
「=」で変数や式を含めて表示する方法
※ python 3.8 で追加

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-6
"""
# フォーマット文字列で変数や式を表示する方法
name = "太郎"
sex = "男性"
age = 20

# f-stringで変数や式を含めて表示する方法
print(f"{name=}は{age=}歳の{sex=}です。")
print(f"{name=}は{age*2=}歳の{sex=}です。")

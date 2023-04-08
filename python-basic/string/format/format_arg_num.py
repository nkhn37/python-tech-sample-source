"""文字列基礎
引数の番号を指定して値を埋め込む方法

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-3
"""
# 引数の番号を指定して値を埋め込む
print("{0}は{2}歳の{1}です。".format("太郎", "男性", 20))

# 変数に値を入れて使用する場合も同様
name = "太郎"
sex = "男性"
age = 20
print("{0}は{2}歳の{1}です。".format(name, sex, age))

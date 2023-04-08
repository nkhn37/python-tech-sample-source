"""文字列基礎
先頭から引数の値を順に埋め込む方法

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-2
"""
# 先頭から引数の値を順に埋め込む
print("{}の性別は{}で、年齢は{}歳です。".format("太郎", "男性", 20))

# 変数に値を入れて使用する場合も同様
name = "太郎"
sex = "男性"
age = 20
print("{}の性別は{}で、年齢は{}歳です。".format(name, sex, age))

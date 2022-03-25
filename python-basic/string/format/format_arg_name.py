"""文字列基礎
引数に名前をつけて値を埋め込む方法

[説明ページ]
https://tech.nkhn37.net/python-str-format-f-string/#i-3
"""
# 引数を名前付けして値を埋め込む
print('{name}は{age}歳の{sex}です。'.format(name='太郎', sex='男性', age=20))

# 変数に値を入れて使用する場合も同様
name1 = '太郎'
sex1 = '男性'
age1 = 20
print('{name}は{age}歳の{sex}です。'.format(name=name1, sex=sex1, age=age1))

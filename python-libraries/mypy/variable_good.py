"""mypyを使用した型チェックの方法
変数の型チェック(型チェックが問題ない場合)

[説明ページ]
https://tech.nkhn37.net/python-mypy-type-annotation-check/#i
"""
# intの型アノテーション
x: int = 10
print(x)

# 異なる型(str)を代入する
x = 20
print(x)

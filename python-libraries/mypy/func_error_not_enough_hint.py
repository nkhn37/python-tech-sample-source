"""mypyを使用した型チェックの方法
設定ファイルによるカスタマイズ

[説明ページ]
https://tech.nkhn37.net/python-mypy-type-annotation-check/#i-3
"""


# 型アノテーションを指定する場合
# アノテーションの指定が不十分
def func_annotation(x: int, y):
    return x * y


if __name__ == "__main__":
    val1 = "test"
    val2 = 3
    print(func_annotation(val1, val2))

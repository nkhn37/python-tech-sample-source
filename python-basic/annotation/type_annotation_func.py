"""型ヒント（変数・関数の型アノテーション）の基本
関数の型アノテーション

[説明ページ]
https://tech.nkhn37.net/python-type-annotation-basic/#i-7
"""


# 型アノテーションを指定しない場合
def func(x, y):
    return x * y


# 型アノテーションを指定する場合
def func_annotation(x: int, y: int) -> int:
    return x * y


if __name__ == "__main__":
    val1 = 10
    val2 = 20
    print(func(val1, val2))
    print(func_annotation(val1, val2))

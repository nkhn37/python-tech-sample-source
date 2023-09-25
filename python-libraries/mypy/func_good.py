"""mypyを使用した型チェックの方法
関数の型チェック(型チェックが問題ない場合)

[説明ページ]
https://tech.nkhn37.net/python-mypy-type-annotation-check/#i-2
"""


def func_annotation(x: int, y: int) -> int:
    return x * y


if __name__ == "__main__":
    val1 = 10
    val2 = 3

    # 正しい型で使用する
    print(func_annotation(val1, val2))

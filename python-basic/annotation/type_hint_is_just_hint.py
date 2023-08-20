"""型ヒント（変数・関数の型アノテーション）の基本
Pythonの型ヒントはただの注釈でしかない

[説明ページ]
https://tech.nkhn37.net/python-type-annotation-basic/#Python
"""


def func_annotation(x: int, y: int) -> int:
    return x * y


if __name__ == "__main__":
    # 型アノテーションに従った使用方法
    val1 = 10
    val2 = 20
    print(func_annotation(val1, val2))

    # Pythonの型ヒントはただの注釈でしかないため強制力はない
    val1 = "test"
    val2 = 3
    print(func_annotation(val1, val2))

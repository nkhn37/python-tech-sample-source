"""型ヒント（変数・関数の型アノテーション）の基本
__annotations__属性

[説明ページ]
https://tech.nkhn37.net/python-type-annotation-basic/#__annotations
"""


# 型アノテーションを指定する場合
def func_annotation(x: int, y: int) -> int:
    return x * y


if __name__ == "__main__":
    print(func_annotation.__annotations__)

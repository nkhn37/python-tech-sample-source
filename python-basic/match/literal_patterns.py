"""構造的パターンマッチ (match case) の使い方
リテラルパターン(Literal Patterns)の場合

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#Literal_Patterns
"""


def check(data):
    match data:
        case 1:
            print("失敗")
        case 2:
            print("成功")
        case _:
            print("値は不適切です。")


if __name__ == "__main__":
    value = 1
    check(value)

    print("---")
    value = 2
    check(value)

    print("---")
    value = 3
    check(value)

    print("---")
    value = "test"
    check(value)

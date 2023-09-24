"""構造的パターンマッチ (match case) の使い方
ワイルドカードパターン(Wildcard Patterns)の場合

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#Wildcard_Patterns
"""


def show(data):
    match data:
        case _:
            print(data)


if __name__ == "__main__":
    value = 1
    show(value)

    print("---")
    value = "test"
    show(value)

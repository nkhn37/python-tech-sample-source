"""構造的パターンマッチ (match case) の使い方
キャプチャパターン(Capture Patterns)の場合

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#Capture_Patterns
"""


def check(data):
    match data:
        case 1:
            print("失敗")
        case x:
            print(f"成功: {x}")

    # 以下のような書き方をしてしまうと「case 1:」に到達しない
    # match value:
    #     case x:
    #         print(f"成功: {x}")
    #     case 1:
    #         print("失敗")


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

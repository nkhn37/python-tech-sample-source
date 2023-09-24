"""構造的パターンマッチ (match case) の使い方
ORパターン(OR Patterns)の場合

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#OROR_Patterns
"""


def check_status(status):
    match status:
        case 200:
            print("OK")
        case 500 | 501 | 502:
            print("サーバーエラー")
        case _:
            print("対象外")


if __name__ == "__main__":
    response = 200
    check_status(response)

    print("---")
    response = 500
    check_status(response)

    print("---")
    response = 501
    check_status(response)

    print("---")
    response = 502
    check_status(response)

    print("---")
    response = 400
    check_status(response)

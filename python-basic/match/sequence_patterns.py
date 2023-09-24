"""構造的パターンマッチ (match case) の使い方
シーケンスパターン(Sequence Patterns)の場合

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#Sequence_Patterns
"""


def devisible_by_3_5(data):
    sequence = [data % 3, data % 5]
    match sequence:
        case (0, 0):
            print(f"{data}: 3と5で割り切れる")
        case (0, _):
            print(f"{data}: 3で割り切れる")
        case (_, 0):
            print(f"{data}: 5で割り切れる")
        case _:
            print(f"{data}")


if __name__ == "__main__":
    for d in range(1, 16):
        devisible_by_3_5(d)

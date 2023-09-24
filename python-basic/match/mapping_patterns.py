"""構造的パターンマッチ (match case) の使い方
マッピングパターン(Mapping Patterns)の場合

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#Mapping_Patterns
"""


def check(target):
    match target:
        case {"cond1": cond1, "cond2": cond2}:
            print(cond1, cond2)
        case {"cond3": cond3, **items}:
            print(cond3)
            print(items)
        case {**items}:
            print(items)
        case _:
            print("対象外")


if __name__ == "__main__":
    data = {"cond1": 10, "cond2": 20}
    check(data)

    print("---")
    data = {"cond3": 30, "cond4": 40, "cond5": 50}
    check(data)

    print("---")
    data = {"cond6": 60, "cond7": 70}
    check(data)

    print("---")
    data = [1, 2, 3, 4, 5]
    check(data)

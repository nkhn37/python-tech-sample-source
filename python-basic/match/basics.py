"""構造的パターンマッチ (match case) の使い方
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-structual-pattern-matching-basics/#_match_case
"""
value = 2

match value:
    case 1:
        print("失敗")
    # ↓ ここがマッチする
    case 2:
        print("成功")
    case _:
        print("値は不適切です。")

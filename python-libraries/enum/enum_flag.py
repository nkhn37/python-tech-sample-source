"""列挙型 enumの使い方の基本
フラグとして使いたい場合 (Flag)

[説明ページ]
https://tech.nkhn37.net/python-enum-basics/#_Flag
"""
from enum import Flag, auto


class Conditions(Flag):
    """Flagクラスを継承したフラグ"""

    COND_A = auto()
    COND_B = auto()
    COND_C = auto()


if __name__ == "__main__":
    print(Conditions.COND_A.name, Conditions.COND_A.value)
    print(Conditions.COND_B.name, Conditions.COND_B.value)
    print(Conditions.COND_C.name, Conditions.COND_C.value, "\n")

    # AとBが設定されている状況
    condition_setting = Conditions.COND_A | Conditions.COND_B
    print(condition_setting)

    # 存在の確認はinで可能
    print(Conditions.COND_A in condition_setting)
    print(Conditions.COND_B in condition_setting)
    print(Conditions.COND_C in condition_setting, "\n")

    # 条件は|や&を使って結合できる
    cond_a = Conditions.COND_A | Conditions.COND_B
    cond_b = Conditions.COND_B | Conditions.COND_C
    print(cond_a | cond_b)
    print(cond_a & cond_b)

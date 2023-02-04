"""if文基礎
論理演算子（and、or、not）で条件式を指定する

[説明ページ]
https://tech.nkhn37.net/python-if-basic/#andornot
"""


def is_positive_and_even(number):
    """正の数 かつ 偶数"""
    if number > 0 and number % 2 == 0:
        return True
    else:
        return False


def is_positive_or_even(number):
    """正の数 または 偶数"""
    if number > 0 or number % 2 == 0:
        return True
    else:
        return False


def is_not_positive(number):
    """正の数ではない"""
    if not number > 0:
        return True
    else:
        return False


print("===== 正の数 かつ(and) 偶数")
for i in range(-2, 3):
    print(f"{i:2}: {is_positive_and_even(i)}")

print("===== 正の数 または(or) 偶数")
for i in range(-2, 3):
    print(f"{i:2}: {is_positive_or_even(i)}")

print("===== 正の数ではない(not)")
for i in range(-2, 3):
    print(f"{i:2}: {is_not_positive(i)}")

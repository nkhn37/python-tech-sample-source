"""部分適用とクロージャの比較
クロージャでの実装

[説明ページ]
https://tech.nkhn37.net/python-partial-basic/#i-3
"""


def make_pow(factor):
    # my_powという内部関数は、外部関数のfactor引数を参照する
    def my_pow(x):
        return x ** factor
    return my_pow


pow2 = make_pow(2)

# 4 ** 2 = 16
print(pow2(4))
# 5 ** 2 = 25
print(pow2(5))

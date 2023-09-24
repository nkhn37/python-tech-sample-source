"""partial関数の使い方の基本
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-partial-basic/#i-2
"""
from functools import partial

# pow(base, exp)においてexp=2に固定する
pow2 = partial(pow, exp=2)
# 4 ** 2 = 16
print(pow2(4))
# 5 ** 2 = 25
print(pow2(5))

# pow(base, exp)においてexp=3に固定する
pow3 = partial(pow, exp=3)
# 4 ** 3 = 64
print(pow3(4))
# 5 ** 3 = 125
print(pow3(5))

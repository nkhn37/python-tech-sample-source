"""if文基礎
ラムダ(lambda)関数と三項演算子の組み合わせ

[説明ページ]
https://tech.nkhn37.net/python-if-basic/#lambda
"""
# 三項演算子とラムダ関数の組み合わせ
get_even_or_odd = lambda x: "even" if x % 2 == 0 else "odd"

num = 1
print(get_even_or_odd(num))

num = 2
print(get_even_or_odd(num))

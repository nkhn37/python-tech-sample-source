"""関数基礎
ラムダ(lambda)関数（ラムダ式、無名関数）の使い方

[説明ページ]
https://tech.nkhn37.net/python-lambda/#i
"""
# ラムダ関数
func = lambda val1, val2: val1 * 2 + val2 * 2

print(type(func))
print(func(1, 2))
print(func(3, 4))

"""reduce関数の使い方の基本
ラムダ関数(無名関数)を使用する

[説明ページ]
https://tech.nkhn37.net/python-reduce-basic/#i-2
"""
from functools import reduce

tmp_list = [1, 2, 3, 4, 5]

# reduce関数でラムダ関数を使って足し算を適用する
result = reduce(lambda x, y: x + y, tmp_list)
print(result)

# reduce関数でラムダ関数を使って掛け算を適用する
result = reduce(lambda x, y: x * y, tmp_list)
print(result)

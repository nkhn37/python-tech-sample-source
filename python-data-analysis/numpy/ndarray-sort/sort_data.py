"""NumPy基礎
配列(ndarray)をソートする方法(sortメソッド)
元のデータ自体をソートする

[説明ページ]
https://tech.nkhn37.net/numpy-array-sort-argsort/#i-3
"""
import numpy as np

x = np.array([5, 2, 4, 6, 1])
print(f'x = {x}')

# 元の配列自体をソートする場合
x.sort()
print(f'x = {x}')

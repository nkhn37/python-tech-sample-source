"""NumPy基礎
配列(ndarray)をソートする方法(sort関数)
降順にソートする

[説明ページ]
https://tech.nkhn37.net/numpy-array-sort-argsort/#i-2
"""
import numpy as np

x = np.array([5, 2, 4, 6, 1])
print(f'x = {x}')

# 降順にソートする場合
x_sorted = np.sort(x)[::-1]
print(f'x_sorted = {x_sorted}')

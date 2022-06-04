"""NumPy基礎
配列(ndarray)をソートする方法(sort関数)
昇順にソートする

[説明ページ]
https://tech.nkhn37.net/numpy-array-sort-argsort/#i
"""
import numpy as np

x = np.array([5, 2, 4, 6, 1])
print(f'x = {x}')

# 昇順にソートする場合
x_sorted = np.sort(x)
print(f'x_sorted = {x_sorted}')

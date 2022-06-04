"""NumPy基礎
配列(ndarray)をソートする方法(sort関数)
軸(axis)を指定してソートする

[説明ページ]
https://tech.nkhn37.net/numpy-array-sort-argsort/#axis
"""
import numpy as np

rand = np.random.RandomState(1)
X = rand.randint(0, 10, (5, 5))
print(f'X = \n{X}\n')

# 列ごとにソートする
X_sorted_col = np.sort(X, axis=0)
print(f'X_sorted (axis=0) = \n{X_sorted_col}\n')

# 行ごとにソートする
X_sorted_row = np.sort(X, axis=1)
print(f'X_sorted (axis=1) = \n{X_sorted_row}')

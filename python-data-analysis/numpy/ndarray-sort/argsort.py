"""NumPy基礎
配列(ndarray)のソート後のインデックスを取得する(argsort関数)

[説明ページ]
https://tech.nkhn37.net/numpy-array-sort-argsort/#_argsort
"""
import numpy as np

x = np.array([5, 2, 4, 6, 1])
print(f'x = {x}')

# ソートした後のインデックス順を取得する
sort_idx = np.argsort(x)
print(f'sort_idx = {sort_idx}')

# ソートされた配列を取得する
print(f'x_sorted = {x[sort_idx]}')

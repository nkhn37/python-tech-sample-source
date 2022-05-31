"""NumPy基礎
配列の要素を参照する方法
スライスで配列の一部を取り出す(行や列を取り出す場合)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-access/#i-3
"""
import numpy as np

data = np.arange(25).reshape((5, 5))
print(f'data: \n{data}')

# 行を取り出す
print('\n行を取り出す')
print(f'data[0, :] = {data[0, :]}')
print(f'data[0] = {data[0]}')

# 列を取り出す
print('\n列を取り出す')
print(f'data[:, 0] = {data[:, 0]}')

"""NumPy基礎
配列の要素を参照する方法
スライスで配列の一部を取り出す(2次元配列の場合)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-access/#2
"""
import numpy as np

data = np.arange(25).reshape((5, 5))
print(f'data: \n{data}')

# 部分配列を取り出す
print('\n部分配列を取り出す')
print(f'data[:2, :2] = \n{data[:2, :2]}')
print(f'data[3:, 3:] = \n{data[3:, 3:]}')

# stepを指定して部分配列を取り出す
print('\nstepを指定して部分配列を取り出す')
print(f'data[::2, ::2] = \n{data[::2, ::2]}')

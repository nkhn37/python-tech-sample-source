"""NumPy基礎
配列(ndarray)の結合方法
行方向の結合(vstackを使用する場合)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-concatenate-vstack-hstack/#vstack
"""
import numpy as np

x = np.arange(9).reshape((3, 3))
y = np.arange(9).reshape((3, 3))

# 2次元配列を行方向に結合する
result = np.vstack((x, y))
print(result)

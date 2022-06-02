"""NumPy基礎
配列(ndarray)の結合方法
列方向の結合(hstackを使用する場合)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-concatenate-vstack-hstack/#hstack
"""
import numpy as np

x = np.arange(9).reshape((3, 3))
y = np.arange(9).reshape((3, 3))

# 2次元配列を列方向に結合する
result = np.hstack((x, y))
print(result)

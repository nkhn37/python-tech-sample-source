"""NumPy基礎
配列(ndarray)の形状を変更する方法
1次元配列から多次元配列を作成する
(2次元配列を作る場合）

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-reshape-newaxis/#1
"""
import numpy as np

x = np.arange(1, 10).reshape((3, 3))
print(x)
print(f'size: {x.size}')
print(f'shape: {x.shape}')

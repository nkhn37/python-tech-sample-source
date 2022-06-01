"""NumPy基礎
配列(ndarray)の形状を変更する方法
行ベクトルを作成する
(reshapeを使用する方法)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-reshape-newaxis/#reshape
"""
import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(f'x = {x}')
# 行ベクトルを作成する
x_row = x.reshape((1, x.size))
print(f'x_row = {x_row}')

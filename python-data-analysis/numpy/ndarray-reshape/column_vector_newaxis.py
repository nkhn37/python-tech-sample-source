"""NumPy基礎
配列(ndarray)の形状を変更する方法
列ベクトルを作成する
(np.newaxisを使用する方法)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-reshape-newaxis/#npnewaxis-2
"""
import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(f'x = {x}')
# 列ベクトルを作成する
x_col = x[:, np.newaxis]
print(f'x_col = \n{x_col}')

"""NumPy基礎
配列(ndarray)の形状を変更する方法
行ベクトルを作成する
(np.newaxisを使用する場合)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-reshape-newaxis/#npnewaxis
"""
import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(f'x = {x}')
# 行ベクトルを作成する
x_row = x[np.newaxis, :]
print(f'x_row = {x_row}')

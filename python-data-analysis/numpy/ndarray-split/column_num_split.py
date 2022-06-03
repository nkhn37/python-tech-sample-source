"""NumPy基礎
配列(ndarray)の分割方法
列方向(水平方向)の分割：指定個数で分割する方法
splitを使用した場合

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-split-vsplit-hsplit/#split-3
"""
import numpy as np

x = np.arange(36).reshape((6, 6))
print(f'x: \n{x}\n')

# 配列を列方向（水平方向）に指定個数で分割する (split)
x_split = np.split(x, 3, axis=1)

for i, x in enumerate(x_split):
    print(f'x_split[{i}]: \n{x}')

"""NumPy基礎
配列(ndarray)の分割方法
行方向(垂直方向)の分割：指定個数で分割する方法
splitを使用した場合

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-split-vsplit-hsplit/#split
"""
import numpy as np

x = np.arange(36).reshape((6, 6))
print(f'x: \n{x}\n')

# 配列を行方向（垂直方向）に指定個数で分割する (split)
x_split = np.split(x, 3)

for i, x in enumerate(x_split):
    print(f'x_split[{i}]: \n{x}')

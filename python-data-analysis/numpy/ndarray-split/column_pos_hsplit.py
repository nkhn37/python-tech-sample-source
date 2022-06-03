"""NumPy基礎
配列(ndarray)の分割方法
列方向(水平方向)の分割：指定位置で分割する方法
hsplitを使用した場合

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-split-vsplit-hsplit/#hsplit-2
"""
import numpy as np

x = np.arange(25).reshape((5, 5))
print(f'x: \n{x}\n')

# 配列を列方向（水平方向）に指定位置で分割する (hsplit)
x_split = np.hsplit(x, [2, 4])

for i, x in enumerate(x_split):
    print(f'x_split[{i}]: \n{x}')

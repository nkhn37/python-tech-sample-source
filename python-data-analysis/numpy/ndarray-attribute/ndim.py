"""NumPy基礎
配列の次元数を確認する(ndim)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-attributes-check/#_ndim
"""
import numpy as np

data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(data)
print(f'ndim: {data.ndim}')

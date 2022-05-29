"""NumPy基礎
配列の型を確認する(dtype)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-attributes-check/#_dtype
"""
import numpy as np

data = np.array([1, 2, 3, 4, 5])
print(data)
print(f'dtype: {data.dtype}')

"""NumPy基礎
配列の要素数を確認する(size)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-attributes-check/#_size
"""
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(data)
print(f'size: {data.size}')

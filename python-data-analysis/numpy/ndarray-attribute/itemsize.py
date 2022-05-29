"""NumPy基礎
配列の1要素のバイトサイズを確認する(itemsize)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-attributes-check/#_itemsize
"""
import numpy as np

data = np.random.randint(0, 10, 10)
print(data)
print(f'itemsize: {data.itemsize} bytes')

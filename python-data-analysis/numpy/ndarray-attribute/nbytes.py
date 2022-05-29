"""NumPy基礎
配列全体のバイトサイズを確認する(nbytes)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-attributes-check/#_nbytes
"""
import numpy as np

data = np.random.randint(0, 10, 10)
print(data)
print(f'nbytes: {data.nbytes} bytes')

"""NumPy基礎
配列の要素を参照する方法

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-access/#i
"""
import numpy as np

data = np.arange(10)
print(f'data: {data}')

# 単一の要素にアクセスする（インデックスは0が開始なので注意）
print(f'data[0] = {data[0]}')
print(f'data[5] = {data[5]}')
print(f'data[9] = {data[9]}')

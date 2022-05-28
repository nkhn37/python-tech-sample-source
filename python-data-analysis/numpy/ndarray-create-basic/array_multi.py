"""numpy基礎
配列の作成方法(array関数)
多次元配列を作成する場合

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#i-3
"""
import numpy as np

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_array = np.array(data)

print(data_array)
print(type(data_array))
print(data_array.shape)
print(data_array.dtype)

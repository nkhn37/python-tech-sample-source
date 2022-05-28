"""numpy基礎
指定した値で埋めた配列を作成する場合(full関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#full
"""
import numpy as np

data_array = np.full((3, 3), 1.5)

print(data_array)
print(type(data_array))
print(data_array.dtype)

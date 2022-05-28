"""numpy基礎
指定間隔の連続値で配列を作成する場合(arange関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#arange
"""
import numpy as np

data_array = np.arange(0, 10, 2)

print(data_array)
print(type(data_array))
print(data_array.dtype)

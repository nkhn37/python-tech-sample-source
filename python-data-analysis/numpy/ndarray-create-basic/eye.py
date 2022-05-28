"""numpy基礎
単位行列を作成する方法(eye関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#eye
"""
import numpy as np

data_array = np.eye(3)

print(data_array)
print(type(data_array))
print(data_array.dtype)

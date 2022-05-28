"""numpy基礎
配列の作成方法(array関数)
型が異なる場合は（可能であれば）アップキャストする

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#i
"""
import numpy as np

data = [1.23, 2, 3, 4, 5]
data_array = np.array(data)

print(data_array)
print(type(data_array))
print(data_array.dtype)

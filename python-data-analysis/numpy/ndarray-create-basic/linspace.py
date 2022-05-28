"""numpy基礎
等間隔のデータを作成する方法(linspace関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#linspace
"""
import numpy as np

data_array = np.linspace(0, 1, 5)

print(data_array)
print(type(data_array))
print(data_array.dtype)

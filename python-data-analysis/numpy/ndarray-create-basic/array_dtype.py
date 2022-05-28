"""numpy基礎
配列の作成方法(array関数)
型を明示的に指定したい場合

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#i-2
"""
import numpy as np

data = [1, 2, 3, 4, 5]
data_array = np.array(data, dtype=np.double)

print(data_array)
print(type(data_array))
print(data_array.dtype)

"""numpy基礎
値が初期化されてはいない配列を作成する場合(empty関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#empty
"""
import numpy as np

data_array = np.empty(10)

print(data_array)
print(type(data_array))
print(data_array.dtype)

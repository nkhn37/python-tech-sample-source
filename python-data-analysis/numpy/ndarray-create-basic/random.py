"""numpy基礎
ランダムな数値で配列を作成する方法
0~1のランダムな配列を作成する場合(random関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#01_random
"""
import numpy as np

data_array = np.random.random((3, 3))

print(data_array)
print(type(data_array))
print(data_array.dtype)

"""numpy基礎
ランダムな数値で配列を作成する方法
int型のランダムな数値の配列を作成する場合(randint関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#intrandint
"""
import numpy as np

data_array = np.random.randint(0, 20, (3, 3))

print(data_array)
print(type(data_array))
print(data_array.dtype)

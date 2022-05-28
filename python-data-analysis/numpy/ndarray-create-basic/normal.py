"""numpy基礎
ランダムな数値で配列を作成する方法
任意の正規分布に従う数値の配列を作成する場合(normal関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#normal
"""
import numpy as np

data_array = np.random.normal(1, 5, (3, 3))

print(data_array)
print(type(data_array))
print(data_array.dtype)

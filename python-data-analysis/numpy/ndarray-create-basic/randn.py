"""numpy基礎
ランダムな数値で配列を作成する方法
標準正規分布に従う数値の配列を作成する場合(randn関数)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-create-basic/#randn
"""
import numpy as np

data_array = np.random.randn(10)

print(data_array)
print(type(data_array))
print(data_array.dtype)

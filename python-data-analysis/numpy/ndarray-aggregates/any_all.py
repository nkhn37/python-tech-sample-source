"""NumPy基礎
集約関数：要素のTrue判定 （np.any、np.all）

[説明ページ]
https://tech.nkhn37.net/numpy-aggregates-basic/#True_npanynpall
"""
import numpy as np

data1 = np.array([True, True, False])
data2 = np.array([True, True, True])
data3 = np.array([0, 1, 2])
data4 = np.array([1, 2, 3])

print('--- data1')
print(np.any(data1))
print(np.all(data1))
print('--- data2')
print(np.any(data2))
print(np.all(data2))
print('--- data3')
print(np.any(data3))
print(np.all(data3))
print('--- data4')
print(np.any(data4))
print(np.all(data4))

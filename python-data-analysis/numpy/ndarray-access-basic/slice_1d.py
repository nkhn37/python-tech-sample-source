"""NumPy基礎
配列の要素を参照する方法
スライスで配列の一部を取り出す(1次元配列の場合)

[説明ページ]
https://tech.nkhn37.net/numpy-ndarray-access/#1
"""
import numpy as np

data = np.arange(10)
print(f'data: {data}')

# スライスで要素の一部を取り出す
print('\nスライスで要素の一部を取り出す')
print(f'data[2:8] = {data[2:8]}')
print(f'data[5:] = {data[5:]}')
print(f'data[:5] = {data[:5]}')

# stepを指定して値を取り出す
print('\nstepを指定して一定間隔で値を取り出す')
print(f'data[0:5:2] = {data[0:5:2]}')
print(f'data[::2] = {data[::2]}')

# 逆順で配列を取り出す
print('\n逆順で配列を取り出す')
print(f'data[::-1] = {data[::-1]}')

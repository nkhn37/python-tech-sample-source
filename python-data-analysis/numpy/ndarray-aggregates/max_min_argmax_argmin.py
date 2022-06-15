"""NumPy基礎
集約関数：最大（np.max）、最小（np.min）、
　　　　　最大要素位置（np.argmax）、最小要素位置（np.argmin）

[説明ページ]
https://tech.nkhn37.net/numpy-aggregates-basic/#npmaxnpminnpargmaxnpargmin
"""
import numpy as np

# データの用意
data = np.arange(1, 6)

print(f'最大：{np.max(data)}')
print(f'最小：{np.min(data)}')
print(f'最大要素位置：{np.argmax(data)}')
print(f'最小要素位置：{np.argmin(data)}')

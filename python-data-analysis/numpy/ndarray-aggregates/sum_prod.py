"""NumPy基礎
集約関数：総和（np.sum）と総乗（np.prod）

[説明ページ]
https://tech.nkhn37.net/numpy-aggregates-basic/#npsumnpprod
"""
import numpy as np

# データの用意
data = np.arange(1, 6)

print(f'総和：{np.sum(data)}')
print(f'総乗：{np.prod(data)}')

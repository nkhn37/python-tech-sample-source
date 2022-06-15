"""NumPy基礎
集約関数：平均（np.mean）、中央値（np.median）、標準偏差（np.std）、分散（np.var）

[説明ページ]
https://tech.nkhn37.net/numpy-aggregates-basic/#npmeannpmediannpstdnpvar
"""
import numpy as np

# 平均5, 標準偏差2の正規分布に従うデータを用意
data = 5 + np.random.randn(1000) * 2

print(f'平均値：{np.mean(data)}')
print(f'中央値：{np.median(data)}')
print(f'標準偏差：{np.std(data)}')
print(f'分散：{np.var(data)}')

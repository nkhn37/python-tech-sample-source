"""matplotlib
hexbinによる2次元の六角形ヒストグラムの描画

[説明ページ]
https://tech.nkhn37.net/matplotlib-hist-hist2d-hexbin/#hexbin2
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

# 2次元正規分布の平均と共分散を定義
# 平均
m = [0, 0]
# 共分散
cov = [[1, 1], [1, 2]]
# データの生成
x, y = np.random.multivariate_normal(m, cov, 1000).T

# 六角形での2次元ヒストグラムの表示
plt.hexbin(x, y, gridsize=30, cmap='Purples')
plt.colorbar()

plt.show()

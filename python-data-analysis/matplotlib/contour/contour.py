"""matplotlib
contourによる等高線プロット

[説明ページ]
https://tech.nkhn37.net/matplotlib-contour-contourf/#contour
"""
import numpy as np
import matplotlib.pyplot as plt

# データグリッドの生成
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

# データ点の生成
Z = np.sin(X) + np.cos(Y)

# 等高線プロットの表示
plt.contour(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()

plt.show()

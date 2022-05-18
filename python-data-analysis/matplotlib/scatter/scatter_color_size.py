"""matplotlib
scatterで散布図を表示する(色やサイズを指定して使用する方法)

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-scatter/#i-5
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

rs = np.random.RandomState(1)
x = rs.randn(100)
y = rs.randn(100)
# 色をランダムに指定する
colors = rs.rand(100)
# サイズをランダムに指定する
sizes = 1000 * rs.rand(100)

# 散布図を表示しカラーバーを表示する
# c:色、s:サイズ、alpha:透過度、cmap:カラーマップ指定
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='plasma')
# カラーバーを表示する
plt.colorbar()

plt.show()

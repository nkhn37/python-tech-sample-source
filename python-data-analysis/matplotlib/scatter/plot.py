"""matplotlib
plotによる散布図の描画(基本的な使い方)

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-scatter/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

rs = np.random.RandomState(1)
x = rs.randn(100)
y = rs.randn(100)

# plotで散布図を表示する
plt.plot(x, y, 'o')

plt.show()

"""matplotlib
scatterで散布図を表示する(基本的な使い方)

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-scatter/#i-4
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

rs = np.random.RandomState(1)
x = rs.randn(100)
y = rs.randn(100)

# scatterで散布図を表示する
plt.scatter(x, y, marker='o')

plt.show()

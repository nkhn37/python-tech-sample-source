"""matplotlib
plotでの軸の範囲の指定方法(axis)

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-lim-axis/#i-3
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# グラフ表示
plt.plot(x, np.sin(x))
# axisによる軸範囲設定 [xmin, xmax, ymin, ymax]
plt.axis([-2, 12, -1.5, 1.5])

plt.show()

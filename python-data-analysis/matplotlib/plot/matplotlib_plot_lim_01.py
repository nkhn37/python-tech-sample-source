"""matplotlib
plotでの軸の範囲の指定方法(xlim, ylim)

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-lim-axis/#i
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# グラフ表示
plt.plot(x, np.sin(x))
# x軸の範囲を変更する
plt.xlim(-2, 12)
# y軸の範囲を変更する
plt.ylim(-1.5, 1.5)

plt.show()

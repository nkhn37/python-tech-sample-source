"""matplotlib
plotでの軸の範囲の指定方法(axis)
画面にフィットさせる場合: tightオプション

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-lim-axis/#_tight
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# グラフ表示
plt.plot(x, np.sin(x))
# tightでグラフに軸をフィットさせる
plt.axis('tight')

plt.show()

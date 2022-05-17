"""matplotlib
plotでの軸の範囲の指定方法(axis)
x軸、y軸の値の比率を揃える場合: equalオプション

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-lim-axis/#xy_equal
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# グラフ表示
plt.plot(x, np.sin(x))
# equalで軸の比率をそろえる
plt.axis('equal')

plt.show()

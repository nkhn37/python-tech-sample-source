"""matplotlib
plotでの軸の範囲の指定方法(xlim, ylim)
軸を逆転させる方法

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-lim-axis/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# グラフ表示
plt.plot(x, np.sin(x))
# x軸の範囲を変更する（反転）
plt.xlim(12, -2)
# y軸の範囲を変更する（反転）
plt.ylim(1.5, -1.5)

plt.show()

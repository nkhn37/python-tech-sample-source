"""matplotlib
plotでタイトル・軸名・凡例を表示する方法
setでまとめて設定する方法

[説明ページ]
https://tech.nkhn37.net/matplotlib-title-label-legend-set/#_set
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# グラフ表示
ax = plt.axes()
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')

# setメソッドでタイトル等を各種設定
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='y',
       title='Sine & Cosine Curve')

# 凡例の設定
plt.legend()

plt.show()

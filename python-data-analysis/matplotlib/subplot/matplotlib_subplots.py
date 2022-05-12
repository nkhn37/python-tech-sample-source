"""matplotlib
複数グラフを一つのウィンドウに表示する
オブジェクト指向な方法(subplots)

[説明ページ]
https://tech.nkhn37.net/matplotlib-subplots/#_subplots
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots(2, 1)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

fig.show()

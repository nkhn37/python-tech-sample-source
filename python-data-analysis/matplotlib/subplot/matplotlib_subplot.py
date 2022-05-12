"""matplotlib
複数グラフを一つのウィンドウに表示する(subplot)

[説明ページ]
https://tech.nkhn37.net/matplotlib-subplots/#_subplot
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# 引数は、(行数, 列数, 指定する位置)
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

plt.show()

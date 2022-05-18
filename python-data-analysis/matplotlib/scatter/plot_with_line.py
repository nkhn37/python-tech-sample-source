"""matplotlib
plotで点と線を一緒に表示する

[説明ページ]
https://tech.nkhn37.net/matplotlib-plot-scatter/#i-3
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 50)
y = np.sin(x)

# 線と点を一緒に表示する
plt.plot(x, y, '-o')

plt.show()

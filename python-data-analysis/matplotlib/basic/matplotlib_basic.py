"""matplotlib
基本的なプロット方法

[説明ページ]
https://tech.nkhn37.net/matplotlib-basic-usage/#matplotlib-5
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()

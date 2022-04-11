"""matplotlib
画像を保存する方法

[説明ページ]
https://tech.nkhn37.net/matplotlib-basic-usage/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

fig.savefig('temp.png')

plt.show()

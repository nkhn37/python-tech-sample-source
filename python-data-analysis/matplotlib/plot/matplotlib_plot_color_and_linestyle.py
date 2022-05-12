"""matplotlib
plotで線の色と形状を一括で変更する方法

[説明ページ]
https://tech.nkhn37.net/matplotlib-color-linestyle/#i-3
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# ===== 腺の色と形状を一括で指定する
# 通常の線 + 青
plt.plot(x, x, '-b')
# 点線 + マゼンタ
plt.plot(x, x+1, '--m')
# 点線ドット + 黒
plt.plot(x, x+2, '-.k')
# ドット + 緑
plt.plot(x, x+3, ':g')

plt.show()

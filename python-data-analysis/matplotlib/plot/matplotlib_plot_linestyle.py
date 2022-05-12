"""matplotlib
plotで線の形状を変更する方法

[説明ページ]
https://tech.nkhn37.net/matplotlib-color-linestyle/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# ===== 線のスタイルを変更する
# 通常の線で表示する
plt.plot(x, x, linestyle='solid')
# 点線で表示する
plt.plot(x, x+1, linestyle='dashed')
# 点線+ドットの線で表示する
plt.plot(x, x+2, linestyle='dashdot')
# ドットの線で表示する
plt.plot(x, x+3, linestyle='dotted')

# ===== 省略形で指定する
# 通常の線で表示する(=solid)
plt.plot(x, x+4, linestyle='-')
# 点線で表示する(=dashed)
plt.plot(x, x+5, linestyle='--')
# 点線+ドットの線で表示する(=dashdot)
plt.plot(x, x+6, linestyle='-.')
# ドットの線で表示する(=dotted)
plt.plot(x, x+7, linestyle=':')

plt.show()

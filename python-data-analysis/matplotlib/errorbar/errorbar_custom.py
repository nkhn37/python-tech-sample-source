"""matplotlib
errorbarによるエラーバーの表示

[説明ページ]
https://tech.nkhn37.net/matplotlib-errorbar-basic/#errorbar
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

# x軸を用意
x = np.linspace(0, 10, 100)
# 誤差の標準偏差を設定
dy = 1.5
# sin(x)に標準偏差1.5の正規分布に従う誤差を追加
y = np.sin(x) + dy * np.random.randn(100)

# (x, y)のプロットと誤差範囲(標準偏差)を表示、色などをカスタマイズ
plt.errorbar(x, y, yerr=dy, fmt='o', color='blue', ecolor='gray',
             elinewidth=2)

plt.show()

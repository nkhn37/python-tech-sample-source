"""matplotlib
histによるヒストグラムの描画（表示のカスタマイズ）

[説明ページ]
https://tech.nkhn37.net/matplotlib-hist-hist2d-hexbin/#i-3
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

# 正規分布に従うデータの生成
d = np.random.randn(1000)

# ヒストグラムの表示（各種設定）
plt.hist(d, bins=30, color='red', edgecolor='k', alpha=0.5)

plt.show()

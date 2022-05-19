"""matplotlib
histによるヒストグラムの描画（基本的な方法）

[説明ページ]
https://tech.nkhn37.net/matplotlib-hist-hist2d-hexbin/#i-2
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

# 正規分布に従うデータの生成
d = np.random.randn(1000)

# ヒストグラムの表示
plt.hist(d)

plt.show()

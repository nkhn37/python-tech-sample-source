"""matplotlib
histによるヒストグラムの描画（複数ヒストグラムを同時に描画）

[説明ページ]
https://tech.nkhn37.net/matplotlib-hist-hist2d-hexbin/#i-4
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

# 正規分布に従うデータを複数生成
# 平均0, 標準偏差1
d1 = np.random.normal(0, 1, 1000)
# 平均-2, 標準偏差0.5
d2 = np.random.normal(-2, 0.5, 1000)
# 平均5, 標準偏差3
d3 = np.random.normal(5, 3, 1000)

# 設定値の作成
kwargs = dict(bins=30, alpha=0.5, histtype='stepfilled', edgecolor='k')

# ヒストグラムの表示
plt.hist(d1, **kwargs)
plt.hist(d2, **kwargs)
plt.hist(d3, **kwargs)

plt.show()

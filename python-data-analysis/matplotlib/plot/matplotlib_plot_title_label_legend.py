"""matplotlib
plotでタイトル・軸名・凡例を表示する方法

[説明ページ]
https://tech.nkhn37.net/matplotlib-title-label-legend-set/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# グラフ表示
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')

# タイトルの表示
plt.title('Sine & Cosine Curve')

# x軸ラベルの設定
plt.xlabel('x')
plt.xlim(0, 10)

# y軸ラベルの設定
plt.ylabel('sin(x)')
plt.ylim(-2, 2)

# 凡例の設定
plt.legend()

plt.show()

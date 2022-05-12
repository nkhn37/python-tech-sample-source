"""matplotlib
plotで線の色を変更する方法

[説明ページ]
https://tech.nkhn37.net/matplotlib-color-linestyle/#i
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 100)

# 色を文字列で指定する。
plt.plot(x, x, color='red')
# 色を短縮文字列で指定する
plt.plot(x, x+1, color='b')
# グレースケールの範囲で指定する (0~1)
plt.plot(x, x+2, color='0.5')
# 16進数のカラーコードで指定する
plt.plot(x, x+3, color='#ff6c00')
# HTMLのカラーネームで指定する
plt.plot(x, x+4, color='darkgreen')

plt.show()

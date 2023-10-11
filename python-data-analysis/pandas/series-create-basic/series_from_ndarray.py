"""pandas基礎
Seriesの作成方法
(NumPy配列(ndarray)から作成する)

[説明ページ]
https://tech.nkhn37.net/pandas-series-create-basic/#NumPy
"""
import numpy as np
import pandas as pd

# NumPy配列(ndarray)からSeriesを作成する
# int
arr = np.array([1, 5, 2, 4, 5])
data = pd.Series(arr)
print(data, "\n")

# float
arr = np.array([1.0, 1.5, 2.0, 4.0, 5.0])
data = pd.Series(arr)
print(data)

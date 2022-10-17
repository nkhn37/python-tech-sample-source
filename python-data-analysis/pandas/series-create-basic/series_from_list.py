"""pandas基礎
Seriesの作成方法
(リストから作成する)

[説明ページ]
https://tech.nkhn37.net/pandas-series-create-basic/#NumPy
"""
import pandas as pd

# リストからSeriesを作成する
# int
data = pd.Series([1, 5, 2, 4, 5])
print(data, '\n')

# float
data = pd.Series([1.0, 1.5, 2.0, 4.0, 5.0])
print(data)

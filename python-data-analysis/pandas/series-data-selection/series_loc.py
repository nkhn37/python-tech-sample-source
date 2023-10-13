"""pandas基礎
Seriesのデータ選択方法
(locメソッドによるデータ選択(明示的なインデックス))

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#loc
"""
import pandas as pd

data = pd.Series(["a", "b", "c", "d", "e"], index=[1, 2, 3, 4, 5])
print(data, "\n")

# locメソッドでデータ選択（明示的なインデックス）
print(data.loc[1], "\n")
print(data.loc[1:3])

"""pandas基礎
Seriesのデータ選択方法
(ilocメソッドによるデータ選択(暗黙的なインデックス))

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#iloc
"""
import pandas as pd

data = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[1, 2, 3, 4, 5])
print(data, '\n')

# ilocメソッドでデータ選択（暗黙的なインデックス）
print(data.iloc[1], '\n')
print(data.iloc[1:3])

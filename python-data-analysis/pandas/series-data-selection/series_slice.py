"""pandas基礎
Seriesのデータ選択方法
(スライスでのデータ選択)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#i-3
"""
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(data, '\n')

# スライスでのアクセス
print(data['b':'d'], '\n')
print(data[0:2])

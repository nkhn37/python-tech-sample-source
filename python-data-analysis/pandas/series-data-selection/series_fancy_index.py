"""pandas基礎
Seriesのデータ選択方法
(ファンシーインデックスによるアクセス)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#i-5
"""
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(data, '\n')

# ファンシーインデックス
print(data[['c', 'd', 'a']])

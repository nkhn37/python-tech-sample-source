"""pandas基礎
Seriesのデータ選択方法
(インデックス情報を取得する ~keys~)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#keys
"""
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(data, '\n')

# インデックスを取り出す
print(data.keys())

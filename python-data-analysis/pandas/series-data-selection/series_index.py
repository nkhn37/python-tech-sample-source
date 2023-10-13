"""pandas基礎
Seriesのデータ選択方法
(インデックスで要素を指定して選択)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#i
"""
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(data, "\n")

# 要素をインデックスで指定して参照
print(data["b"])

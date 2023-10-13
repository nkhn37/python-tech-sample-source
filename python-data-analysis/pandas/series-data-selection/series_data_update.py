"""pandas基礎
Seriesのデータ選択方法
(要素の値を上書きする)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#i-2
"""
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(data, "\n")

# 値を上書きする
data["e"] = 10
print(data)

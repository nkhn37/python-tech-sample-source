"""pandas基礎
Seriesのデータ選択方法
(インデックス(キー)の有無を確認する　~in, not in~)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#_in_not_in
"""
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(data, "\n")

# キーの有無を確認する
print("c" in data)
print("z" in data)

"""pandas基礎
Seriesのデータ選択方法
(条件によるマスキング)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#i-4
"""
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(data, "\n")

# マスキング
print(f"data > 1:\n{data > 1}\n")
print(f"data < 5:\n{data < 5}\n")
print(f"(data > 1) & (data < 5):\n{(data > 1) & (data < 5)}\n")
print(f"data[(data > 1) & (data < 5)]:\n{data[(data > 1) & (data < 5)]}")

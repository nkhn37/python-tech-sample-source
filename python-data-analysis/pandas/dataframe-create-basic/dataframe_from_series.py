"""pandas基礎
DataFrameの作成方法
(Seriesから作成する)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-create-basic/#Series
"""
import pandas as pd

# Seriesを作成する
data = pd.Series([100, 200, 300, 400, 500], index=["A", "B", "C", "D", "E"])
print(data, "\n")

# SeriesからDataFrameを作成する
df = pd.DataFrame(data, columns=["attr1"])
print(df)

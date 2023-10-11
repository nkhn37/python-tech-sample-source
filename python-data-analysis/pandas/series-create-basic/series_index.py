"""pandas基礎
Seriesの作成方法
(任意のインデックスを指定して作成する)

[説明ページ]
https://tech.nkhn37.net/pandas-series-create-basic/#i
"""
import pandas as pd

# リストからSeriesを作成する
# 任意の数値を指定する
data = pd.Series([1, 5, 2, 4, 5], index=[100, 300, 200, 500, 400])
print(data, "\n")

# 文字列を指定することも可能
data = pd.Series([1, 5, 2, 4, 5], index=["a", "c", "d", "e", "z"])
print(data)

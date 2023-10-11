"""pandas基礎
Seriesの作成方法
(辞書から作成する)

[説明ページ]
https://tech.nkhn37.net/pandas-series-create-basic/#i-2
"""
import pandas as pd

# 辞書からSeriesを作成する
dic = {"a": 10, "z": 5, "c": 20, "f": 100}
data = pd.Series(dic)
print(data, "\n")

# 辞書の中から一部だけを抽出してSeriesを作成する
data = pd.Series(dic, index=["a", "f", "z"])
print(data)

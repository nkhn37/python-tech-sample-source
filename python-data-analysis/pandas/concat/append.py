"""pandas基礎
SeriesやDataFrameを連結する方法
(appendメソッドによるデータ連結)
※ pandas 1.4.0から非推奨
   将来的には削除される予定のためconcatを使用することを推奨

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-concat-append/#append
"""
import pandas as pd

# ===== Seriesの連結
# データの準備
ser1 = pd.Series(['A', 'B', 'C', 'D', 'E'], index=[1, 2, 3, 4, 5])
ser2 = pd.Series(['V', 'W', 'X', 'Y', 'Z'], index=[6, 7, 8, 9, 10])

# 連結
print(ser1.append(ser2), '\n')

# ===== DataFrameの連結
# データの準備
df1 = pd.DataFrame([['A', 'B'], ['C', 'D'], ['E', 'F']],
                   index=[1, 2, 3], columns=['attr1', 'attr2'])
df2 = pd.DataFrame([['U', 'V'], ['W', 'X'], ['Y', 'Z']],
                   index=[4, 5, 6], columns=['attr1', 'attr2'])

# 連結
print(df1.append(df2))

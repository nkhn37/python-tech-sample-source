"""pandas基礎
SeriesやDataFrameを連結する方法
(concat関数の基本的な使い方)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-concat-append/#concat-2
"""
import pandas as pd

# ===== Seriesの連結
# データの準備
ser1 = pd.Series(['A', 'B', 'C', 'D', 'E'], index=[1, 2, 3, 4, 5])
ser2 = pd.Series(['V', 'W', 'X', 'Y', 'Z'], index=[6, 7, 8, 9, 10])

# 連結
ser_concat = pd.concat([ser1, ser2])
print(ser_concat, '\n')

# ===== DataFrameの連結
# データの準備
df1 = pd.DataFrame([['A', 'B'], ['C', 'D'], ['E', 'F']],
                   index=[1, 2, 3], columns=['attr1', 'attr2'])
df2 = pd.DataFrame([['U', 'V'], ['W', 'X'], ['Y', 'Z']],
                   index=[4, 5, 6], columns=['attr1', 'attr2'])

# 連結
df_concat = pd.concat([df1, df2])
print(df_concat)

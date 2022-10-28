"""pandas基礎
SeriesやDataFrameを連結する方法
(concat関数: 連結するデータにキーを指定して階層型インデックスにする keys)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-concat-append/#_keys
"""
import pandas as pd

# ===== DataFrameの連結
# データの準備
df1 = pd.DataFrame([['A', 'B'], ['C', 'D'], ['E', 'F']],
                   index=[1, 2, 3], columns=['attr1', 'attr2'])
df2 = pd.DataFrame([['U', 'V'], ['W', 'X'], ['Y', 'Z']],
                   index=[2, 3, 4], columns=['attr1', 'attr2'])

# 連結 (階層型のインデックスにする)
df_concat = pd.concat([df1, df2], keys=['D1', 'D2'])
print(df_concat)

"""pandas基礎
SeriesやDataFrameを連結する方法
(concat関数: インデックスを無視する ignore_index)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-concat-append/#_ignore_index
"""
import pandas as pd

# ===== DataFrameの連結
df1 = pd.DataFrame([['A', 'B'], ['C', 'D'], ['E', 'F']],
                   index=[1, 2, 3], columns=['attr1', 'attr2'])
df2 = pd.DataFrame([['U', 'V'], ['W', 'X'], ['Y', 'Z']],
                   index=[2, 3, 4], columns=['attr1', 'attr2'])

# 連結 (インデックスを無視する)
df_concat = pd.concat([df1, df2], ignore_index=True)
print(df_concat)

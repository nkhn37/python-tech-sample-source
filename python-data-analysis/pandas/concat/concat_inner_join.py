"""pandas基礎
SeriesやDataFrameを連結する方法
(concat関数: 積集合での連結 join='inner')

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-concat-append/#_join8217inner8217
"""
import pandas as pd

# ===== DataFrameの連結
df1 = pd.DataFrame([['A', 'B'], ['C', 'D'], ['E', 'F']],
                   index=[1, 2, 3], columns=['attr1', 'attr2'])
df2 = pd.DataFrame([['U', 'V'], ['W', 'X'], ['Y', 'Z']],
                   index=[4, 5, 6], columns=['attr2', 'attr3'])

# 連結 (デフォルトはjoin='outer')
df_concat = pd.concat([df1, df2])
print(df_concat, '\n')

# 連結 (join='inner')
df_concat = pd.concat([df1, df2], join='inner')
print(df_concat)

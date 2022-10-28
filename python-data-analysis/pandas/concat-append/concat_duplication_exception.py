"""pandas基礎
SeriesやDataFrameを連結する方法
(concat関数: 重複がある場合に例外を出す verify_integrity)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-concat-append/#_verify_integrity
"""
import pandas as pd

# ===== DataFrameの連結
df1 = pd.DataFrame([['A', 'B'], ['C', 'D'], ['E', 'F']],
                   index=[1, 2, 3], columns=['attr1', 'attr2'])
df2 = pd.DataFrame([['U', 'V'], ['W', 'X'], ['Y', 'Z']],
                   index=[2, 3, 4], columns=['attr1', 'attr2'])

# 連結 (インデックス重複時は例外:ValueError)
try:
    df_concat = pd.concat([df1, df2], verify_integrity=True)
    print(df_concat)
except ValueError as ex:
    print(ex)


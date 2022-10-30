"""pandas基礎
欠損値(NaN, None)の扱いと処理方法
(pandasでの欠損値の扱い)

[説明ページ]
https://tech.nkhn37.net/pandas-dropna-fillna/#pandas
"""
import numpy as np
import pandas as pd

# Seriesでの欠損値の例
ser = pd.Series([1, np.nan, 3, None, 5])
print(ser, '\n')

# DataFrameでの欠損値の例
df = pd.DataFrame([[1, np.nan, 3], [4, 5, None]],
                  index=[1, 2], columns=['attr1', 'attr2', 'attr3'])
print(df, '\n')
print(df.dtypes)

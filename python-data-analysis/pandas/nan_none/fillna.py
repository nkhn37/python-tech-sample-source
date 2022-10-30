"""pandas基礎
欠損値(NaN, None)の扱いと処理方法
(欠損値を指定した値で埋める fillna)

[説明ページ]
https://tech.nkhn37.net/pandas-dropna-fillna/#_fillna
"""
import numpy as np
import pandas as pd

# Series
ser = pd.Series([1, 2, np.nan, np.nan, 5])

# 欠損値を指定した値で埋める
print(ser.fillna(0), '\n')

# DataFrame
df = pd.DataFrame([[1, 2, 3, np.nan],
                   [5, np.nan, np.nan, 8],
                   [np.nan, 10, np.nan, 12],
                   [np.nan, np.nan, np.nan, 16]],
                  index=[1, 2, 3, 4],
                  columns=['attr1', 'attr2', 'attr3', 'attr4'])

# 欠損値を指定した値で埋める
print(df.fillna(0))

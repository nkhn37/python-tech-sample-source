"""pandas基礎
欠損値(NaN, None)の扱いと処理方法
(フォワードで欠損値を埋める ffill)

[説明ページ]
https://tech.nkhn37.net/pandas-dropna-fillna/#_ffill
"""
import numpy as np
import pandas as pd

# Series
ser = pd.Series([1, 2, np.nan, np.nan, 5])

# フォワードで欠損値を埋める
print(ser.fillna(method='ffill'), '\n')

# DataFrame
df = pd.DataFrame([[1, 2, 3, np.nan],
                   [5, np.nan, np.nan, 8],
                   [np.nan, 10, np.nan, 12],
                   [np.nan, np.nan, np.nan, 16]],
                  index=[1, 2, 3, 4],
                  columns=['attr1', 'attr2', 'attr3', 'attr4'])

# フォワードで欠損値を埋める (行方向)
print(df.fillna(method='ffill'), '\n')

# フォワードで欠損値を埋める (列方向)
print(df.fillna(axis=1, method='ffill'))

"""pandas基礎
欠損値(NaN, None)の扱いと処理方法
(欠損値の削除方法 dropna)

[説明ページ]
https://tech.nkhn37.net/pandas-dropna-fillna/#_dropna
"""
import numpy as np
import pandas as pd

# Series
ser = pd.Series([1, np.nan, 3, None, 5])
print(ser.dropna(), '\n')

# DataFrame
df = pd.DataFrame([[1, np.nan, 3], [4, 5, None], [7, 8, 9]],
                  index=[1, 2, 3], columns=['attr1', 'attr2', 'attr3'])

# 行方向の削除
print(df.dropna(), '\n')

# 列方向の削除
print(df.dropna(axis=1))

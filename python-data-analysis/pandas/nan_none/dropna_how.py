"""pandas基礎
欠損値(NaN, None)の扱いと処理方法
(全て欠損値の場合に削除する how)

[説明ページ]
https://tech.nkhn37.net/pandas-dropna-fillna/#_how
"""
import numpy as np
import pandas as pd

# DataFrame
df = pd.DataFrame([[1, 2, np.nan], [np.nan, np.nan, np.nan], [7, 8, np.nan]],
                  index=[1, 2, 3], columns=['attr1', 'attr2', 'attr3'])

# 行方向の削除（全てNaNの行のみ削除）
print(df.dropna(how='all'), '\n')

# 列方向の削除（全てNaNの列のみ削除）
print(df.dropna(axis=1, how='all'))

"""pandas基礎
欠損値(NaN, None)の扱いと処理方法
(欠損値でないことを判定する notnull)

[説明ページ]
https://tech.nkhn37.net/pandas-dropna-fillna/#_notnull
"""
import numpy as np
import pandas as pd

# Series
ser = pd.Series([1, np.nan, 3, None, 5])
print(ser.notnull(), '\n')

# DataFrame
df = pd.DataFrame([[1, np.nan, 3], [4, 5, None]],
                  index=[1, 2], columns=['attr1', 'attr2', 'attr3'])
print(df.notnull())

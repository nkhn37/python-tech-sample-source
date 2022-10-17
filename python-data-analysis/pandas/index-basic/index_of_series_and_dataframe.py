"""pandas基礎
Indexの基本
(SeriesとDataFrameのインデックス)

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#pandasIndex
"""
import numpy as np
import pandas as pd

# Series
ser = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
print(ser)
print(ser.index)
print('\n')

# DataFrame
df = pd.DataFrame(np.arange(9).reshape((3, 3)),
                  index=[1, 2, 3],
                  columns=['A', 'B', 'C'])
print(df)
print(df.index)
print(df.columns)

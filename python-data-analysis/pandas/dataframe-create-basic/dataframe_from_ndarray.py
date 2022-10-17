"""pandas基礎
DataFrameの作成方法
(2次元のNumPy配列(ndarray)から作成する)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-create-basic/#2NumPyndarray
"""
import numpy as np
import pandas as pd

arr = np.arange(9).reshape((3, 3))
print(arr, '\n')

# 2次元のNumPy配列からDataFrameを作成する
df = pd.DataFrame(arr,
                  index=['A', 'B', 'C'],
                  columns=['attr1', 'attr2', 'attr3'])
print(df)

"""pandas基礎
SeriesからNumPy配列(ndarray)に変換する

[説明ページ]
https://tech.nkhn37.net/pandas-series-create-basic/#SeriesNumPyndarray
"""
import numpy as np
import pandas as pd

# NumPy ndarrayからSeriesへ変換する
arr = np.array([1, 5, 2, 4, 5])
data = pd.Series(arr)
print(data, '\n')

# SeriesからNumPy ndarrayへ変換する
arr_tmp = data.values
print(arr_tmp, type(arr_tmp))

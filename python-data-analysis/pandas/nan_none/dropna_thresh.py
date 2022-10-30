"""pandas基礎
欠損値(NaN, None)の扱いと処理方法
(欠損値以外のデータ数で削除を制御する thresh)

[説明ページ]
https://tech.nkhn37.net/pandas-dropna-fillna/#_thresh
"""
import numpy as np
import pandas as pd

# DataFrame
df = pd.DataFrame([[1, 2, 3, np.nan],
                   [5, 6, np.nan, 8],
                   [np.nan, 10, np.nan, 12],
                   [np.nan, np.nan, np.nan, 16]],
                  index=[1, 2, 3, 4],
                  columns=['attr1', 'attr2', 'attr3', 'attr4'])

# 行方向の削除 (欠損値以外が指定数値以上ある行を残す)
print(df.dropna(thresh=3), '\n')

# 列方向の削除 (欠損値以外が指定数値以上ある行を残す)
print(df.dropna(axis=1, thresh=3))

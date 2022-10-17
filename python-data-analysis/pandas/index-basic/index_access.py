"""pandas基礎
Indexの基本
(Indexオブジェクトに対するアクセス)

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#Index-3
"""
import pandas as pd

ind = pd.Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 要素へのアクセス
print(ind[1])
# スライスによるアクセス
print(ind[1:9:2])
# 各種情報へのアクセス
print(ind.size)
print(ind.shape)
print(ind.ndim)
print(ind.dtype)

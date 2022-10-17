"""pandas基礎
Indexの基本
(Indexオブジェクトはイミュータブル(immutable))

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#Indeximmutable
"""
import pandas as pd

ind = pd.Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Indexオブジェクトはイミュータブル（immutable）なため要素の変更はできない
ind[0] = 10

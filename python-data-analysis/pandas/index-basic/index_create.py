"""pandas基礎
Indexの基本
(Indexオブジェクトの作成例)

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#Index-2
"""
import pandas as pd

ind = pd.Index([1, 2, 3])
print(ind)

ind = pd.Index(["A", "B", "C"])
print(ind)

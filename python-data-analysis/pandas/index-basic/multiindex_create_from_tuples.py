"""pandasの基礎
MultiIndexの作成
階層構造を持つインデックスに適している
(from_tuplesでタプルから作成する場合)

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#MultiIndex
"""
import pandas as pd

# MultiIndexを作成 (from_tuples)
multi_index = pd.MultiIndex.from_tuples(
    [("A", 1), ("A", 2), ("B", 1), ("B", 2), ("B", 3)],
    names=["Level 1", "Level 2"],
)
print(multi_index, "\n")

# データフレームの作成
df_multi = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],
    index=multi_index,
    columns=["col1", "col2", "col3"],
)
print(df_multi)

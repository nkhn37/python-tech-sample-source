"""pandasの基礎
MultiIndexの作成
階層構造を持つインデックスに適している
(from_arraysでリストから作成する場合)

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#MultiIndex
"""
import pandas as pd

# MultiIndexを作成 (from_arrays)
multi_index = pd.MultiIndex.from_arrays(
    [["A", "A", "B", "B", "B"], [1, 2, 1, 2, 3]],
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

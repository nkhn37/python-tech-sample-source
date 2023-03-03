"""DataFrameによるCSVファイルの入出力
read_csv関数
(階層インデックスを指定する場合 index_col引数)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_index_col
"""
import pandas as pd

# 階層インデックスを指定する場合
df = pd.read_csv(
    "testdata_multi_index.csv",
    encoding="utf-8",
    index_col=["level1", "level2"],
)

print(df, "\n")
print(df.index, "\n")
print(df.dtypes)

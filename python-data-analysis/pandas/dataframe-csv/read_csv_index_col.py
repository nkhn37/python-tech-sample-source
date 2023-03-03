"""DataFrameによるCSVファイルの入出力
read_csv関数
(インデックスの列を指定する場合 index_col引数)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_index_col
"""
import pandas as pd

# インデックス列を指定して読み込む ※index_col=0のように列番号でも同じ
df = pd.read_csv("testdata.csv", encoding="utf-8", index_col="id")

print(df, "\n")
print(df.index, "\n")
print(df.dtypes)

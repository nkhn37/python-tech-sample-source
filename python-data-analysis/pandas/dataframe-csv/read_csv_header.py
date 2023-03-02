"""DataFrameによるcsvファイルの入出力
read_csv関数
(ヘッダー行を指定する場合 header引数)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_header
"""
import pandas as pd

# ヘッダー行を指定する
df = pd.read_csv("testdata_header.csv", encoding="utf-8", header=2)

print(df, "\n")
print(df.dtypes)

"""DataFrameによるcsvファイルの入出力
read_csv関数
(ヘッダー行がないcsvファイルを読み込む場合 header=None)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_headerNone
"""
import pandas as pd

# ヘッダー行がないCSVファイルを読み込む
df = pd.read_csv("testdata_header_none.csv", encoding="utf-8", header=None)

print(df, "\n")
print(df.dtypes)

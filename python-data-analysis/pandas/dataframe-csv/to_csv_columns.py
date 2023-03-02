"""DataFrameによるcsvファイルの入出力
to_csvメソッド
(特定の列のみ出力する columns引数)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_columns
"""
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("testdata.csv", encoding="utf-8")

# 指定した列名のみ出力する
df.to_csv("writedata_columns.csv", columns=["id", "data"])

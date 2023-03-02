"""DataFrameによるcsvファイルの入出力
to_csvメソッド
(区切り文字を指定する方法 sep引数)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_sep
"""
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("testdata.csv", encoding="utf-8")

# 区切り文字を指定する (\tでTSVファイルとして保存)
df.to_csv("writedata_sep.tsv", encoding="utf-8", sep="\t")

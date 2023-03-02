"""DataFrameによるcsvファイルの入出力
to_csvメソッド
(書き込みモード指定 mode引数 追記モード mode="a")

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_mode
"""
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("testdata.csv", encoding="utf-8")

# 追記モードで追加する場合
df.to_csv("writedata_mode_a.csv")
df.to_csv("writedata_mode_a.csv", mode="a", header=False)

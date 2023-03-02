"""DataFrameによるcsvファイルの入出力
to_csvメソッド
(書き込みモード指定 mode引数 上書き防止 mode="x")

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_mode
"""
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("testdata.csv", encoding="utf-8")

# 上書き防止 ファイルが存在しない場合:新規作成、存在する場合:エラー
df.to_csv("writedata_mode_x.csv", mode="x")

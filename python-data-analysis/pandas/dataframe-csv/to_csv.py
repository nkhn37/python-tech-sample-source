"""DataFrameによるcsvファイルの入出力
to_csvメソッド
(基本的な書き込み方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#i-2
"""
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("testdata.csv", encoding="utf-8")

# 別名でcsvを書き込む
df.to_csv("writedata.csv")

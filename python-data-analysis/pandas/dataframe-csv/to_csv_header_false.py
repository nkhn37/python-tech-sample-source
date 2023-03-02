"""DataFrameによるcsvファイルの入出力
to_csvメソッド
(ヘッダーを出力しない書き込み方法 header=False)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_headerFalse
"""
import pandas as pd

# csvファイルを読み込む
df = pd.read_csv("testdata.csv", encoding="utf-8")

# 別名でcsvを書き込む (ヘッダーを出力しない)
df.to_csv("writedata_header_false.csv", encoding="utf-8", header=False)

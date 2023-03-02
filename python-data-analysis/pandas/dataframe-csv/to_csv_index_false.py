"""DataFrameによるcsvファイルの入出力
to_csvメソッド
(インデックスは出力しない書き込み方法 index=False)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_indexFalse
"""
import pandas as pd

# csvファイルを読み込む
df = pd.read_csv("testdata.csv", encoding="utf-8")

# 別名でcsvを書き込む (インデックスは出力しない)
df.to_csv("writedata_index_false.csv", encoding="utf-8", index=False)

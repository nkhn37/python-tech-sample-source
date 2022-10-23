"""pandas基礎
DataFrameによるcsvファイルの入出力
to_csv
(インデックスは出力しない書き込み方法 index引数)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_index
"""
import pandas as pd

# csvファイルを読み込む
df = pd.read_csv('testdata.csv', encoding='utf-8')

# 別名でcsvを書き込む (インデックスは出力しない)
df.to_csv('writedata_2.csv', encoding='utf-8', index=False)

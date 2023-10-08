"""Parquetファイルの入出力
読み込み方法 (pd.read_parquet)

[説明ページ]
https://tech.nkhn37.net/pandas-parquet/#Parquet_read_parquet
"""
import pandas as pd

# Parquetデータの読み込み
df = pd.read_parquet("./data.parquet")
print(df)

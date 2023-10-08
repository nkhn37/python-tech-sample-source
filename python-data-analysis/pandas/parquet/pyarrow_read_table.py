"""Parquetファイルの入出力
pyarrowを直接使った読み込み方法

[説明ページ]
https://tech.nkhn37.net/pandas-parquet/#pyarrow
"""
from pyarrow import parquet

# Parquetデータの読み込み
table = parquet.read_table("./data_arrow.parquet")
print(table, "\n")

# テーブルを辞書形式に変換
data = table.to_pydict()
print(data)

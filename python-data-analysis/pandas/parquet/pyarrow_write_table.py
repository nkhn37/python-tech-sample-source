"""Parquetファイルの入出力
pyarrowを直接使った書き込み方法

[説明ページ]
https://tech.nkhn37.net/pandas-parquet/#pyarrow
"""
import pyarrow as pa
from pyarrow import parquet

# データの準備
data = {"column1": [1, 2, 3, 4, 5], "column2": ["A", "B", "C", "D", "E"]}
print(data, "\n")

# Arrowテーブル形式に変換する
table = pa.Table.from_pydict(data)
print(table)

# Parquet形式で保存する
parquet.write_table(table, "./data_arrow.parquet")

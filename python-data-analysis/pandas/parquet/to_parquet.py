"""Parquetファイルの入出力
書き込み方法(to_parquet)

[説明ページ]
https://tech.nkhn37.net/pandas-parquet/#Parquet_to_parquet
"""
import pandas as pd

# データの準備
data = {"column1": [1, 2, 3, 4, 5], "column2": ["A", "B", "C", "D", "E"]}

# pandasデータフレームの作成
df = pd.DataFrame(data, index=["a", "b", "c", "d", "e"])
print(df)

# parquet形式で保存する
df.to_parquet("./data.parquet")

# # indexを保存しない場合
# df.to_parquet("./data.parquet", index=False)

"""DataFrameによるCSVファイルの入出力
read_csv関数
(取得するデータ型を指定する方法 dtype引数)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_dtype
"""
import pandas as pd

# 取得するデータの方を指定する
df = pd.read_csv(
    "testdata.csv", encoding="utf-8", dtype={"id": "float64", "data": str}
)

print(df, "\n")
print(df.dtypes)

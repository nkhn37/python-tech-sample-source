"""DataFrameによるcsvファイルの入出力
read_csv関数
(parse_dates引数による日付列を指定して取り込む方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_parse_dates
"""
import pandas as pd

# 日付列を指定してデータを読み込む (parse_dates引数)
df = pd.read_csv(
    "testdata.csv",
    encoding="utf-8",
    dtype={"id": int, "data": int, "text": str},
    parse_dates=["update_datetime"],
)

print(df, "\n")
print(df.dtypes)

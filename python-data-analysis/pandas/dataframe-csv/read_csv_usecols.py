"""pandas基礎
DataFrameによるcsvファイルの入出力
read_csv
(特定の列だけ指定して読み込む方法 usecols引数)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#_usecols
"""
import pandas as pd

# 特定の列だけを指定して読み込む
df = pd.read_csv('testdata.csv', encoding='utf-8', usecols=['id', 'text'])

print(df, '\n')
print(df.dtypes)

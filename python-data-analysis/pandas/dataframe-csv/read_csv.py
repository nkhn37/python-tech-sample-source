"""pandas基礎
DataFrameによるcsvファイルの入出力
read_csv
(基本的な読み込み方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#i
"""
import pandas as pd

# csvファイルを読み込む
df = pd.read_csv('testdata.csv', encoding='utf-8')

print(df, '\n')
print(df.dtypes)

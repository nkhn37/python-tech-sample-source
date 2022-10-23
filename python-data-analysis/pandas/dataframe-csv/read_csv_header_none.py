"""pandas基礎
DataFrameによるcsvファイルの入出力
read_csv
(ヘッダー行がないcsvファイルを読み込む場合)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-csv/#csv
"""
import pandas as pd

# ヘッダー行がないcsvファイルを読み込む
df = pd.read_csv('testdata_2.csv',  encoding='utf-8',
                 header=None)

print(df, '\n')
print(df.dtypes)

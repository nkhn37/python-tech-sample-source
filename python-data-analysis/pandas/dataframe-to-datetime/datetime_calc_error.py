"""pandas基礎
DataFrameで日付・時間の列を処理する方法
(エラーとなってしまう場合)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-datetime/#i
"""
import pandas as pd

df = pd.read_csv('sample_datetime.csv', encoding='utf-8')
df['diff_datetime'] = df['end_datetime'] - df['start_datetime']

print(df, '\n')
print(df.dtypes)

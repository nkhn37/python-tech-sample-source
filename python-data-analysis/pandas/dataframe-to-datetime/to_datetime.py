"""pandas基礎
DataFrameで日付・時間の列を処理する方法 to_datetime

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-datetime/#datetime_to_datetime
"""
import pandas as pd

df = pd.read_csv('sample_datetime.csv', encoding='utf-8')
print(df, '\n')
print(df.dtypes, '\n')

# 型変換を実施する
df['start_datetime'] = pd.to_datetime(df['start_datetime'])
df['end_datetime'] = pd.to_datetime(df['end_datetime'])

# 時間の差分を計算する
df['diff_datetime'] = df['end_datetime'] - df['start_datetime']

print(df, '\n')
print(df.dtypes)

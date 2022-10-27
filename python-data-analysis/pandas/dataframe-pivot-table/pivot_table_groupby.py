"""pandas基礎
groupbyでピボットテーブルを作成する方法

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-pivot-table/#_groupby
"""
import pandas as pd

# ===== サンプルデータの読み込み
df = pd.read_csv('sample.csv')
# print(df)
# print(df.dtypes)

# ===== データ加工
# 日付列をdatetimeに変更
df['date'] = pd.to_datetime(df['date'])
# 年・月・日の列を作成
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# マニュアルでpivot_tableを作成
print(df.groupby(['product_code', 'month'])['price'].sum().unstack())

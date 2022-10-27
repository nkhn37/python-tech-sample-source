"""pandas基礎
DataFrameのpivot_tableでピボットテーブルを扱う
(基本的なpivot_tableの使い方)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-pivot-table/#pivot_table-2
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

# ===== pivot_table
pt = df.pivot_table('price',
                    index='product_code',
                    columns='month',
                    aggfunc='sum')
print(pt)

"""pandas基礎
DataFrameのpivot_tableでピボットテーブルを扱う
(多重ピボットテーブル: 複数レベルの指定)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-pivot-table/#i
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

# ===== pivot_table（複数レベルでの指定）
pt = df.pivot_table('price',
                    index=['product_code', 'client'],
                    columns=['year', 'month', 'day'],
                    aggfunc='sum')
# NaN部分を0で埋めて表示
print(pt.fillna(0))

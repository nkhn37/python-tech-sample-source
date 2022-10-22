"""pandas基礎
DataFrameのデータ選択方法
(列名を指定して特定の列を取得する方法:基本的な使用方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-data-selection/#i-2
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
attr2 = pd.Series([60, 70, 80, 90, 100], index=['A', 'B', 'C', 'D', 'E'])
df = pd.DataFrame({'attr1': attr1, 'attr2': attr2})
print(df, '\n')

# 列名を指定して特定の列情報を取得する（辞書のようにアクセス）
print(df['attr1'], '\n')
# 列名を変数のようにして読み込むことも可能
print(df.attr1)

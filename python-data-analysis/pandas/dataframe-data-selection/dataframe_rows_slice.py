"""pandas基礎
DataFrameのデータ選択方法
(スライスで特定のキーを持つ行を選択する方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-data-selection/#i-6
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
attr2 = pd.Series([60, 70, 80, 90, 100], index=['A', 'B', 'C', 'D', 'E'])
df = pd.DataFrame({'attr1': attr1, 'attr2': attr2})
print(df, '\n')

# ===== スライスで特定のキーを持つ行を選択する
# 明示的なインデックスを使用する場合
print(df['B':'D'], '\n')
# 暗黙的なインデックスを使用する場合
print(df[1:3])

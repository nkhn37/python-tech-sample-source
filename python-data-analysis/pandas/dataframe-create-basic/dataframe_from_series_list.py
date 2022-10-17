"""pandas基礎
DataFrameの作成方法
(Seriesの辞書から作成する)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-create-basic/#Series-2
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
attr2 = pd.Series([60, 70, 80, 90, 100], index=['A', 'B', 'C', 'F', 'G'])
dics = {'attr1': attr1, 'attr2': attr2}
print(dics, '\n')

# Seriesの辞書からDataFrameを作成する
df = pd.DataFrame(dics)
print(df)

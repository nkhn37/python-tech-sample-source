"""pandas基礎
DataFrameの作成方法
(辞書のリストから作成する)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-create-basic/#i
"""
import pandas as pd

dics = [{'attr1': 1, 'attr2': 2},
        {'attr1': 3, 'attr3': 4},
        {'attr2': 5, 'attr3': 6}]
print(dics, '\n')

# 辞書のリストからDataFrameを作成。欠損値がある場合はNaNが補完される
df = pd.DataFrame(dics)
print(df)

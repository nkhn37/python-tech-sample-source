"""pandas基礎
DataFrameのデータ選択方法
(特定の列情報を任意順序に並べたデータを取得する方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-data-selection/#i-4
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=["A", "B", "C", "D", "E"])
attr2 = pd.Series([60, 70, 80, 90, 100], index=["A", "B", "C", "D", "E"])
df = pd.DataFrame({"attr1": attr1, "attr2": attr2})
print(df, "\n")

# 特定の列名を指定し、任意順序で並べ替えてデータを取得する（同じ列の複製も可能）
print(df[["attr2", "attr1", "attr1", "attr2"]])

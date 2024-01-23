"""pandas基礎
DataFrameのデータ選択方法
(マスキングで特定条件に一致する行を選択する方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-data-selection/#i-8
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=["A", "B", "C", "D", "E"])
attr2 = pd.Series([60, 70, 80, 90, 100], index=["A", "B", "C", "D", "E"])
df = pd.DataFrame({"attr1": attr1, "attr2": attr2})
print(df, "\n")

# 特定の条件に一致する行を選択する
print(df[(df["attr1"] > 10) & (df["attr2"] < 100)])

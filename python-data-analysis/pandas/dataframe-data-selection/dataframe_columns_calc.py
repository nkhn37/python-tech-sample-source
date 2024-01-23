"""pandas基礎
DataFrameのデータ選択方法
(既存の列を用いて計算した結果列を作成する方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-data-selection/#i-5
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=["A", "B", "C", "D", "E"])
attr2 = pd.Series([60, 70, 80, 90, 100], index=["A", "B", "C", "D", "E"])
df = pd.DataFrame({"attr1": attr1, "attr2": attr2})
print(df, "\n")

# 既存の列から計算して新しい列を作成する
df["sum"] = df["attr1"] + df["attr2"]
print(df)

"""pandas基礎
DataFrameのデータ選択方法
(任意の行、列の値を選択する方法: loc, iloc, at, iat)
 特定位置の情報を選択する

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-data-selection/#i-8
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=["A", "B", "C", "D", "E"])
attr2 = pd.Series([60, 70, 80, 90, 100], index=["A", "B", "C", "D", "E"])
attr3 = pd.Series([110, 120, 130, 140, 150], index=["A", "B", "C", "D", "E"])
df = pd.DataFrame({"attr1": attr1, "attr2": attr2, "attr3": attr3})
print(df, "\n")

# 特定の位置を選択する
# 明示的なインデックスを使用する場合
print(df.loc["C", "attr2"], "\n")
# atを使っても同様のことができる
print(df.at["C", "attr2"], "\n")

# 暗黙的なインデックスを使用する場合
print(df.iloc[2, 1], "\n")
# iatを使っても同様のことができる
print(df.iat[2, 1])

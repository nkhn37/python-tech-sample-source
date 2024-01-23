"""pandas基礎
DataFrameのデータ選択方法
(列名を指定して特定の列を取得する方法:列名とメソッド名の重複に注意)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-data-selection/#i-3
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=["A", "B", "C", "D", "E"])
attr2 = pd.Series([60, 70, 80, 90, 100], index=["A", "B", "C", "D", "E"])
df = pd.DataFrame({"attr1": attr1, "pop": attr2})
print(df, "\n")

# メソッド名と重なる場合、辞書形式の取得と属性名での取得は一致しない
print(f"df.pop: \n{df.pop}\n")
print(f"df['pop']: \n{df['pop']}\n")
print(df.pop is df["pop"])

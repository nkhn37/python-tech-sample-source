"""pandas基礎
DataFrameのデータ選択方法
(queryを用いた条件指定によるデータ選択方法)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-data-selection/#query
"""
import pandas as pd

attr1 = pd.Series([10, 20, 30, 40, 50], index=["A", "B", "C", "D", "E"])
attr2 = pd.Series([60, 70, 80, 90, 100], index=["A", "B", "C", "D", "E"])
df = pd.DataFrame({"attr1": attr1, "attr2": attr2})
print(df, "\n")

# queryを用いて条件に一致する行を選択する
# ※ 内部的に文字列評価を行うためパフォーマンスに影響ある場合があることに注意
print(df.query("attr1 > 10 and attr2 < 100"), "\n")

# 変数を使ったクエリの記載も可能
threshold1 = 20
threshold2 = 90
print(df.query("attr1 >= @threshold1 and attr2 < @threshold2"))

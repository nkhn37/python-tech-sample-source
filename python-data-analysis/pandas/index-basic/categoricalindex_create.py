"""pandasの基礎
CategoricalIndexの作成
限定された数のカテゴリーを持つデータに適している

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#CategoricalIndex
"""
import pandas as pd

# カテゴリーで使うラベルのリスト
category_data = ["High", "Medium", "Low", "Low"]

# CategoricalIndexの作成
# categoriesに指定するものがカテゴリーとして許容するリスト
# ordered=Trueとすることで"Low"<"Medium"<"High"の順序があることを示す
category_index = pd.CategoricalIndex(
    category_data,
    categories=["Low", "Medium", "High"],
    ordered=True,
)
print(category_index, "\n")

# データフレームの作成
df_categorical = pd.DataFrame(
    data=[[70, 80, 90], [40, 50, 60], [10, 20, 30], [10, 5, 10]],
    index=category_index,
    columns=["col1", "col2", "col3"],
)
print(df_categorical)

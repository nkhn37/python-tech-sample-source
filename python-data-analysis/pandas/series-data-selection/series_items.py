"""pandas基礎
Seriesのデータ選択方法
(要素を取得してリストや辞書に変換する ~items~)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#_items
"""
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(data, "\n")

# 要素を取得して、リストや辞書に変換する
print(f"data.items(): {data.items()}")
print(f"list(data.items()): {list(data.items())}")
print(f"dict(data.items()): {dict(data.items())}", "\n")

# itemsはfor文で使用可能
print("for文で各値を取得")
for idx, val in data.items():
    print(idx, val)

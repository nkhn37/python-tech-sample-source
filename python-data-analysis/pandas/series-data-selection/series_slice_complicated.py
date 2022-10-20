"""pandas基礎
Seriesのデータ選択方法
(スライスでのデータ選択と複雑さ)

[説明ページ]
https://tech.nkhn37.net/pandas-series-data-selection/#i-6
"""
import pandas as pd

data = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[1, 2, 3, 4, 5])
print(data, '\n')

# 要素を参照（明示的なインデックスを参照）
print(data[1], '\n')
# スライスによるアクセス(暗黙的なインデックスを参照）
print(data[1:4])

"""pandas基礎
DataFrameをgroupbyでグループ化して集約する方法
(基本的な使い方)

[説明ページ]
https://tech.nkhn37.net/pandas-groupby-aggregation/#groupbyDataFrame-2
"""
import pandas as pd

quality_result = pd.DataFrame(
    {'serial_no': ['S001', 'S002', 'S003', 'S004', 'S005',
                   'S006', 'S007', 'S008', 'S009', 'S010'],
     'item_code': ['A', 'A', 'B', 'B', 'C', 'A', 'A', 'B', 'C', 'C'],
     'quality_val1': [100, 150, 20, 10, 50, 120, 80, 5, 55, 40],
     'quality_val2': [1, 2, 100, 120, 20, 5, 7, 90, 10, 10]}
)
print(quality_result, '\n')

# item_codeでグループ化
gr = quality_result.groupby('item_code')
print(gr, '\n')

# グループごとに集約を計算
# print(quality_result.groupby('item_code').sum())
print(gr.sum())

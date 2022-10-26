"""pandas基礎
DataFrameをgroupbyでグループ化して集約する方法
(グループごとに繰り返し処理する方法)

[説明ページ]
https://tech.nkhn37.net/pandas-groupby-aggregation/#i-2
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

# グループごとに取り出して処理をする
for (item_code, group) in quality_result.groupby('item_code'):
    print(f'item_code: {item_code}')
    print(f'group_data:\n{group}')
    print(f"group['quality_val1'].sum() = {group['quality_val1'].sum()}", '\n')

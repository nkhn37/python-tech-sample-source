"""pandas基礎
DataFrameを結合する方法
merge (1対1の結合)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-merge-join/#11
"""
import pandas as pd

# 製品一覧
product_list = pd.DataFrame(
    {'serial_no': ['A001', 'B001', 'C001', 'C002', 'D001'],
     'customer_id': ['cid_1', 'cid_1', 'cid_2', 'cid_2', 'cid_3'],
     'product_code': ['p_a', 'p_b', 'p_c', 'p_c', 'p_d']
     }
)

# 品質情報
quality_result = pd.DataFrame(
    {'serial_no': ['A001', 'B001', 'C001', 'C002', 'D001'],
     'quality': [100, 200, 300, 400, 500]
     }
)

print(f'製品一覧(product_list):\n{product_list}\n')
print(f'品質実績(quality_result):\n{quality_result}\n')

# 製品一覧と品質情報をマージ（1対1）
result_df = pd.merge(product_list, quality_result)

print(f'製品一覧と品質情報をマージ（1対1）:\n{result_df}')

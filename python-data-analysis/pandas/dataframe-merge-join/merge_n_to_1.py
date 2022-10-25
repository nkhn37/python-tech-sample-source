"""pandas基礎
DataFrameを結合する方法
merge (多対1の結合)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-merge-join/#1
"""
import pandas as pd

# 製品一覧
product_list = pd.DataFrame(
    {'serial_no': ['A001', 'B001', 'C001', 'C002', 'D001'],
     'customer_id': ['cid_1', 'cid_1', 'cid_2', 'cid_2', 'cid_3'],
     'product_code': ['p_a', 'p_b', 'p_c', 'p_c', 'p_d']
     }
)

# 顧客情報
customer_info = pd.DataFrame(
    {'customer_id': ['cid_1', 'cid_2', 'cid_3'],
     'customer_name': ['顧客１', '顧客２', '顧客３']
     }
)

print(f'製品一覧(product_list):\n{product_list}\n')
print(f'顧客情報(customer_info):\n{customer_info}\n')

# 製品一覧と顧客情報をマージ（多対1）
result_df = pd.merge(product_list, customer_info)

print(f'製品一覧と顧客情報をマージ（多対1）:\n{result_df}')

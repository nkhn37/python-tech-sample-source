"""pandas基礎
DataFrameを結合する方法
merge (多対多の結合)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-merge-join/#i
"""
import pandas as pd

# 製品一覧
product_list = pd.DataFrame(
    {'serial_no': ['A001', 'B001', 'C001', 'C002', 'D001'],
     'customer_id': ['cid_1', 'cid_1', 'cid_2', 'cid_2', 'cid_3'],
     'product_code': ['p_a', 'p_b', 'p_c', 'p_c', 'p_d']
     }
)

# 製品特徴
product_feature = pd.DataFrame(
    {'product_code': ['p_a', 'p_a', 'p_b', 'p_b', 'p_c', 'p_c',
                      'p_d', 'p_d', 'p_d'],
     'feature': ['a-1', 'a-2', 'b-1', 'b-2', 'c-1', 'c-2',
                 'd-1', 'd-2', 'd-3']
     }
)

print(f'製品一覧(product_list):\n{product_list}\n')
print(f'製品特徴(product_feature):\n{product_feature}\n')

# 製品一覧と製品特徴をマージ（多対多）
result_df = pd.merge(product_list, product_feature)

print(f'製品一覧と製品特徴をマージ（多対多）:\n{result_df}')

"""pandas基礎
DataFrameを結合する場合
merge (left_on, right_on, left_index, right_indexの混在での結合)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-merge-join/#left_on_right_on_left_index_right_index
"""
import pandas as pd

# 製品一覧
product_list = pd.DataFrame(
    {'serial_no': ['A001', 'B001', 'C001', 'C002', 'D001'],
     'customer_id': ['cid_1', 'cid_1', 'cid_2', 'cid_2', 'cid_3'],
     'product_code': ['p_a', 'p_b', 'p_c', 'p_c', 'p_d']
     }
)
# serial_no列をインデックスに設定
product_list = product_list.set_index('serial_no')

# 品質情報
quality_result = pd.DataFrame(
    {'serial_no': ['A001', 'B001', 'C001', 'C002', 'D001'],
     'quality': [100, 200, 300, 400, 500]
     }
)

print(f'製品一覧(product_list):\n{product_list}\n')
print(f'品質実績(quality_result):\n{quality_result}\n')

# インデックスを使ってマージ（左：インデックスを使用、右：列名を指定）
result_df = pd.merge(product_list, quality_result,
                     left_index=True, right_on='serial_no')

print(f'インデックスを使ってマージ（左：インデックス、右：列名）\n{result_df}')

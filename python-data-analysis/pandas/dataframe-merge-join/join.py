"""pandas基礎
DataFrameを結合する場合
joinメソッド (インデックスでの結合)

[説明ページ]
https://tech.nkhn37.net/pandas-dataframe-merge-join/#join
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
# serial_no列をインデックスに設定
quality_result = quality_result.set_index('serial_no')

print(f'製品一覧(product_list):\n{product_list}\n')
print(f'品質実績(quality_result):\n{quality_result}\n')

# joinメソッドを使ってインデックスで結合
result_df = product_list.join(quality_result)

print(f'joinメソッドを使ってインデックスで結合:\n{result_df}')

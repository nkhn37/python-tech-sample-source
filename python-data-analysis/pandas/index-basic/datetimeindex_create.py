"""pandasの基礎
DatetimeIndexの作成
時系列データのためのインデックスに適している

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#DatetimeIndex
"""
import pandas as pd

# 時間単位のDatetimeIndexを作成
date_index_h = pd.date_range(
    "2024-01-01",
    periods=5,
    freq="H",
)
print(date_index_h, "\n")

# データフレームの作成
df_time_value = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],
    index=date_index_h,
    columns=["val1", "val2", "val3"],
)
print(df_time_value)

# # 最初(start)と最後(end)を指定することも可能
# # start、end、periods（時間の数）の3引数を同時に使用することはできないので注意
# date_index_s_e = pd.date_range(
#     start="2024-01-01 00:00:00",
#     end="2024-01-01 04:00:00",
#     freq="H",
# )
# print(date_index_s_e)

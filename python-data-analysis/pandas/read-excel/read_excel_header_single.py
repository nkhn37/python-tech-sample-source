"""pandas基礎
Excelファイルを読み込む方法 read_excel
(ヘッダーを指定する方法 header)

単一行をヘッダーに指定する場合

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i-5
"""
import pandas as pd

# ヘッダー行を指定する(単一行の場合)
df = pd.read_excel('excel2.xlsx',
                   sheet_name='sample_1',
                   header=1)
print(df)

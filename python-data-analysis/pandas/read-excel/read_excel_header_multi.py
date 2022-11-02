"""pandas基礎
Excelファイルを読み込む方法 read_excel
(ヘッダーを指定する方法 header)

複数行をヘッダーに指定する場合

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i-6
"""
import pandas as pd

# ヘッダー行を指定する(複数行の場合)
df = pd.read_excel('excel2.xlsx',
                   sheet_name='sample_2',
                   header=[1, 2])
print(df)

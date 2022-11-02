"""pandas基礎
Excelファイルを読み込む方法 read_excel
(ヘッダーを指定する方法 header)

ヘッダー行がないデータを読み込む場合

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i-7
"""
import pandas as pd

# ヘッダー行がないファイルを読み込む
df = pd.read_excel('excel2.xlsx',
                   sheet_name='sample_3',
                   header=None)
print(df)

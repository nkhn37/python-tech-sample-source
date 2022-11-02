"""pandas基礎
Excelファイルを読み込む方法 read_excel
(シート名を指定して読み込む方法)

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i-2
"""
import pandas as pd

# シート名を指定して読み込む
df = pd.read_excel('excel1.xlsx',
                   sheet_name='sample_1')
print(df)

"""pandas基礎
Excelファイルを読み込む方法 read_excel
(読み込む列を指定する方法 usecols)

列名称で指定する場合

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i-10
"""
import pandas as pd

# 読み込む列を指定する（列名称で指定）
df = pd.read_excel('excel1.xlsx',
                   usecols=['product_code', 'client', 'price'])
print(df)

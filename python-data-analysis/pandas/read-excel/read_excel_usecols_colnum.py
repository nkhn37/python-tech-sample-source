"""pandas基礎
Excelファイルを読み込む方法 read_excel
(読み込む列を指定する方法 usecols)

列番号で指定する場合

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i-11
"""
import pandas as pd

# 列の指定方法（intで指定）
df = pd.read_excel('excel1.xlsx',
                   usecols=[1, 2, 4])
print(df)

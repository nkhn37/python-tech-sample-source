"""pandas基礎
Excelファイルを読み込む方法 read_excel
(読み込む列を指定する方法 usecols)

Excelの列名(A, B, ...)で指定する場合

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#ExcelA_B
"""
import pandas as pd

# 列の指定方法（Excelの列(A,B,...)でまとめて指定）
df = pd.read_excel('excel1.xlsx',
                   usecols='B:C, E')
print(df)

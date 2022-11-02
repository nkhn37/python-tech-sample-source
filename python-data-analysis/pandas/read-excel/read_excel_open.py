"""pandas基礎
Excelファイルを読み込む方法 read_excel
(openで開いたファイルから読み込む方法)

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#open
"""
import pandas as pd

# openで開いたファイルから読み込む
with open('excel1.xlsx', 'rb') as f:
    df = pd.read_excel(f)

print(df)

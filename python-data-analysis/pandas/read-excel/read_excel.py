"""pandas基礎
Excelファイルを読み込む方法 read_excel
(基本的な読み込み方法)

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i
"""
import pandas as pd

# Excelファイルを指定して読み込む
df = pd.read_excel('excel1.xlsx')
print(df)

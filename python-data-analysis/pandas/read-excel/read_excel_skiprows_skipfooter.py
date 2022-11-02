"""pandas基礎
Excelファイルを読み込む方法 read_excel
(ヘッダーやフッタを読み飛ばす方法 skiprows, skipfooter)

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#_skiprows_skipfooter
"""
import pandas as pd

# 上下のヘッダーやフッターを読み飛ばす
df = pd.read_excel('excel3.xlsx',
                   skiprows=3,
                   skipfooter=3)
print(df)

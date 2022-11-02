"""pandas基礎
Excelファイルを読み込む方法 read_excel
(インデックス列を指定する方法 index_col)

単一列をインデックス列に指定する方法

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i-8
"""
import pandas as pd

# インデックス列を指定する(単一列の場合)
df = pd.read_excel('excel1.xlsx',
                   index_col=1)
print(df)

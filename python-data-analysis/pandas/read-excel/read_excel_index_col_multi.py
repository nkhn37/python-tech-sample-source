"""pandas基礎
Excelファイルを読み込む方法 read_excel
(インデックス列を指定する方法 index_col)

複数列をインデックス列に指定する方法

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#i-9
"""
import pandas as pd

# インデックス列を指定する(複数列の場合)
df = pd.read_excel('excel1.xlsx',
                   index_col=[1, 2])
print(df)

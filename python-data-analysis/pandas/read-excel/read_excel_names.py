"""pandas基礎
Excelファイルを読み込む方法 read_excel
(列名称を書き換えて読み込む方法 names)

[説明ページ]
https://tech.nkhn37.net/pandas-read-excel/#_names
"""
import pandas as pd

# 列名称を変更して読み込む
df = pd.read_excel('excel1.xlsx',
                   names=['製造番号', '製品コード', '顧客', '日付', '価格'])
print(df)

"""for文基礎
zipで複数リストをまとめてfor文で処理する方法
（タプルで要素を取得する場合）

[説明ページ]
https://tech.nkhn37.net/python-for-zip/#tuplefor
"""
data1 = [10, 20, 30, 40, 50]
data2 = ["A", "B", "C", "D", "E"]

# zipで複数リストをまとめて処理する (タプルで取得する)
for tpl in zip(data1, data2):
    print(f"dt1: {tpl[0]}, dt2: {tpl[1]}")

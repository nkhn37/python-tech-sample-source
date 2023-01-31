"""for文基礎
enumerateを用いたfor文の使い方
（タプルで要素を取得する場合）

[説明ページ]
https://tech.nkhn37.net/python-for-enumerate/#tuplefor
"""
data = ["A", "B", "C", "D", "E"]

# enumerateの返却値をtupleで受け取る
for tpl in enumerate(data):
    print(f"idx: {tpl[0]}, dt: {tpl[1]}")

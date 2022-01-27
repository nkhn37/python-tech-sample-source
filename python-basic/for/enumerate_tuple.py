"""for文基礎
enumerate関数を用いたfor文の使い方
（タプルで要素を取得する場合）

[説明ページ]
https://tech.nkhn37.net/python-for-enumerate/#enumeratefor
"""
data = ['A', 'B', 'C', 'D', 'E']

# tupleで受け取る
for tpl in enumerate(data):
    print(f'idx: {tpl[0]}, dt: {tpl[1]}')

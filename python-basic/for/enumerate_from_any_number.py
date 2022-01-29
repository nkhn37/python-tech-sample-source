"""for文基礎
enumerateで任意のインデックス数値から開始する方法

[説明ページ]
https://tech.nkhn37.net/python-for-enumerate/#enumerate
"""
# enumerateのインデックス開始数値を指定する
data = ['A', 'B', 'C', 'D', 'E']

for idx, dt in enumerate(data, 5):
    print(f'idx: {idx}, dt: {dt}')

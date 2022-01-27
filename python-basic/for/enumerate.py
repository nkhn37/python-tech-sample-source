"""for文基礎
enumerate関数を用いたfor文の使い方
（基本的な使い方）

[説明ページ]
https://tech.nkhn37.net/python-for-enumerate/#enumeratefor
"""
# enumerate関数
data = ['A', 'B', 'C', 'D', 'E']

for idx, dt in enumerate(data):
    print(f'idx: {idx}, dt: {dt}')

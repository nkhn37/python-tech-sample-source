"""集合基礎
和集合の計算方法

[説明ページ]
https://tech.nkhn37.net/python-set-calc-comparison/#i-2
"""
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# 和集合
print(f'a | b : {a | b}')
print(f'a.union(b) : {a.union(b)}')
print(f'b.union(a) : {b.union(a)}')

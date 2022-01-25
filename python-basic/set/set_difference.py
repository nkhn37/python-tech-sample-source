"""集合基礎
差集合の計算方法

[説明ページ]
https://tech.nkhn37.net/python-set-calc-comparison/#i-3
"""
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# 差集合
print(f'a - b : {a - b}')
print(f'a.difference(b) : {a.difference(b)}')
print(f'b - a : {b - a}')
print(f'b.difference(a) : {b.difference(a)}')

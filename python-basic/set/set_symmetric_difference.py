"""集合基礎
排他的論理和の計算方法

[説明ページ]
https://tech.nkhn37.net/python-set-calc-comparison/#i-4
"""
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# 排他的論理和
print(f'a ^ b : {a ^ b}')
print(f'a.symmetric_difference(b) : {a.symmetric_difference(b)}')
print(f'b.symmetric_difference(a) : {b.symmetric_difference(a)}')

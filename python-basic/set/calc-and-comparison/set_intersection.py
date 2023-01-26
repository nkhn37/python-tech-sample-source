"""集合基礎
積集合の計算方法

[説明ページ]
https://tech.nkhn37.net/python-set-calc-comparison/#i
"""
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# 積集合の計算
print(f"a & b: {a & b}")
print(f"a.intersection(b): {a.intersection(b)}")
print(f"b & a: {b & a}")
print(f"b.intersection(a): {b.intersection(a)}")

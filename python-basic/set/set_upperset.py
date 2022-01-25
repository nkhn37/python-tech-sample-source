"""集合基礎
集合の包含関係の判定方法
（上位集合と真上位集合）

[説明ページ]
https://tech.nkhn37.net/python-set-calc-comparison/#i-5
"""
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {1, 2, 3, 4, 5}

# aはbの上位集合
print(f'a >= b : {a >= b}')
print(f'a.issuperset(b) : {a.issuperset(b)}')
# aはbの真上位集合
print(f'a > b : {a > b}')

print('===== bがaと同じ集合であったとすると')
# aはbの真上位集合ではない
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f'a > b : {a > b}')

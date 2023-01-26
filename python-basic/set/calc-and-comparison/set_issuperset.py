"""集合基礎
集合の包含関係の判定方法
（上位集合と真上位集合）

[説明ページ]
https://tech.nkhn37.net/python-set-calc-comparison/#i-6
"""
# aはbの真上位集合
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {1, 2, 3, 4, 5}

print("===== aはbの真上位集合である場合")
print(f"a >= b: {a >= b}")
print(f"a.issuperset(b): {a.issuperset(b)}")
print(f"a > b: {a > b}")

# aはbの上位集合であるが、真上位集合ではない
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("===== aはbの上位集合であるが、真上位集合ではない場合")
print(f"a >= b: {a >= b}")
print(f"a.issuperset(b): {a.issuperset(b)}")
print(f"a > b: {a > b}")

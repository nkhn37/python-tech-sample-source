"""集合基礎
集合の包含関係の判定方法
（集合が等しいかの判定）

[説明ページ]
https://tech.nkhn37.net/python-set-calc-comparison/#i-5
"""
# aとbは等しい
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5}

print("===== aとbが等しい場合")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")

# aとbは等しくない
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("===== aとbが等しくない場合")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")

"""集合基礎
集合の包含関係の判定方法
（部分集合と真部分集合）

[説明ページ]
https://tech.nkhn37.net/python-set-calc-comparison/#i-7
"""
# bはaの真部分集合
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {1, 2, 3, 4, 5}

print("===== bはaの真部分集合である場合")
print(f"b <= a: {b <= a}")
print(f"b.issubset(a): {b.issubset(a)}")
print(f"b < a: {b < a}")

# bはaの部分集合であるが、真部分集合ではない
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("===== bはaの部分集合であるが、真部分集合ではない場合")
print(f"b <= a: {b <= a}")
print(f"b.issubset(a): {b.issubset(a)}")
print(f"b < a: {b < a}")

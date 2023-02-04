"""if文基礎
複数演算子を連結した条件式の記載

[説明ページ]
https://tech.nkhn37.net/python-if-basic/#i
"""
numbers = range(-3, 4)
print(list(numbers), "\n")

print("===== 複数演算子を連結した条件式")
for i in numbers:
    if 0 <= i < 3:
        print(f"{i:2}: {True}")
    else:
        print(f"{i:2}: {False}")

print("===== andで条件を書く場合")
for i in numbers:
    if i >= 0 and i < 3:
        print(f"{i:2}: {True}")
    else:
        print(f"{i:2}: {False}")

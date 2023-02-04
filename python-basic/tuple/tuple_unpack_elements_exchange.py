"""タプル基礎
タプルのアンパックの考え方を用いた要素の交換

[説明ページ]
https://tech.nkhn37.net/python-tuple-basic/#i-6
"""
data1 = "A"
data2 = "B"
print(
    f"data1: {data1}, id(data1): {id(data1)}, "
    f"data2: {data2}, id(data2): {id(data2)}"
)

# 要素の交換
data1, data2 = data2, data1
print(
    f"data1: {data1}, id(data1): {id(data1)}, "
    f"data2: {data2}, id(data2): {id(data2)}"
)

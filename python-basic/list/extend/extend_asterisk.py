"""リスト基礎
*演算子を用いたリストの拡張方法

[説明ページ]
https://tech.nkhn37.net/python-list-extend/#list-2
"""
# *演算子でlistを拡張する。
data = ["A", "B", "C"]

new_data = data * 3
print(f"data: {data}, id(data): {id(data)}")
print(f"new_data: {new_data}, id(new_data): {id(new_data)}")

# *=を使って拡張する。
print("===")
print(f"*=実行前　data: {data}, id(data): {id(data)}")
data *= 3
print(f"*=実行後　data: {data}, id(data): {id(data)}")

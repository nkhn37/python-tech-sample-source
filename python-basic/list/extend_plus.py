"""リスト基礎
+演算子を用いたリストの拡張方法
・+=演算子を用いて拡張した場合はextendメソッドと同じ結果になる

[説明ページ]
https://tech.nkhn37.net/python-list-extend/#list
"""
# +演算子でlistを追加する。
data = ['A', 'B', 'C', 'D', 'E']
add_data = ['F', 'G', 'H']

new_data = data + add_data
print(f'data: {data}, id(data): {id(data)}')
print(f'new_data: {new_data}, id(new_data): {id(new_data)}')

# +=を使う場合は、結果としてはextendと同じ
print('===')
print(f'+=実行前　data: {data}, id(data): {id(data)}')
data += add_data
print(f'+=実行後　data: {data}, id(data): {id(data)}')

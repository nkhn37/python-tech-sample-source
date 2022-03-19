"""リスト基礎
extendメソッドとappendメソッドの違い

・extendメソッドの場合は、追加するリストの各要素が既存のリストに順番に追加される。
・appendメソッドを用いてリストを追加した場合は、追加するリスト全体が一つの要素として、
既存のリストに追加される。

[説明ページ]
https://tech.nkhn37.net/python-list-extend/#extendappend
"""
print('===== extendの場合')
data = ['A', 'B', 'C', 'D', 'E']
add_data = ['F', 'G', 'H']

data.extend(add_data)
print(f'data: {data}')

print('\n===== appendの場合')
data = ['A', 'B', 'C', 'D', 'E']
add_data = ['F', 'G', 'H']

data.append(add_data)
print(f'data: {data}')

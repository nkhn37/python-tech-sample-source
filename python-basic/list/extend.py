"""リスト基礎
extendメソッドで既存のリストに新しいリストを追加する方法
・既存のリストそのものが変更される

[説明ページ]
https://tech.nkhn37.net/python-list-extend/#extend
"""
# listに新しいlistを追加する
data = ['A', 'B', 'C', 'D', 'E']
add_data = ['F', 'G', 'H']

print(f'extend実行前　data: {data}, id(data): {id(data)}')
data.extend(add_data)
print(f'extend実行後　data: {data}, id(data): {id(data)}')

"""リスト基礎
リスト内の要素の有無を確認する方法

[説明ページ]
https://tech.nkhn37.net/python-list-in-notin/
"""
data = ['A', 'B', 'C', 'D', 'E']

# リスト内に特定の要素が存在することを確認する。
print('=== in ===')
print('A' in data)
print('Z' in data)

# リスト内に特定の要素が存在しないことを確認する
print('\n=== not in ===')
print('A' not in data)
print('Z' not in data)

"""リスト基礎
リスト内包表記の使い方（複数リストから新しいリストを作成）

[説明ページ]
https://tech.nkhn37.net/python-list-comprehension/#i-2

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# 複数のリストから新しいリストを作成する。
# リスト内包表記を用いる
data1 = [1, 2, 3, 4, 5]
data2 = [11, 12, 13, 14, 15]
new_data = [i * j for i in data1 if i % 2 == 0 for j in data2 if j % 2 == 0]

print(f'new_data: {new_data}')

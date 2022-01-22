"""リスト基礎
複数の要素位置を取得したい場合の対応方法
（index関数ではなく、リスト内包表記を用いる）

[説明ページ]
https://tech.nkhn37.net/python-list-index/#i-2
"""
# 複数の要素位置を取得したい場合
data = ['A', 'B', 'C', 'A', 'B', 'C', 'D', 'A', 'B']

idx_list = [i for i, d in enumerate(data) if d == 'B']
print(f'idx_list: {idx_list}')

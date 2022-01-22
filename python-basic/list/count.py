"""リスト基礎
リストの要素数をカウントする方法

[説明ページ]
https://tech.nkhn37.net/python-list-count/
"""
# リスト内の同一要素の要素数をカウントする
data = ['A', 'B', 'A', 'C', 'D', 'E', 'A']

cnt = data.count('A')
print(f'cnt: {cnt}')

# 見つからない場合は0を返す
cnt = data.count('Z')
print(f'cnt: {cnt}')

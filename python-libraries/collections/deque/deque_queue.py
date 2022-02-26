"""Collectionsモジュール
dequeでキューやスタックを実現する
キュー（queue）操作の実現

[説明ページ]
https://tech.nkhn37.net/python-collections-deque/#queue
"""
import collections

# dequeの作成
data = collections.deque()

# データの追加
data.append(10)
data.append(20)
data.append(30)
data.append(40)

# 先頭からのデータ取り出し
print(data)
print(data.popleft())
print(data)
print(data.popleft())
print(data)

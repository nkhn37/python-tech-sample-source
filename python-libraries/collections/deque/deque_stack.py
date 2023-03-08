"""Collectionsモジュール
dequeでキューやスタックを実現する
スタック（stack）操作の実現

[説明ページ]
https://tech.nkhn37.net/python-collections-deque/#dequestack
"""
import collections

# dequeの作成
data = collections.deque()

# データの追加
data.append(10)
data.append(20)
data.append(30)
data.append(40)

# 末尾からのデータ取り出し
print(data)
print(data.pop())
print(data)
print(data.pop())
print(data)

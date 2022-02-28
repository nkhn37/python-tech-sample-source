"""Collectionsモジュール
Counterでカウント数のみを取り出すvaluesメソッド

[説明ページ]
https://tech.nkhn37.net/python-collections-counter/#values
"""
import collections

data = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'b', 'd', 'd']

counter = collections.Counter(data)

print(counter)

print('=====')
# カウント数の値のみをを取り出す
print(counter.values())
# カウント数の合計を計算する
print(sum(counter.values()))

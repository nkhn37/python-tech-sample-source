"""Collectionsモジュール
Counterで要素数をカウントする

[説明ページ]
https://tech.nkhn37.net/python-collections-counter/#Counter
"""
import collections

data = ["a", "a", "a", "b", "b", "c", "a", "b", "d", "d"]

counter = collections.Counter(data)

print(counter)
print(counter["a"])

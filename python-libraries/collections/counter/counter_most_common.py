"""Collectionsモジュール
Counterで上位を抽出するmost_commonメソッド

[説明ページ]
https://tech.nkhn37.net/python-collections-counter/#most_common
"""
import collections

data = ["a", "a", "a", "b", "b", "c", "a", "b", "d", "d"]

counter = collections.Counter(data)

print(counter)

print("=====")
# 上位1位までを抽出
print(counter.most_common(1))
# 上位2位までを抽出
print(counter.most_common(2))
# 引数なしだとすべて抽出
print(counter.most_common())

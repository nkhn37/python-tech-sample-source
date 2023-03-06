"""Collectionsモジュール
defaultdictの定義と使い方
0で初期化する場合(lambdaで記載)

[説明ページ]
https://tech.nkhn37.net/python-collections-defaultdict/#int0
"""
import collections

data = ["A", "B", "A", "C", "D", "B", "A", "B", "D"]
# lambda関数で記載
dict_count = collections.defaultdict(lambda: int())

for key in data:
    dict_count[key] += 1

print(dict_count)

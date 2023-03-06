"""Collectionsモジュール
defaultdictの定義と使い方
0.0で初期化する場合(lambdaで記載)

[説明ページ]
https://tech.nkhn37.net/python-collections-defaultdict/#float00
"""
import collections

data = ["A", "B", "A", "C", "D", "B", "A", "B", "D"]
# lambdaで記載
dict_count = collections.defaultdict(lambda: float())

for key in data:
    dict_count[key] += 1.0

print(dict_count)

"""Collectionsモジュール
defaultdictの定義と使い方

[説明ページ]
https://tech.nkhn37.net/python-collections-defaultdict/#collectionsdefaultdict
"""
import collections

data = ['A', 'B', 'A', 'C', 'D', 'B', 'A', 'B', 'D']
dict_count = collections.defaultdict(lambda: int())

# # 以下のような書き方もOK
# dict_count = collections.defaultdict(int)
# # floatをデフォルトにする場合の例は以下
# dict_count = collections.defaultdict(lambda: float())
# dict_count = collections.defaultdict(float)

for key in data:
    dict_count[key] += 1

print(dict_count)

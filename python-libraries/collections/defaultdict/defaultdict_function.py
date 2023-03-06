"""Collectionsモジュール
defaultdictの定義と使い方
関数で任意の規定値を定義可能

[説明ページ]
https://tech.nkhn37.net/python-collections-defaultdict/#i-2
"""
import collections


def init_dict():
    # 本来複雑な処理を書けるが例として1を返却するのみ
    return 1


data = ["A", "B", "A", "C", "D", "B", "A", "B", "D"]
dict_count = collections.defaultdict(init_dict)

for key in data:
    dict_count[key] += 1

print(dict_count)

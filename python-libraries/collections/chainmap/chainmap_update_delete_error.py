"""Collectionsモジュール
ChainMapでチェーン上の辞書を更新、削除する
※以下のプログラムはKeyErrorのエラーとなる
　対応版のプログラムはchainmap_deepchainmap.pyを参照

[説明ページ]
https://tech.nkhn37.net/python-collections-chainmap/#ChainMap-3
"""
import collections

dict_a = {"a": "A"}
dict_b = {"b": "B"}
dict_c = {"c": "C"}

# ChainMapを用いて辞書を連結する
d_map = collections.ChainMap(dict_c, dict_b, dict_a)
print(d_map)

print("=====")
# 値を更新する
d_map["b"] = "B_update"
print(d_map)

print("=====")
# 値を削除する
del d_map["a"]
print(d_map)

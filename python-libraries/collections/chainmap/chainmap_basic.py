"""Collectionsモジュール
ChainMapで辞書を連結する

[説明ページ]
https://tech.nkhn37.net/python-collections-chainmap/#ChainMap
"""
import collections

dict_a = {'a': 'A', 'b': 'B'}
dict_b = {'b': 'BB', 'c': 'CC'}
dict_c = {'b': 'BBB', 'c': 'CCC'}

# ChainMapを用いて辞書を連結する
d_map = collections.ChainMap(dict_a, dict_b, dict_c)
print(d_map)
print(type(d_map.maps), d_map.maps)
print(f"d_map['a'] = {d_map['a']}, d_map['b'] = {d_map['b']}, "
      f"d_map['c'] = {d_map['c']}")

print('=====')
# 連結順を逆転させる
d_map.maps.reverse()
print(d_map)
print(type(d_map.maps), d_map.maps)
print(f"d_map['a'] = {d_map['a']}, d_map['b'] = {d_map['b']}, "
      f"d_map['c'] = {d_map['c']}")

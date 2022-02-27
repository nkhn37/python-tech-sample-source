"""辞書によるdictの連結
（collections.ChainMapとの対比のためのプログラム）

[説明ページ]
https://tech.nkhn37.net/python-collections-chainmap/#dictupdate
"""
dict_a = {'a': 'A', 'b': 'B'}
dict_b = {'b': 'BB', 'c': 'CC'}
dict_c = {'b': 'BBB', 'c': 'CCC'}

dict_a.update(dict_b)
print(dict_a)
dict_a.update(dict_c)
print(dict_a)

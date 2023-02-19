"""ジェネレータ基礎
ジェネレータ内包表記の使い方
（タプルやリストに変換して使用する方法）

[説明ページ]
https://tech.nkhn37.net/python-generator-comprehension/#i-3

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# ジェネレータからタプルに変換
gen = (i for i in range(10) if i % 2 == 0)
tpl_tmp = tuple(gen)
print(type(tpl_tmp), tpl_tmp)

# ジェネレータからリストに変換
gen = (i for i in range(10) if i % 2 == 0)
list_tmp = list(gen)
print(type(list_tmp), list_tmp)

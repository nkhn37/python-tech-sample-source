"""map関数の使い方の基本
ラムダ関数(無名関数)を使用する場合

[説明ページ]
https://tech.nkhn37.net/python-map-basic/#i-5
"""
tmp_list = [1, 2, 3, 4, 5]

# map関数を適用し、リストで取得
result = list(map(lambda x: x**2, tmp_list))
print(result)

# map関数を適用し、タプルで取得
result = tuple(map(lambda x: x**2, tmp_list))
print(result)

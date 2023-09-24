"""filter関数の使い方の基本
ラムダ関数(無名関数)を使用する場合

[説明ページ]
https://tech.nkhn37.net/python-filter-basic/#i-3
"""
tmp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter関数を適用し、リストで取得
result = list(filter(lambda x: x % 2 == 0, tmp_list))
print(result)

# filter関数を適用し、タプルで取得
result = tuple(filter(lambda x: x % 2 == 0, tmp_list))
print(result)

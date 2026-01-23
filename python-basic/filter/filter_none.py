"""filter 関数の使い方の基本
関数の引数に None を指定する場合

[説明ページ]
https://tech.nkhn37.net/python-filter-basic
"""

tmp_list = [0, 1, "", "Hello", [], [1, 2, 3], None, True, False]

# None を指定すると要素の truthy/falsy で判定される
result = list(filter(None, tmp_list))
print(result)

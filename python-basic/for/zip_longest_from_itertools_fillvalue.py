"""for文基礎
iter_tools.zip_longestで任意の指定値で補完したい場合
（fillvalueオプションを使用する）

iter_tools.zip_longestの使用方法は、zip_longest_from_itertools.pyを参照

[説明ページ]
https://tech.nkhn37.net/python-for-zip/#iter_toolszip_logestfillvalue
"""
# itertools.zip_longestで、補完する値を指定する
import itertools

data1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data2 = ['A', 'B', 'C', 'D', 'E']

for dt1, dt2 in itertools.zip_longest(data1, data2, fillvalue='Z'):
    print(f'dt1: {dt1}, dt2: {dt2}')

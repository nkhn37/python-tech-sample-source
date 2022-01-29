"""for文基礎
要素数が異なるリストをまとめて繰り返し処理する場合、要素数が多い方にあわせて
足りない部分を補って処理する方法
（itertools.zip_logestを使用する）

足りない部分はNoneが補完される。指定した値で補完したい場合はfillvalueオプションを使用する。
サンプルソースコードはzip_longest_from_itertools_fillvalue.pyを参照

[説明ページ]
https://tech.nkhn37.net/python-for-zip/#itertoolszip_longest
"""
# itertools.zip_longestを用いて、不足分を補完する
import itertools

data1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data2 = ['A', 'B', 'C', 'D', 'E']

for dt1, dt2 in itertools.zip_longest(data1, data2):
    print(f'dt1: {dt1}, dt2: {dt2}')

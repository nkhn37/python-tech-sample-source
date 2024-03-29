"""for文基礎
zipで要素数が異なる場合の実行結果
（zipは少ない要素数のリストにあわせて実行される）

※要素数が多い方に併せて足りなう部分を補って処理するにはitertools.zip_longestを使用します。
サンプルソースコードはzip_longest_from_itertools.pyを参照

[説明ページ]
https://tech.nkhn37.net/python-for-zip/#zip-2
"""
data1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data2 = ["A", "B", "C", "D", "E"]

# 要素の長さが異なる場合(少ない要素数にあわせて実行される)
for dt1, dt2 in zip(data1, data2):
    print(f"dt1: {dt1}, dt2: {dt2}")

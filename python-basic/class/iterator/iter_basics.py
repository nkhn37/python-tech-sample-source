"""イテレータ（iteratorの基本）
iter関数でイテレータを作成する例

[説明ページ]
https://tech.nkhn37.net/python-iterator-basics/#iterator-2
"""
sample = "python"

# イテレータを作成
i = iter(sample)
print(type(i))

# 値を順に取り出す
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# 全て取り出し終わるとStopIteration例外となる
print(next(i))

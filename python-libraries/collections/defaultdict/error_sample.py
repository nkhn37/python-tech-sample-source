"""collections.defaultdict
defaultdictを使いたい理由:
以下のプログラムでは最初のアクセスタイミングで"A"が辞書ないにないためKeyErrorとなる。

[説明ページ]
https://tech.nkhn37.net/python-collections-defaultdict/#i
"""
data = ["A", "B", "A", "C", "D", "B", "A", "B", "D"]
dict_count = {}

for key in data:
    dict_count[key] += 1

print(dict_count)

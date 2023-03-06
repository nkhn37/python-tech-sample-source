"""collections.defaultdict
defaultdictを使わないで初期値を扱う場合

[説明ページ]
https://tech.nkhn37.net/python-collections-defaultdict/#i
"""
data = ["A", "B", "A", "C", "D", "B", "A", "B", "D"]
dict_count = {}

for key in data:
    if key in dict_count:
        dict_count[key] += 1
    else:
        dict_count[key] = 1

print(dict_count)

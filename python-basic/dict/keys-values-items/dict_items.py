"""辞書基礎
辞書の要素を列挙するビューを作成する (itemsメソッド)

[説明ページ]
https://tech.nkhn37.net/python-dict-keys-values-items/#_items
"""
d = {"k1": 10, "k2": 20, "k3": 30, "k4": 40, "k5": 50}

# items()で要素のビューを取得する
itm_v = d.items()
print(type(itm_v))
print(f"itm_v: {itm_v}")

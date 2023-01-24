"""辞書基礎
辞書の値を列挙するビューを作成する (valuesメソッド)

[説明ページ]
https://tech.nkhn37.net/python-dict-keys-values-items/#_values
"""
d = {"k1": 10, "k2": 20, "k3": 30, "k4": 40, "k5": 50}

# values()で値のビューを取得する
val_v = d.values()
print(type(val_v))
print(f"val_v: {val_v}")

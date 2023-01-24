"""辞書基礎
辞書のキーを列挙するビューを作成する (keysメソッド)

[説明ページ]
https://tech.nkhn37.net/python-dict-keys-values-items/#_keys
"""
d = {"k1": 10, "k2": 20, "k3": 30, "k4": 40, "k5": 50}

# keys()でキーのビューを取得する
key_v = d.keys()
print(type(key_v))
print(f"key_v: {key_v}")

"""辞書基礎
keys, values, itemsのビューとしての特徴

[説明ページ]
https://tech.nkhn37.net/python-dict-keys-values-items/#keysvaluesitems
"""
d = {'k1': 10, 'k2': 20, 'k3': 30, 'k4': 40, 'k5': 50}

# items()で要素のビューを取得する
itm_v = d.items()
print(f'itm_v: {itm_v}')

# 元の辞書にデータを追加する。
d['k6'] = 60

# データ追加前に作成したビューを確認してみる。
print(f'itm_v: {itm_v}')

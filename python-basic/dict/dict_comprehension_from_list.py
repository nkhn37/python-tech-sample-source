"""辞書基礎
辞書内包表記の使い方
（既存のリストから辞書を作成する）

[説明ページ]
https://tech.nkhn37.net/python-dict-comprehension/#i-2

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# キーと値のそれぞれのリストから辞書を作成する例
keys = ['k1', 'k2', 'k3', 'k4', 'k5']
values = [10, 20, 30, 40, 50]

data = {k: v for k, v in zip(keys, values) if v >= 30}
print(f'data: {data}')

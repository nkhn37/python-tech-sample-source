"""辞書基礎
辞書内包表記の使い方
（既存の辞書から新しい辞書を作成する）

[説明ページ]
https://tech.nkhn37.net/python-dict-comprehension/#i-3

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# 辞書から新しい辞書を作成する例
d = {'k1': 10, 'k2': 15, 'k3': 20, 'k4': 25, 'k5': 30}

data = {k: v for k, v in d.items() if v % 2 == 0}
print(f'data: {data}')

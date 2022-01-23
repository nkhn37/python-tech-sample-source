"""辞書基礎
辞書内包表記を使用しない場合の記載
（辞書内包表記版はdict_comprehension_from_dict.pyを参照）

辞書内包表記は記載がシンプルになるだけではなく、速度も高速なことから
同じ書き方ができる場合は、辞書内包表記を利用することを検討しましょう。

[説明ページ]
https://tech.nkhn37.net/python-dict-comprehension/#i-3

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# 辞書から新しい辞書を作成する例
d = {'k1': 10, 'k2': 15, 'k3': 20, 'k4': 25, 'k5': 30}

# 内包表記を使わない場合
data = {}
for k, v in d.items():
    if v % 2 == 0:
        data[k] = v
print(f'data: {data}')

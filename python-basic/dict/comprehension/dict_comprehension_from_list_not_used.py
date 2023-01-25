"""辞書基礎
辞書内包表記を使用しない場合の記載
（辞書内包表記版はdict_comprehension_from_list.pyを参照）

辞書内包表記は記載がシンプルになるだけではなく、速度も高速なことから
同じ書き方ができる場合は、辞書内包表記を利用することを検討しましょう。

[説明ページ]
https://tech.nkhn37.net/python-dict-comprehension/#i-3

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# キーと値のそれぞれのリストから辞書を作成する例
keys = ["k1", "k2", "k3", "k4", "k5"]
values = [10, 20, 30, 40, 50]

# 内包表記を使わない場合
data = {}
for k, v in zip(keys, values):
    if v >= 30:
        data[k] = v
print(f"data: {data}")
